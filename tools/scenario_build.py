#!/usr/bin/env python3
"""Scenario authoring DSL + JSON builder.

Each scene module exposes build(S). S.line() appends a node; by default a node
flows into the next appended node. S.choice() attaches choices to the previous
line. Labels make jump targets readable; they are resolved at the end.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

import s0_prologue, s1_day1, s2_night1, s3_rainy, s4_alley, s5_last  # noqa: E402

MODULES = (s0_prologue, s1_day1, s2_night1, s3_rainy, s4_alley, s5_last)


class Scene:
    def __init__(self):
        self.nodes = []
        self.labels = {}
        self.used_ids = set()

    # ---- primitives -------------------------------------------------
    def line(self, text=None, who=None, e=None, bg=None, ch=None, show=None,
             hide=False, bgm=None, weather=None, fx=None, eff=None,
             ending=None, choices=None, show2=None, hide2=False, rain=None):
        nid = "n%03d" % (len(self.nodes) + 1)
        node = {}
        if who:
            node["who"] = who
        if text:
            node["text"] = text
        if e:
            node["e"] = e
        if bg:
            node["bg"] = bg
        if ch:
            node["ch"] = ch
        if show:
            node["show"] = show
        if hide:
            node["hide"] = True
        if show2:
            node["show2"] = show2
        if hide2:
            node["hide2"] = True
        if bgm:
            node["bgm"] = bgm
        if weather:
            node["weather"] = weather
        if fx:
            node["fx"] = fx
        if ending:
            node["ending"] = ending
        if choices:
            node["choices"] = choices
        if rain is not None:
            node["rain"] = rain
        self.nodes.append({"id": nid, "node": node})
        return nid

    def label(self, name):
        if name in self.labels:
            raise SystemExit("duplicate label: %s" % name)
        self.labels[name] = "n%03d" % (len(self.nodes) + 1)

    def choice(self, options, prompt=None):
        """Attach choices to the last line node."""
        last = self.nodes[-1]
        last["node"]["choices"] = options
        return last["id"]

    def goto(self, label):
        nid = "n%03d" % (len(self.nodes) + 1)
        self.nodes.append({"id": nid, "node": {"goto": "@" + label}})
        return nid

    def branch(self, rules):
        """rules: list of (cond, label). Last entry should be (None, label)."""
        nid = "n%03d" % (len(self.nodes) + 1)
        self.nodes.append({"id": nid, "node": {"branch": rules}})
        return nid

    # ---- finalize ---------------------------------------------------
    def finish(self):
        out = {}
        nodes = self.nodes
        label_targets = {v: k for k, v in self.labels.items()}

        for i, item in enumerate(nodes):
            n = item["node"]
            if "goto" in n:
                n["next"] = n.pop("goto")
            if "branch" in n:
                n["branch"] = [
                    {"if": c, "next": "@" + t} if c else {"next": "@" + t}
                    for c, t in n["branch"]
                ]
            if "choices" in n:
                for c in n["choices"]:
                    if "to" in c:
                        c["next"] = "@" + c.pop("to")
            # implicit next: the following node
            if ("next" not in n and "choices" not in n and "branch" not in n
                    and "ending" not in n and i + 1 < len(nodes)):
                n["next"] = nodes[i + 1]["id"]

        # resolve @label
        for item in nodes:
            n = item["node"]

            def ref(v):
                if isinstance(v, str) and v.startswith("@"):
                    key = v[1:]
                    if key not in self.labels:
                        raise SystemExit("unknown label: %s" % key)
                    return self.labels[key]
                return v

            if "next" in n:
                n["next"] = ref(n["next"])
            if "branch" in n:
                for b in n["branch"]:
                    b["next"] = ref(b["next"])
            if "choices" in n:
                for c in n["choices"]:
                    c["next"] = ref(c["next"])

        meta = META
        meta["count"] = len(nodes)
        for item in nodes:
            out[item["id"]] = item["node"]
        meta["start"] = nodes[0]["id"]
        meta["labelIndex"] = label_targets
        return {"meta": meta, "nodes": out}


META = {
    "title": "새벽 한 시, 달의 뒷면",
    "subtitle": "골목 끝 심야 카페 스무 밤",
    "affMax": 18,
    "heroines": {
        "doyeon": {"name": "한도연", "role": "달의 뒷면 사장 · 수석 바리스타", "color": "#c98a4e"},
        "harin": {"name": "유하린", "role": "골목의 소리를 그리는 미대생", "color": "#a89ed6"},
    },
    "endings": {
        "doyeon_happy": {
            "no": "01", "label": "HAPPY END", "title": "마감 종이 울려도",
            "desc": "새벽 한 시, 문을 닫지 않기로 했다. 삼 년 동안 혼자였던 골목을 이제는 둘이 걷는다.",
        },
        "doyeon_normal": {
            "no": "02", "label": "NORMAL END", "title": "다음 계절의 원두",
            "desc": "말하지 못한 마음은 마감 후의 시간에 두고 왔다. 그래도 매주 금요일, 그 불빛은 켜져 있다.",
        },
        "harin_happy": {
            "no": "03", "label": "HAPPY END", "title": "이어폰 한쪽씩",
            "desc": "골목의 소리로 만든 첫 곡의 제목은 새벽 한 시. 이제 그 곡은 두 사람이 함께 듣는다.",
        },
        "harin_normal": {
            "no": "04", "label": "NORMAL END", "title": "그림의 뒷면",
            "desc": "이름을 묻지 않는 가게에서 만난 사람은, 작품 속에 이름 없는 사람으로 남았다.",
        },
        "true_end": {
            "no": "05", "label": "TRUE END", "title": "우리 셋의 마지막 주문",
            "desc": "달의 뒷면은 아무도 못 본다. 하지만 이제 그걸 봐 주는 사람이 셋이다.",
        },
    },
}


def main():
    S = Scene()
    for mod in MODULES:
        mod.build(S)
    data = S.finish()
    out = os.path.join(os.path.dirname(__file__), "..", "src", "data", "scenario.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print("wrote", out, len(data["nodes"]), "nodes", len(data["meta"]["endings"]), "endings")


if __name__ == "__main__":
    main()

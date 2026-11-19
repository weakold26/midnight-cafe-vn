#!/usr/bin/env python3
"""대사 화자와 화면에 서 있는 캐릭터가 어긋나는 지점을 찾는다."""
import json, os
from collections import deque

HERE = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(os.path.join(HERE, "..", "src", "data", "scenario.json"), encoding="utf-8"))
nodes, meta = data["nodes"], data["meta"]

WHO = {"한도연": "doyeon", "유하린": "harin"}


def test(c, aff, flags):
    if not c:
        return True
    if c.get("flag") and c["flag"] not in flags:
        return False
    for k, v in (c.get("affMin") or {}).items():
        if aff.get(k, 0) < v:
            return False
    return True


seen = set()
queue = deque([(meta["start"], {}, frozenset(), (None, None))])
issues = []
guard = 0
while queue:
    nid, aff, flags, who = queue.popleft()
    while True:
        guard += 1
        if guard > 400000:
            break
        n = nodes.get(nid)
        if not n:
            break
        main, side = who
        if n.get("hide"):
            main, side = None, None
        if n.get("hide2"):
            side = None
        if n.get("show"):
            main = n["show"]["id"]
        if n.get("show2"):
            side = n["show2"]["id"]
        who = (main, side)
        spk = WHO.get(n.get("who"))
        if spk and spk not in who:
            main = spk
            who = (main, side)
            issues.append((nid, n.get("who"), who, (n.get("text") or "")[:40]))
        if n.get("ending"):
            break
        if n.get("choices"):
            for c in n["choices"]:
                k = (c["next"], aff.get("haram", 0), aff.get("serin", 0), flags, who)
                if k not in seen and test(c.get("when"), aff, flags):
                    seen.add(k)
                    queue.append((c["next"], aff, flags, who))
            break
        nid2 = n.get("next")
        k = (nid2, aff.get("haram", 0), aff.get("serin", 0), flags, who)
        if k in seen:
            break
        seen.add(k)
        if not nid2:
            break
        nid = nid2

print("mismatch lines:", len(issues))
for i in issues:
    print(" ", i[0], "화자=%s / 화면=%s | %s" % i[1:])

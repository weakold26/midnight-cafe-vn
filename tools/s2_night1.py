# -*- coding: utf-8 -*-
"""사흘째 밤 — 마감 후 단둘, LP, 그리고 허당"""


def build(S):
    S.line(ch="사흘째 · 마감 후", bg="counter_night", bgm="lofi", rain=False,
           text="사흘째 되는 밤에, 하린이 평소보다 일찍 갔다. 시험 준비가 있다고, 스케치북을 반만 접어 들고 나갔다.")
    S.line(text="남은 사람은 둘. 마감 종이 울린 후의 가게는, 낮과 완전히 다른 장소가 됐다.")
    S.line(show={"id": "doyeon", "expr": "base"}, who="한도연",
           text="의자는 내가 올릴게요. 물은 냉장고에 있는 병에 부탁해요. 바닥은 조금만 밀고요.")
    S.line(who="나", text="역할이 정확하네요.")
    S.line(who="한도연", text="혼자 하던 걸 둘이 하면, 안 겹치게 나눠야 해요. 이건 삼 년 만에 처음 해 보는 거라, 아직 서툴러요.")
    S.line(text="그녀는 의자를 두 개씩 들었다. 한 손으로. 나는 그걸 보고 내가 두 개를 들고 두 번 오갔다.")
    S.line(who="한도연", e="base", text="…그렇게 하면 오래 걸려요.")
    S.line(who="나", text="그래도 이쪽이 덜 위험해요. 그렇게 들면 팔이 아프실 텐데.")
    S.line(text="그녀가 잠깐 손을 멈추고 나를 봤다. 아무 말 없이, 다음 의자부터는 한 개씩 들었다.")

    S.line(bg="counter_night", text="마감 종이 울리고 조명을 절반만 남겼다. 도연 씨가 벽 쪽으로 갔다. LP 판을 고르고 있었다.")
    S.line(who="한도연", text="오늘은 뭐 들을까요. 손님이 없으니까, 이제 우리가 손님이에요.")
    S.line(who="나", text="제가 골라도 돼요?")
    S.line(who="한도연", e="base", text="그럼요. 대신 하나만. 마감 후엔 한 장만 들어요. 그게 규칙이에요.")
    S.line(text="서른 장쯤 되는 LP 사이에서 내 손이 멈춘 곳은, 저 하얀 판이었다. 이름이 지워진 판.")
    S.line(who="나", text="이건 뭔가요?")
    S.line(who="한도연", e="serious", text="…그거요.")
    S.line(text="그녀가 잠깐 팔짱을 끼고, 벽에 기대서 나를 봤다. 대답을 고르는 시간이 길었다.")

    S.choice([
        {"t": "“이름이 지워진 게 계속 걸려서요. 그걸로 들어도 될까요?”", "to": "d3_lp_blank", "eff": {"doyeon": 2}, "flag": "lp_hint"},
        {"t": "“그럼 오늘 기분에 맞는 걸로 골라 주세요.”", "to": "d3_lp_her", "eff": {"doyeon": 2}},
        {"t": "“제가 아는 곡이 있으면 좋겠는데, 여기 있을까요?”", "to": "d3_lp_known", "eff": {"doyeon": 1}},
    ])

    S.label("d3_lp_blank")
    S.line(who="한도연", e="serious", text="…들어요. 대신, 이 판에 대해선 내가 먼저 말할 때까지 아무것도 묻지 말아요.")
    S.line(who="나", text="그렇게 할게요.")
    S.line(text="그녀가 판을 꺼내 턴테이블에 올렸다. 바늘이 내려앉는 소리, 그리고 몇 초의 잡음이 흘렀다.")
    S.line(text="피아노가 시작됐다. 아주 느렸다. 한 음과 다음 음 사이에, 숨 쉴 자리가 있었다.")
    S.line(who="한도연", text="이건 삼 년 전에, 내가 여기 두고 간 판이에요.")
    S.line(who="나", text="…두고 가셨어요?")
    S.line(who="한도연", e="base", text="네. 이 가게가 아직 내 가게가 아니었을 때요. 그때는 이 자리에 다른 가게가 있었고, 나는 그냥 손님이었어요.")
    S.line(text="그녀가 말을 멈췄다. 나는 아무것도 묻지 않았다. 방금 약속했으니까.")
    S.line(who="한도연", text="이름을 지운 건, 그때의 내가 이 판을 버리기로 마음먹었기 때문이에요. 근데 버리지 못했어요. 여기 두고 갔어요. 그리고 일 년 뒤에, 이 가게를 인수했어요.")
    S.line(who="나", text="그럼 지금은… 사장님 판이네요.")
    S.line(who="한도연", e="blush", text="그러니까 우습죠. 버리려던 걸 다시 사 온 셈이니까.")
    S.line(text="그녀가 컵을 들었다. 웃는 것 같기도 하고, 아닌 것 같기도 했다. 피아노는 아직 같은 자리를 맴돌고 있었다.")
    S.goto("d3_after_lp")

    S.label("d3_lp_her")
    S.line(who="한도연", e="base", text="기분에 맞는 걸로요? 그건 좀 어려운 주문인데.")
    S.line(who="나", text="사장님이 잘 아시잖아요.")
    S.line(text="그녀가 서랍에서 한 장을 꺼냈다. 겉표지에 손때가 많이 묻어 있었다.")
    S.line(text="관악기 소리가 먼저 왔다. 낮게 깔리다가, 갑자기 밝아졌다. 낮에 틀던 것과 달리, 조금 느긋했다.")
    S.line(who="한도연", text="이건 마감 후에만 들어요. 낮에 들으면 손님이 두 번 온 줄 알아요.")
    S.line(who="나", text="…그 정도예요?")
    S.line(who="한도연", e="base", text="이 판은 좀 나른해요. 나른한 음악은, 나른한 사람 옆에서만 들어야 하거든요.")
    S.line(text="그 말을 하고, 그녀가 스스로 조금 놀란 얼굴을 했다. 컵을 입에 대고, 그 뒤로 아무 말도 하지 않았다.")
    S.goto("d3_after_lp")

    S.label("d3_lp_known")
    S.line(who="한도연", e="base", text="아는 곡이요? 여기 있는 건 대부분 이십 년 넘은 것들이에요.")
    S.line(who="나", text="그럼 더 좋죠. 요즘 건 너무 잘 만들어져서, 가끔은 좀 지루하니까.")
    S.line(who="한도연", e="surprised", text="…그건 좀 어른 같은 말인데요.")
    S.line(who="나", text="방학이라서요.")
    S.line(text="그녀가 웃음을 참다가, 결국 아주 작게 냈다. 그리고 한 장을 골라 올렸다.")
    S.line(text="기타 소리가 나왔다. 녹음 상태가 좋지 않아서, 중간에 잡음이 섞였다. 그게 오히려 좋았다.")
    S.line(who="한도연", text="잡음이 있는 판은, 한 번 더 들어요. 잡음까지가 그 사람의 연주니까.")
    S.goto("d3_after_lp")

    S.label("d3_after_lp")
    S.line(bg="counter_night", text="한 장이 끝나갈 무렵, 도연 씨가 카운터 뒤에서 잔을 정리하고 있었다.")
    S.line(text="그녀가 접시를 들고 돌아서다가, 발을 헛디뎠다. 접시 하나가 손에서 미끄러졌다.")
    S.line(text="다행히 바닥에 떨어지기 전에 잡았다. 그런데 잡은 자세가 아주 우스웠다. 한쪽 다리를 들고, 접시를 가슴에 안은 채로.")
    S.line(who="한도연", e="surprised", text="….")
    S.line(text="나와 눈이 마주쳤다. 그녀가 아주 천천히 다리를 내렸다.")
    S.line(who="한도연", e="blush", text="방금, 못 본 걸로 해요.")
    S.line(text="그 말이 너무 진지해서, 오히려 웃음이 났다. 참으려고 했는데 늦었다.")

    S.choice([
        {"t": "“못 봤어요. 다만 소리는 들었어요.”", "to": "d3_clumsy_tease", "eff": {"doyeon": 2}},
        {"t": "“접시 잡는 솜씨는 진짜네요.”", "to": "d3_clumsy_praise", "eff": {"doyeon": 2}},
        {"t": "아무것도 못 본 얼굴로 컵을 닦는다.", "to": "d3_clumsy_ignore", "eff": {"doyeon": 1}},
    ])

    S.label("d3_clumsy_tease")
    S.line(who="한도연", e="blush", text="…소리요?")
    S.line(who="나", text="발이 미끄러지는 소리요. 아주 작았어요. 거의 못 들을 뻔했어요.")
    S.line(who="한도연", text="거의, 라고 하셨죠. 그 '거의'가 문제예요.")
    S.line(text="그녀가 접시를 내려놓고, 앞치마를 고쳐 매었다. 귀가 붉은 걸 숨기려는 동작이었다.")
    S.line(who="한도연", e="base", text="…여기선 내가 제일 조심하는 사람이었는데. 삼 년 동안 한 번도 안 넘어졌어요.")
    S.line(who="나", text="저 때문에 긴장하셨나요?")
    S.line(who="한도연", e="surprised", text="그런 말, 이렇게 바로 물으면 안 되는 거예요.")
    S.line(who="나", text="왜요?")
    S.line(who="한도연", e="blush", text="…대답을 준비할 시간이 없잖아요.")
    S.goto("d3_end")

    S.label("d3_clumsy_praise")
    S.line(who="나", text="그런데 접시는 안 떨어뜨리셨네요. 그건 좀 멋있었어요.")
    S.line(who="한도연", e="surprised", text="…멋있었어요?")
    S.line(who="나", text="네. 팔이 먼저 나갔어요. 생각보다 손이 빠르신가 봐요.")
    S.line(text="그녀가 접시를 내려놓고, 손바닥을 내려다봤다. 그리고 아주 작게 웃었다.")
    S.line(who="한도연", e="base", text="커피 내릴 때는 항상 느리게 하거든요. 흔들리면 맛이 달라져서. 근데 방금은… 몸이 먼저 움직였네요.")
    S.line(who="한도연", text="이런 건 칭찬이라고 하기 좀 그렇죠.")
    S.line(who="나", text="아니요. 저는 꽤 좋았는데요.")
    S.goto("d3_end")

    S.label("d3_clumsy_ignore")
    S.line(text="컵을 닦는 척했다. 아무것도 못 본 것처럼. 그녀도 아무 말 없이 접시를 정리했다.")
    S.line(text="몇 분 뒤, 그녀가 내 앞에 잔을 하나 놓았다. 아이스 아메리카노였다.")
    S.line(who="한도연", e="base", text="…고마워요.")
    S.line(who="나", text="뭘요?")
    S.line(who="한도연", text="못 본 척해 준 거요. 그게 생각보다 어려운 건데.")
    S.line(text="그 말을 하고 그녀는 카운터 안쪽으로 돌아갔다. 등을 보이면 조금 편해지는 사람이 있다.")
    S.goto("d3_end")

    S.label("d3_end")
    S.line(bg="counter_night", text="새벽 두 시. 오븐에서 빵이 나왔다. 오늘은 식빵이 아니라, 작은 소금빵이었다.")
    S.line(show={"id": "doyeon", "expr": "base"}, who="한도연", text="이건 실패한 거예요. 모양이 안 나왔어요. 그래서 팔 수 없고.")
    S.line(who="나", text="그럼요?")
    S.line(who="한도연", text="우리가 먹죠.")
    S.line(text="소금빵은 아직 뜨거웠다. 손으로 잡으면 조금 아플 정도로.")
    S.line(who="한도연", e="base", text="마감 후에 굽는 빵은, 사실 파는 것보다 이게 많아요. 실패한 것들.")
    S.line(who="나", text="실패한 걸 왜 매일 굽세요?")
    S.line(who="한도연", text="실패해야 다음 게 나와요. 그리고… 실패한 빵은, 아침에 사 가는 사람이 없거든요. 그러면 밤에 오는 사람 몫으로 남죠.")
    S.line(text="그녀가 소금빵 하나를 집어 들었다. 깨물기 전에 잠깐 불어서 식혔다. 그 동작이 이상하게 다정해서, 나는 내 빵을 들고 한참을 그냥 서 있었다.")
    S.line(who="한도연", e="base", text="왜 안 먹어요?")
    S.line(who="나", text="…식히는 중이에요.")
    S.line(who="한도연", text="거짓말. 그냥 보고 있었죠.")
    S.line(text="나는 반박하지 못했다. 새벽 두 시의 가게는, 거짓말이 잘 통하지 않는 곳이었다.")

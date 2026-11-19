# -*- coding: utf-8 -*-
"""프롤로그 — 비 오는 골목, 달의 뒷면"""


def build(S):
    S.line(ch="프롤로그 · 비 오는 골목", bg="alley_dawn", bgm="lofi", rain=True,
           text="방학 첫날, 나는 우산을 접지 못한 채 골목 끝에 서 있었다.")
    S.line(text="비는 오후부터 내렸다. 오후에는 그냥 비였는데, 밤이 되니까 골목의 돌바닥을 전부 거울로 만들어 놓았다.")
    S.line(text="가로등이 하나, 간판이 하나. 그 두 개의 불빛이 물 위에서 길게 늘어져 있었다.")
    S.line(text="골목 끝, 계단 세 칸 위. 작은 나무 간판에 손글씨로 적혀 있었다. 달의 뒷면.")
    S.line(text="그 아래에 A4 한 장이 붙어 있었다. 비에 젖어 글씨가 조금 번져 있었다. 주말 알바 구함. 커피 배울 사람.")
    S.line(text="알바를 구하는 사람이 아니라, 알바를 가르쳐 주겠다는 쪽이었다. 그게 이상하게 마음에 걸렸다.")
    S.line(text="우산을 접고 계단을 올라갔다. 문을 두드리자, 안쪽에서 잔이 부딪는 소리가 났다.")
    S.line(bg="counter_night", rain=True, text="문이 열렸다. 조명이 은은한 실내에는 커피 냄새와, 아주 옅게 구운 빵 냄새가 섞여 있었다.")
    S.line(show={"id": "doyeon", "expr": "base"}, who="한도연",
           text="마감 삼십 분 전인데. 커피 마시러 오셨어요?")
    S.line(text="긴 머리를 한쪽으로 묶은 사람이 문을 잡은 채로 나를 봤다. 앞치마 위에 손을 올린 채, 표정은 놀랄 만큼 차분했다.")
    S.line(who="나", text="아, 저기. 문에 붙은 종이요. 알바.")
    S.line(who="한도연", e="surprised", text="…비 오는데 이 시간에요?")
    S.line(who="나", text="오늘 안에 정해야 했어서요. 내일부터 다른 데를 알아봐야 하니까.")
    S.line(text="그녀가 잠깐 나를 내려다보듯 봤다. 우산에서 떨어진 물이 신발 앞에 작은 웅덩이를 만들었다.")
    S.line(who="한도연", e="base", text="들어오세요. 물기부터 닦고.")

    S.choice([
        {"t": "\"안녕하세요. 공고 보고 왔습니다. 늦은 시간에 죄송해요.\"", "to": "p_greet_polite", "eff": {"doyeon": 2}},
        {"t": "\"여기 커피 맛있으면 일할게요. 아니면 다시 갈게요.\"", "to": "p_greet_joke", "eff": {"doyeon": 1}, "flag": "bold"},
        {"t": "말없이 우산을 잘 접어 문 옆에 세워 둔다.", "to": "p_greet_quiet", "eff": {"doyeon": 1}},
    ])

    S.label("p_greet_polite")
    S.line(text="허리를 숙이자 그녀가 손을 저었다. 마감 준비를 하던 손이었는지, 손끝에서 시나몬 냄새가 났다.")
    S.line(who="한도연", e="base", text="사과할 일은 아니에요. 이 시간에 오는 사람은, 보통 급한 사람이니까.")
    S.line(who="한도연", text="여기 앉으세요. 문가 말고, 저쪽. 문가 자리는 밤에 춥거든요.")
    S.line(text="그 말이 이상하게 오래 남았다. 문가 자리가 춥다는 걸 아는 사람은, 거기에 오래 앉아 본 사람일 테니까.")
    S.goto("p_after_greet")

    S.label("p_greet_joke")
    S.line(text="그녀가 한 박자 멈췄다. 그리고 아주 작게 웃었다. 처음 보는 웃음인데, 낯설지가 않았다.")
    S.line(who="한도연", e="base", text="그럼 커피부터 드셔야겠네요. 떨어지면 못 일해요.")
    S.line(who="나", text="떨어지면요?")
    S.line(who="한도연", text="그럼 다른 데 가셔야죠. 대신 여기 커피는, 떨어질 일이 없게 내려요.")
    S.line(text="그 말이 농담인지 자랑인지 알 수 없었는데, 어느 쪽이어도 좋았다.")
    S.goto("p_after_greet")

    S.label("p_greet_quiet")
    S.line(text="우산을 접어 문 옆에 세워 두자, 그녀가 그걸 보고 조금 놀란 얼굴을 했다.")
    S.line(who="한도연", e="surprised", text="…우산을 그렇게 접는 사람은 처음 봐요. 물이 안 떨어지게 접었네요.")
    S.line(who="나", text="젖은 채로 두면 바닥이 미끄러우니까요.")
    S.line(who="한도연", e="base", text="네. 그거, 여기서 꽤 중요한 거예요.")
    S.line(text="그녀가 앞치마 주머니에서 행주를 꺼내 내 앞의 물기를 닦았다. 내가 하겠다고 하기 전에, 이미 다 닦여 있었다.")
    S.goto("p_after_greet")

    S.label("p_after_greet")
    S.line(who="한도연", text="앉아요. 커피 한 잔 내릴 동안 생각해 볼게요.")
    S.line(text="바 카운터 안쪽. 그녀가 원두를 꺼내 저울에 올렸다. 숫자를 보고, 조금 덜어내고, 다시 올렸다.")
    S.line(text="그 손이 정확했다. 이 가게에서 가장 조용한 소리는, 저울이 균형을 잡을 때 나는 아주 작은 딸깍이었다.")
    S.line(who="한도연", text="여기는 아침 아홉 시에 열어요. 새벽 한 시에 닫고요. 하루 열여섯 시간.")
    S.line(who="나", text="혼자 하세요?")
    S.line(who="한도연", e="base", text="삼 년 했어요. 혼자서.")
    S.line(text="컵을 내 앞에 놓았다. 크림이 없는데도 표면이 매끈했다. 그녀가 잠깐 손을 멈추고 나를 봤다.")
    S.line(who="한도연", text="마셔 보세요. 그리고 솔직하게 말해 주세요. 손님한테는 못 묻는 말이거든요.")

    S.choice([
        {"t": "\"산미가 먼저 오는데, 끝이 깨끗해요.\"", "to": "p_taste_acid", "eff": {"doyeon": 2}, "flag": "coffee_talk"},
        {"t": "\"따뜻해서 좋아요. 이런 말 하면 안 되나요?\"", "to": "p_taste_warm", "eff": {"doyeon": 2}},
        {"t": "\"이거… 팔아도 되겠는데요.\"", "to": "p_taste_joke", "eff": {"doyeon": 1}},
    ])

    S.label("p_taste_acid")
    S.line(who="한도연", e="surprised", text="…산미를 먼저 짚네요. 방금 배운 말은 아닌 것 같은데.")
    S.line(who="나", text="집에서 자주 내려 마셔서요. 잘은 몰라도, 쓴맛이 남는 커피는 싫어해서.")
    S.line(who="한도연", e="base", text="좋아요. 그게 시작이에요. 잘 아는 사람보다, 싫은 걸 아는 사람이 오래 해요.")
    S.line(text="그녀가 내 컵 옆에 작은 유리잔을 하나 더 놓았다. 물이었다.")
    S.line(who="한도연", text="다음 잔 전에 입을 헹구세요. 그러면 두 번째 잔이 더 잘 보여요.")
    S.goto("p_offer")

    S.label("p_taste_warm")
    S.line(who="한도연", e="blush", text="…그런 말, 손님한테 들으면 좀 곤란한데.")
    S.line(who="나", text="안 되나요?")
    S.line(who="한도연", e="base", text="안 되는 건 아니에요. 다만 그 말은, 커피가 아니라 사람한테 하는 말이잖아요.")
    S.line(text="그녀가 고개를 숙여 컵을 닦았다. 조명 때문인지, 귀 끝이 조금 붉어 보였다.")
    S.goto("p_offer")

    S.label("p_taste_joke")
    S.line(who="한도연", e="base", text="팔고 있어요. 벌써 삼 년째.")
    S.line(who="나", text="아, 그럼 제가 산 거네요.")
    S.line(who="한도연", text="오늘은 서비스예요. 알바 지원자한테 돈 받으면, 그건 좀 아니죠.")
    S.line(text="농담인데도 그녀는 끝까지 진지한 얼굴로 말했다. 그게 더 웃겨서, 나는 컵을 입에 대고 웃음을 참았다.")
    S.goto("p_offer")

    S.label("p_offer")
    S.line(text="시계를 봤다. 새벽 한 시 오 분 전. 그녀가 앞치마 끈을 풀었다.")
    S.line(who="한도연", text="내일 아침 아홉 시에 오세요. 첫날은 커피 안 가르쳐요. 청소랑, 설거지랑, 손님 인사.")
    S.line(who="나", text="…뽑히는 건가요?")
    S.line(who="한도연", e="base", text="삼십 분 동안 여기 앉아 있었잖아요. 그거면 충분해요. 마감 직전에 남아 있는 사람은, 대개 기다릴 줄 아는 사람이거든요.")
    S.line(text="그녀가 오븐에서 무언가를 꺼냈다. 식빵이었다. 아직 따뜻했다.")
    S.line(who="한도연", text="마감하고 굽는 빵이에요. 내일 아침에 팔 건데, 하나는 가져가세요. 비 맞고 왔으니까.")
    S.line(text="봉투를 받았다. 손바닥에 온기가 오래 남았다.")
    S.line(bg="alley_dawn", rain=True, hide=True, text="계단을 내려와 골목을 나왔다. 비가 그치고 있었다.")
    S.line(text="가게 창 너머로 그녀가 아직 불을 끄지 않고 서 있는 게 보였다. 유리에 비친 불빛이, 달처럼 번져 있었다.")
    S.line(text="봉투 안의 빵은 아직 따뜻했다. 방학이 이렇게 시작될 줄은 몰랐다.")

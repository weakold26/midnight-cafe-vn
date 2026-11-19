# -*- coding: utf-8 -*-
"""마지막 주 — 남은 밤, 그리고 다섯 개의 결말"""


def build(S):
    S.line(ch="마지막 주 · 남은 밤", bg="cafe_day", bgm="jazz",
           text="팔월의 마지막 주. 방학이 일주일 남았다. 가게의 달력에는 아무 표시도 없었다.")
    S.line(text="도연 씨는 마지막 날에 대해 아무 말도 하지 않았다. 나도 물어보지 않았다. 물어보면 정해질 것 같아서.")
    S.line(show={"id": "doyeon", "expr": "base"}, who="한도연", text="오늘 원두가 새로 들어왔어요. 조금 비싼 거예요. 이번 주는 이걸로 나가요.")
    S.line(who="나", text="비싼 거면, 값도 올리세요.")
    S.line(who="한도연", e="surprised", text="…값을 왜 올려요.")
    S.line(who="나", text="좋은 걸 쓰면, 좋은 값에 팔아야 다음에도 좋은 걸 쓸 수 있잖아요. 사장님이 알려 주신 거예요. 원가 계산.")
    S.line(text="그녀가 잠깐 웃었다. 요즘은 이 웃음을 자주 본다. 처음엔 하루에 한 번이었는데, 지금은 하루에 여러 번이다.")
    S.line(who="한도연", e="base", text="…그거, 제가 그랬나요.")
    S.line(who="나", text="네. 첫날에, 물 한 잔 놓는 것부터.")
    S.line(text="그녀는 아무 말 없이 원두 봉투를 열었다. 향이 카운터를 넘어왔다. 이 냄새를 이제는 눈 감고도 알아볼 것 같았다.")

    S.line(bg="cafe_day", text="오후에 하린이 왔다. 낮에 오는 건 처음이었다. 손에 커다란 종이 봉투를 들고 있었다.")
    S.line(show2={"id": "harin", "expr": "base"}, who="유하린", text="…저, 이거. 다음 주 금요일이에요.")
    S.line(text="봉투 안에는 전시 초대장이 들어 있었다. 작은 글씨로, 골목의 소리 — 유하린.")
    S.line(who="유하린", e="blush", text="졸업 작품 전시요. 작은 갤러리인데, 그래도… 와 주실 수 있으면.")
    S.line(who="한도연", e="base", text="당연히 가야죠. 가게는 그날 일찍 닫을게요.")
    S.line(who="유하린", e="surprised", text="…가게를 닫으시게요?")
    S.line(who="한도연", text="손님이 가는 게 아니라, 우리가 가는 거니까. 그날은 제가 손님이에요.")
    S.line(text="하린이 초대장을 두 장 더 꺼냈다. 처음부터 세 장이었다. 그걸 보고 가슴이 조금 아팠다. 애초에 셋을 생각하고 만든 초대장이었다.")

    S.line(bg="counter_night", bgm="lofi", text="그날 밤, 마감을 하면서 도연 씨가 물었다. 아주 무심하게, 컵을 닦으면서.")
    S.line(show={"id": "doyeon", "expr": "base"}, who="한도연", text="방학 끝나면요. 뭐 해요?")
    S.line(who="나", text="…학교 가야죠.")
    S.line(who="한도연", text="그럼 여기 못 오네요. 낮에는.")
    S.line(text="컵을 닦는 소리가 잠깐 멈췄다. 다시 시작됐다. 그 사이에 아주 긴 시간이 있었다.")
    S.line(who="한도연", e="base", text="저녁에는 올 수 있겠네요. 새벽 한 시까지는 열어 두니까.")
    S.line(text="그건 초대인지, 그냥 영업시간 안내인지 알 수 없었다. 하지만 그녀가 그 말을 하기까지, 컵 하나를 세 번 닦았다는 건 알 수 있었다.")

    S.choice([
        {"t": "\"방학 끝나도 여기서 계속 일하고 싶어요.\"", "to": "e_stay", "eff": {"doyeon": 2}, "flag": "stay"},
        {"t": "\"금요일 전시회, 제가 먼저 가서 기다릴게요.\"", "to": "e_exhibit", "eff": {"harin": 2}, "flag": "exhibit"},
        {"t": "아무 말 없이 마지막 날까지 평소처럼 일한다.", "to": "e_silent", "eff": {"doyeon": 1, "harin": 1}},
    ])

    S.label("e_stay")
    S.line(who="나", text="방학 끝나도, 여기서 계속 일하고 싶어요.")
    S.line(who="한도연", e="surprised", text="…학기 중에도요?")
    S.line(who="나", text="네. 저녁이랑 주말이요. 대신 시험 기간엔 조금 빠질지도 몰라요.")
    S.line(text="그녀가 수건을 내려놓았다. 이번엔 컵을 닦지 않았다. 그냥 나를 봤다.")
    S.line(who="한도연", e="base", text="…그럼 제가 뭘 줄 수 있죠. 방학 때보다 적게 일할 텐데.")
    S.line(who="나", text="여기 있는 시간이요.")
    S.line(who="한도연", e="blush", text="그건 임금이 아니잖아요.")
    S.line(who="나", text="임금은 사장님이 정하시고요. 저는 나머지를 말한 거예요.")
    S.line(text="그녀가 아주 오래 나를 봤다. 조명이 어두워서 표정은 잘 보이지 않았는데, 귀는 보였다.")
    S.goto("e_last_night")

    S.label("e_exhibit")
    S.line(who="나", text="금요일, 제가 먼저 가서 기다릴게요. 가게 닫고 오시면, 제가 자리 맡아 둘게요.")
    S.line(who="한도연", e="base", text="…그건 좀 반칙인데. 자리를 맡아 두면, 안 갈 수가 없잖아요.")
    S.line(who="나", text="그러라고 맡아 두는 거예요.")
    S.line(text="하린이 그 말을 듣고 고개를 숙였다. 초대장을 만지작거리던 손이 멈췄다.")
    S.line(who="유하린", e="blush", text="…제가 만든 초대장인데, 저보다 먼저 가시면 어떡해요.")
    S.line(who="나", text="주최자는 늦게 도착하는 거래요. 대신 제가 제일 앞자리 앉아 있을게요.")
    S.line(who="유하린", text="…그럼 저, 거기서 실수할 것 같아요.")
    S.goto("e_last_night")

    S.label("e_silent")
    S.line(text="아무 말도 하지 않았다. 그녀도 더 묻지 않았다. 마감은 평소처럼 끝났고, 오븐에서 빵이 나왔다.")
    S.line(text="그날 밤의 침묵은 다른 날과 달랐다. 무언가를 피하는 침묵이 아니라, 무언가를 아껴 두는 침묵이었다.")
    S.line(who="한도연", e="base", text="…마지막 날엔, 뭐 먹고 싶어요. 제가 만들어 줄게요.")
    S.line(who="나", text="그거, 물어보시는 거예요?")
    S.line(who="한도연", text="네. 이번엔 제가 먼저 물어보는 거예요.")
    S.line(text="그 말에 이유를 물을 수 없었다. 물으면 대답이 작아질 것 같아서, 나는 그냥 생각해 두겠다고 했다.")
    S.goto("e_last_night")

    S.label("e_last_night")
    S.line(ch="마지막 밤 · 새벽 한 시", bg="counter_night", bgm="warm",
           text="팔월의 마지막 밤. 가게는 평소처럼 열두 시에 손님을 다 보내고, 한 시에 마감 종을 울렸다.")
    S.line(show={"id": "doyeon", "expr": "base"}, show2={"id": "harin", "expr": "base"},
           text="하린은 그날도 왔다. 마지막이라고 해서 특별히 다른 건 없었다. 그게 좋았다.")
    S.line(who="유하린", e="base", text="…오늘은 제가 마지막으로 시킬게요. 새벽 한 시 라떼요.")
    S.line(who="한도연", text="네. 제가 내릴게요. 오늘은 사장이 아니라, 바리스타니까.")
    S.line(text="도연 씨가 원두를 갈았다. 그 소리가 가게 안을 가득 채웠다. 나는 그 앞에서, 마지막 잔을 기다렸다.")
    S.line(text="세 잔이 카운터 위에 놓였다. 셋 다 같은 잔이었다. 크림 위에 반달이 하나씩.")
    S.line(show=None, who="한도연", text="이제, 진짜 마지막이네요.")
    S.line(text="그녀가 앞치마 끈을 풀었다. 하린은 스케치북을 덮었다. 나는 컵을 두 손으로 감쌌다. 아직 따뜻했다.")
    S.line(text="무언가 말해야 한다는 걸 알았다. 그런데 무엇을 말해야 하는지, 이 스무 밤 동안 한 번도 정하지 못했다.")

    S.choice([
        {"t": "도연 씨에게, 마감 후의 이 시간이 좋았다고 말한다.", "to": "end_pick_doyeon", "flag": "end_doyeon"},
        {"t": "하린에게, 이어폰 한쪽을 다시 빌려 달라고 한다.", "to": "end_pick_harin", "flag": "end_harin"},
        {"t": "두 사람에게, 셋이서 여기 계속 있고 싶다고 말한다.", "to": "end_pick_both", "flag": "end_both"},
    ])

    # ---------------- 엔딩 분기 ----------------
    S.label("end_pick_both")
    S.line(who="나", text="저, 다음 학기에도 여기 올게요. 대신 조건이 하나 있어요.")
    S.line(who="한도연", e="surprised", text="…조건이요?")
    S.line(who="나", text="하린 씨도 같이요. 마감 후에, 셋이서.")
    S.line(who="유하린", e="blush", text="…저는 손님이잖아요.")
    S.line(who="나", text="손님도 마감 후엔 앉아 있어도 되잖아요. 사장님이 그랬어요. 마감 후엔 우리가 손님이라고.")
    S.line(text="도연 씨가 잠깐 웃고, 고개를 저었다. 그리고 아주 작게 말했다. 좋아요, 그럼.")
    S.goto("end_route")

    S.label("end_pick_doyeon")
    S.line(who="나", text="사장님. 저, 마감 후의 이 시간이 좋았어요. 삼 년 동안 혼자였다는 게, 계속 마음에 걸렸고요.")
    S.line(who="한도연", e="surprised", text="…그건, 제가 혼자서 정한 거예요.")
    S.line(who="나", text="이제 혼자 정하지 않으셔도 되잖아요.")
    S.line(text="그녀가 아무 말도 하지 않았다. 하린이 조용히 일어나, 자기 잔을 들고 창가 자리로 갔다. 셋 중 누구도 그걸 이상하게 생각하지 않았다.")
    S.goto("end_route")

    S.label("end_pick_harin")
    S.line(who="나", text="하린 씨. 이어폰, 한쪽만 다시 빌려 줄래요?")
    S.line(who="유하린", e="surprised", text="…지금요?")
    S.line(who="나", text="네. 마지막이니까, 끝까지 들어 보고 싶어서요.")
    S.line(text="하린이 이어폰을 꺼냈다. 한쪽을 내게, 한쪽을 자기 귀에. 줄이 두 사람 사이에서 아주 짧게 팽팽해졌다.")
    S.line(text="도연 씨가 그걸 보고 조용히 카운터를 정리했다. 등을 돌린 채로, 아주 작게 웃는 소리가 났다.")
    S.goto("end_route")

    S.label("end_route")
    S.branch([
        ({"flag": "end_both", "affMin": {"doyeon": 7, "harin": 7}}, "end_both_qual"),
        ({"flag": "end_both"}, "end_both_plain"),
        ({"flag": "end_doyeon"}, "end_doyeon_check"),
        ({"flag": "end_harin"}, "end_harin_check"),
        (None, "end_tie"),
    ])

    S.label("end_both_plain")
    S.line(text="셋이서 마지막 잔을 비웠다. 그런데 그 잔들은, 아직 아무것도 정하지 못한 채로 비어 있었다.")
    S.goto("end_tie")

    S.label("end_doyeon_check")
    S.branch([
        ({"affMin": {"doyeon": 8}}, "end_doyeon_happy"),
        (None, "end_doyeon_normal"),
    ])

    S.label("end_harin_check")
    S.branch([
        ({"affMin": {"harin": 8}}, "end_harin_happy"),
        (None, "end_harin_normal"),
    ])

    S.label("end_tie")
    S.branch([
        ({"affMin": {"doyeon": 5}, "affMax": {}}, "end_doyeon_normal"),
        (None, "end_harin_normal"),
    ])

    # ---------------- 1. 도연 해피 ----------------
    S.label("end_both_qual")
    S.line(bg="alley_dawn", bgm="warm", hide=True,
           text="새벽 두 시. 셋이 문을 나왔다. 골목에는 비가 그친 자국이 남아 있었고, 물웅덩이가 가로등을 하나씩 담고 있었다.")
    S.line(show={"id": "doyeon", "expr": "base"}, show2={"id": "harin", "expr": "base"}, who="한도연",
           text="그럼 다음 주부터, 다시 월요일이네요. 세 명이서.")
    S.line(who="유하린", e="base", text="저는 금요일이 좋아요. 금요일 밤이 제일 길어서요.")
    S.line(who="나", text="그럼 마감은 매일, 셋이서 하는 걸로 해요.")
    S.line(who="한도연", e="surprised", text="…매일요?")
    S.line(who="나", text="네. 한 명은 빵을 굽고, 한 명은 소리를 듣고, 한 명은 커피를 내리고.")
    S.line(who="유하린", e="blush", text="…저는 소리를 듣는 사람이에요?")
    S.line(who="나", text="하린 씨는 이 가게의 소리를 맡은 사람이죠.")
    S.line(text="도연 씨가 팔짱을 낀 채로 웃었다. 그 웃음이 골목 끝까지 갔다가 돌아오는 것 같았다.")
    S.line(who="한도연", e="base", text="삼 년 전에 이 가게를 인수할 때, 간판을 바꿀까 고민했어요. 이름이 좀 슬프다고 생각했거든요. 달의 뒷면은 아무도 못 보니까.")
    S.line(who="한도연", text="근데 오늘은, 이름을 바꾸지 않기로 했어요. 이제는 봐 주는 사람이 셋이니까.")
    S.line(bg="counter_night", hide=True,
           text="그다음 주 월요일, 가게 메뉴판에는 세 개의 새 이름이 붙었다. 달의 뒷면 라떼, 새벽 한 시 라떼, 보름달 크림 라떼.")
    S.line(text="메뉴판 맨 아래에는 아주 작은 글씨가 있었다. 없는 메뉴는 물어보세요. 이름은, 시키는 사람이 정합니다.")
    S.line(text="그리고 마감 후의 가게에는, 이제 불이 세 개 켜진다. 하나는 오븐, 하나는 턴테이블, 하나는 창가 자리.")
    S.line(ending="true_end", text="우리 셋의 마지막 주문은, 언제나 같은 것이었다. 서로의 잔을 한 번씩 바꿔 마시는 것.")

    # ---------------- 2. 도연 해피 ----------------
    S.label("end_doyeon_happy")
    S.line(bg="counter_night", bgm="warm", text="새벽 한 시 십 분. 하린이 먼저 나갔다. 문이 닫히고, 가게 안에는 우리 둘만 남았다.")
    S.line(show={"id": "doyeon", "expr": "base"}, who="한도연", text="…방학 끝나면요. 낮에는 못 오죠.")
    S.line(who="나", text="네. 대신 저녁에는 올게요. 매일은 아니어도, 올 수 있는 날은.")
    S.line(who="한도연", e="base", text="그럼 그날은, 마감을 조금 일찍 해도 되나요.")
    S.line(who="나", text="왜요?")
    S.line(who="한도연", e="blush", text="…같이 걷고 싶어서요. 이 골목을. 삼 년 동안 혼자 걸었거든요.")
    S.line(text="대답 대신 우산을 들었다. 비는 오지 않았는데, 우산을 들고 나가면 두 사람이 조금 가까워진다는 걸 이 스무 밤 동안 배웠다.")
    S.line(bg="alley_dawn", text="계단을 내려와 골목을 걸었다. 그녀가 내 팔에 손을 걸었다. 아주 가볍게, 놓칠까 봐 조금 세게.")
    S.line(who="한도연", e="base", text="저, 하나만 물어볼게요. 계속 궁금했던 건데.")
    S.line(who="나", text="네.")
    S.line(who="한도연", text="첫날에 왜 하필 그 시간에 왔어요? 마감 삼십 분 전에, 비를 맞고.")
    S.line(who="나", text="그날 다른 데를 다 떨어지고, 마지막으로 온 거였어요. 여기까지 오는 데 사십 분 걸렸고, 도착했을 때 알바를 구하는 마음이 아니었어요.")
    S.line(who="한도연", e="surprised", text="그럼 뭐였는데요.")
    S.line(who="나", text="그냥, 불이 켜져 있어서요. 골목에서 저 불빛만 보였거든요.")
    S.line(text="그녀가 걸음을 멈췄다. 그리고 나를 봤다. 가로등이 그 얼굴을 반만 비추고 있었다.")
    S.line(who="한도연", e="blush", text="…그거, 제가 제일 듣고 싶었던 말이에요. 삼 년 동안.")
    S.line(bg="counter_night", hide=True,
           text="다음 날, 가게 벽에 걸린 이름 지워진 LP 옆에 작은 명패가 붙었다. 손글씨로 이렇게 적혀 있었다. 새벽 한 시, 2026.")
    S.line(text="이름을 다시 붙인 건 그녀였다. 그리고 그날부터 이 가게는, 새벽 한 시에만 문을 여는 가게가 아니라, 새벽 한 시를 기다리는 가게가 되었다.")
    S.line(ending="doyeon_happy", text="마감 종이 울려도, 우리는 아직 문을 닫지 않는다.")

    # ---------------- 3. 도연 노멀 ----------------
    S.label("end_doyeon_normal")
    S.line(bg="counter_night", bgm="lofi", text="마지막 잔을 다 마셨다. 하린이 먼저 일어나 인사를 했고, 도연 씨가 문까지 나가 봐 줬다.")
    S.line(show={"id": "doyeon", "expr": "base"}, who="한도연", text="…마지막 인사는 안 해요?")
    S.line(who="나", text="아, 네. 잘 지내세요. 사장님.")
    S.line(who="한도연", e="surprised", text="…사장님.")
    S.line(text="그 호칭이 그날따라 낯설었다. 스무 밤 동안 백 번도 더 했던 말인데, 마지막이라고 생각하니 다르게 들렸다.")
    S.line(who="한도연", e="base", text="네. 잘 지내세요. 방학 끝나면, 학교에서 열심히 하고.")
    S.line(bg="alley_dawn", text="문을 나와 계단을 내려갔다. 뒤에서 문이 닫히는 소리가 났다. 그리고 잠기는 소리.")
    S.line(text="몇 걸음 걷다가 뒤돌아봤다. 가게 불은 아직 꺼지지 않았다. 유리에 비친 불빛이, 달처럼 번져 있었다. 첫날과 똑같이.")
    S.line(bg="cafe_day", bgm="jazz", text="개강 첫 주. 나는 저녁 일곱 시에 골목으로 갔다. 문을 열자 종이 울렸고, 그녀가 고개를 들었다.")
    S.line(show={"id": "doyeon", "expr": "surprised"}, who="한도연", text="…어. 왔네요.")
    S.line(who="나", text="손님으로 왔어요. 오늘의 커피 한 잔이요.")
    S.line(text="그녀가 잔을 내렸다. 그리고 컵 옆에 작은 봉투를 하나 놓았다. 원두였다. 봉투에는 내 이름이 적혀 있었다. 이름을 묻지 않는 가게인데, 내 이름은 알고 있었던 것이다.")
    S.line(who="한도연", e="base", text="다음 계절 원두예요. 이번 주에 들어왔어요. 마셔 보고, 이상하면 말해요.")
    S.line(text="나는 그 봉투를 들고 창가 자리에 앉았다. 마감은 아직 네 시간 남아 있었다.")
    S.line(ending="doyeon_normal", text="그날부터 나는 매주 금요일의 손님이 되었다. 마감 후의 시간은 아니었지만, 그녀가 불을 켜 두는 시간 안에 있었다.")

    # ---------------- 4. 하린 해피 ----------------
    S.label("end_harin_happy")
    S.line(bg="counter_night", bgm="warm", text="이어폰 줄이 두 사람 사이에서 팽팽했다. 음악이 시작됐다. 이번엔 가게 소리가 아니었다.")
    S.line(show2={"id": "harin", "expr": "base"}, who="유하린", text="…이건, 제가 만든 거예요. 어제 밤에 완성했어요.")
    S.line(who="나", text="제목은요?")
    S.line(who="유하린", e="blush", text="…아직 없어요. 이름은, 처음 듣는 사람이 정하는 거라고 했잖아요.")
    S.line(text="나는 눈을 감고 끝까지 들었다. 곡의 중간에, 아주 작은 소리가 하나 섞여 있었다. 누군가 계단을 내려오는 발소리. 내 발소리였다.")
    S.line(who="나", text="…이거, 제 발소리잖아요.")
    S.line(who="유하린", e="surprised", text="들렸어요?")
    S.line(who="나", text="네. 열흘 전 새벽에, 골목 끝까지 같이 걸었을 때요.")
    S.line(who="유하린", e="blush", text="…그날 녹음한 거예요. 버릴까 했는데, 계속 마음에 남아서.")
    S.line(text="도연 씨가 카운터에서 조용히 말했다. 그 소리는, 우리 가게에 있어야 할 소리예요.")
    S.line(show={"id": "doyeon", "expr": "base"}, who="한도연", text="제목은 제가 정할게요. 이 가게에서 처음 만든 곡이니까, 이건 사장 권한이에요.")
    S.line(who="유하린", e="surprised", text="…뭐라고 하실 건데요.")
    S.line(who="한도연", text="새벽 한 시. 그리고 부제는, 이어폰 한쪽씩.")
    S.line(bg="cafe_day", hide2=True,
           text="금요일, 전시회는 작은 갤러리에서 열렸다. 입구에 곡이 흘러나오고 있었고, 벽에는 골목의 사진과 채집한 소리의 파형이 붙어 있었다.")
    S.line(bg="cafe_day", show2={"id": "harin", "expr": "blush"}, text="하린이 사람들 사이에 서서, 아주 어색하게 인사를 하고 있었다. 눈이 마주치자, 그 자리에서 조금 웃었다.")
    S.line(who="유하린", text="…와 주셨어요.")
    S.line(who="나", text="제 발소리가 작품에 들어갔는데, 안 올 수가 있나요.")
    S.line(who="유하린", e="base", text="저, 이거 끝나면요. 매일 밤 다시 가도 돼요? 이제는 작품이 아니라, 그냥.")
    S.line(who="나", text="그럼요. 대신 이어폰은 계속 한쪽씩이에요.")
    S.line(text="그녀가 이어폰을 목에서 내려, 한쪽을 내 귀에 끼워 주었다. 전시장 소리와 곡이 반씩 섞였다. 그게 정확히 우리가 있던 자리였다.")
    S.line(ending="harin_happy", text="골목의 소리는 이제 두 사람이 함께 듣는다. 반은 밖에, 반은 안에.")

    # ---------------- 5. 하린 노멀 ----------------
    S.label("end_harin_normal")
    S.line(bg="counter_night", bgm="lofi", text="이어폰을 돌려주고, 잔을 비웠다. 하린은 아무 말도 하지 않고 가방을 쌌다.")
    S.line(show2={"id": "harin", "expr": "base"}, who="유하린", text="…오늘 정말 마지막이네요.")
    S.line(who="나", text="네. 금요일에 전시회에서 봐요.")
    S.line(who="유하린", e="blush", text="…네. 와 주세요. 꼭.")
    S.line(text="그녀가 계단을 내려갔다. 두 블록쯤 걸어가다가, 이번에도 뒤돌아봤다. 나는 이번엔 먼저 손을 흔들었다.")
    S.line(bg="cafe_day", hide2=True, text="금요일. 갤러리는 생각보다 작았고, 사람은 생각보다 많았다. 하린은 입구에서 초대장을 확인하고 있었다.")
    S.line(text="나는 그 앞에 섰다. 그녀가 고개를 들고, 아주 잠깐 멈췄다.")
    S.line(who="유하린", e="surprised", text="…성함이 어떻게 되세요?")
    S.line(text="농담이었다. 우리는 이름을 묻지 않는 가게에서 만났으니까. 나는 웃으면서, 처음 만난 사람처럼 이름을 말했다.")
    S.line(who="유하린", e="blush", text="…아. 네. 들어오세요.")
    S.line(text="작품은 벽 하나를 다 썼다. 골목의 소리. 스피커 앞에 서면, 두 달 동안의 밤이 순서대로 흘러나왔다.")
    S.line(text="그중 한 구간에, 내 발소리가 있었다. 작품 설명에는 이렇게 적혀 있었다. 이름을 묻지 않는 가게에서, 매일 같은 시간에 문을 열어 주던 사람.")
    S.line(text="나는 그 문장을 세 번 읽었다. 하린은 멀리서 다른 사람과 이야기하고 있었다. 이쪽을 보지는 않았다.")
    S.line(ending="harin_normal", text="그림의 뒷면은, 그린 사람만 본다. 나는 그 뒷면에 아주 조금 닿았던 사람으로 남았다.")

    # ---------------- (도연 노멀 중복 방지용 분기 아님) ----------------

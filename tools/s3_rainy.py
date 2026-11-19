# -*- coding: utf-8 -*-
"""일주일째 — 비, 창가 자리, 그리고 시그니처"""


def build(S):
    S.line(ch="일주일째 · 비", bg="cafe_rain", bgm="lofi", rain=True,
           text="일주일째 되는 날, 비가 왔다. 오후부터 조용히, 그치지 않고.")
    S.line(text="비 오는 날의 가게는 손님이 적다. 대신 소리가 많다. 창에 부딪히는 소리, 지붕을 타고 흐르는 소리, 컵이 접시에 닿는 소리.")
    S.line(show={"id": "doyeon", "expr": "base"}, who="한도연", text="비 오는 날은 커피가 두 배로 팔려요. 이유는 몰라요. 그냥 그렇더라고요.")
    S.line(who="나", text="오늘은 한 잔도 안 팔렸는데요.")
    S.line(who="한도연", e="base", text="그럼 오늘은 두 배가 아니라, 세 배가 될 거예요. 저녁에.")
    S.line(text="그녀 말이 맞았다. 저녁 여덟 시부터 사람이 들어오기 시작했다. 우산을 접어 문 옆에 세우고, 창가 자리를 먼저 본다.")
    S.line(who="한도연", text="창가 자리는 비 올 때만 인기 있어요. 사람들은 비를 보러 오는 거예요. 커피는 핑계고.")
    S.line(text="나는 그 말을 들으면서 물을 따랐다. 핑계. 그 단어가 마음에 남았다. 여기 오는 사람들은 다 무언가의 핑계를 가지고 오는 것 같았다.")

    S.line(bg="cafe_rain", text="열 시가 넘어 하린이 들어왔다. 우산이 없었다. 머리카락이 젖어 있었고, 스케치북을 카디건 안에 넣어 감싸고 있었다.")
    S.line(show2={"id": "harin", "expr": "surprised"}, who="유하린", text="…아, 안녕하세요.")
    S.line(who="나", text="우산은요?")
    S.line(who="유하린", e="base", text="버스에서 내렸는데, 갑자기 와서요. 골목까지 뛰었어요. 삼 분이면 되니까.")
    S.line(text="삼 분을 뛰어서 이렇게 젖을 수는 없다. 아마 더 멀리서부터 뛰어온 것 같았다.")
    S.line(who="한도연", e="base", text="수건 가져다줄래요? 안쪽 선반 두 번째 칸에 있어요.")
    S.line(text="수건을 가지러 가는 동안, 도연 씨가 하린에게 뭐라고 조용히 말했다. 하린이 고개를 끄덕였다.")

    S.choice([
        {"t": "수건과 함께 따뜻한 차를 내려 준다.", "to": "r_rain_harin", "eff": {"harin": 2}},
        {"t": "도연 씨를 도와 젖은 창가 자리를 정리한다.", "to": "r_rain_doyeon", "eff": {"doyeon": 2}},
        {"t": "두 사람 몫으로 수건을 두 장 가져다 놓는다.", "to": "r_rain_both", "eff": {"harin": 1, "doyeon": 1}},
    ])

    S.label("r_rain_harin")
    S.line(text="수건을 그녀의 어깨에 걸쳐 주고, 따뜻한 캐모마일을 내렸다. 메뉴에 없는 차였다. 도연 씨가 자기 몫으로 두는 차.")
    S.line(who="유하린", e="blush", text="…이거, 메뉴에 없는데요.")
    S.line(who="나", text="네. 사장님 거예요. 대신 오늘은 제가 허락받았어요.")
    S.line(who="유하린", text="…그런 거 물어봤어요?")
    S.line(who="나", text="네. '비 맞은 손님한테 줄 건데요' 했더니, 잠깐 웃고 가져가라고 하시더라고요.")
    S.line(text="하린이 컵을 두 손으로 감쌌다. 젖은 머리카락이 아직 뺨에 붙어 있었다.")
    S.line(who="유하린", e="base", text="…저, 이런 거 처음이에요. 가게에서 뭘 서비스로 받아 본 적이 없어서.")
    S.line(who="나", text="저도 처음 해 봐요. 주는 쪽은.")
    S.line(who="유하린", e="blush", text="…그럼 우리 둘 다 처음이네요.")
    S.line(text="그 말이 끝나고, 그녀가 아주 작게 웃었다. 창에 비가 부딪히는 소리가 잠깐 커졌다가 작아졌다.")
    S.goto("r_signature")

    S.label("r_rain_doyeon")
    S.line(text="창가 자리에서 손님이 나가자, 물이 잔뜩 묻어 있었다. 도연 씨가 행주를 들고 왔다.")
    S.line(who="나", text="제가 할게요.")
    S.line(who="한도연", text="같이 해요. 창은 위에서 아래로. 물은 아래에서 위로 닦으면 다시 묻어요.")
    S.line(text="둘이 창을 닦았다. 어깨가 자꾸 부딪혔다. 유리에 비친 우리가, 이상하게 가까워 보였다.")
    S.line(who="한도연", e="base", text="비 오는 날은 이 창이 제일 힘들어요. 손님이 다 가고 나면, 여기만 남아서 계속 비를 맞거든요.")
    S.line(who="나", text="창이요?")
    S.line(who="한도연", text="네. 가게는 다 닦였는데, 창만 아직 비가 오는 것 같아서요. 그게 좀 억울하죠.")
    S.line(text="그녀가 마지막 물기를 닦고, 잠깐 창밖을 봤다. 유리에 비친 그녀의 얼굴이, 바깥의 불빛과 겹쳐 있었다.")
    S.line(who="한도연", e="base", text="…이제 괜찮네요. 누가 같이 닦아 주니까, 빨리 끝나네요.")
    S.goto("r_signature")

    S.label("r_rain_both")
    S.line(text="수건을 두 장 가져다, 하나는 하린에게, 하나는 도연 씨 손에 쥐여 줬다.")
    S.line(who="한도연", e="surprised", text="…저는 안 젖었는데요.")
    S.line(who="나", text="창문 닦다가 젖으실 것 같아서요. 비 오는 날은 창이 제일 힘들다고 하셨잖아요.")
    S.line(text="도연 씨가 수건을 한참 내려다봤다. 그리고 조용히 앞치마 주머니에 넣었다.")
    S.line(who="한도연", e="base", text="…그건 좀 반칙인데.")
    S.line(who="나", text="뭐가요?")
    S.line(who="한도연", text="아무것도 아니에요. 하린 씨, 차 마실래요?")
    S.line(text="하린이 고개를 끄덕였다. 두 사람이 동시에 나를 봤다. 그 시선이 부담스럽지 않아서, 조금 이상했다.")
    S.goto("r_signature")

    S.label("r_signature")
    S.line(bg="cafe_rain", text="하린은 늘 '아무거나'를 시켰다. 두 달 동안, 매일. 도연 씨가 그 이유를 알려 줬을 때부터, 나는 그 주문이 조금 슬펐다.")
    S.line(text="그래서 만들었다. 메뉴에 없는 것. 오늘 원두로 내린 라떼 위에, 크림을 반달 모양으로 얹은 것.")
    S.line(show2={"id": "harin", "expr": "surprised"}, who="나", text="오늘은 아무거나 말고, 이거 드셔 보세요.")
    S.line(who="유하린", text="…이게 뭐예요?")
    S.line(who="나", text="그건 정해야 해요. 제가 만들었는데, 이름이 없어서.")
    S.line(who="유하린", e="surprised", text="제가요?")
    S.line(who="나", text="네. 처음 시키는 사람이 이름을 정하는 게 맞잖아요.")
    S.line(text="하린이 컵을 내려다봤다. 크림 위의 반달이 아직 천천히 흘러내리고 있었다.")

    S.choice([
        {"t": "\"달의 뒷면 라떼\"는 어때요?", "to": "r_name_moon", "eff": {"harin": 2}, "flag": "sig_moon"},
        {"t": "\"새벽 한 시 라떼\"는 어때요?", "to": "r_name_one", "eff": {"harin": 2}, "flag": "sig_one"},
        {"t": "\"보름달 크림 라떼\"는 어때요?", "to": "r_name_full", "eff": {"harin": 1}},
    ])

    S.label("r_name_moon")
    S.line(who="유하린", e="base", text="…달의 뒷면.")
    S.line(who="나", text="여기 이름이잖아요. 그리고 달의 뒷면은 아무도 못 보니까, 이름을 붙이는 사람만 볼 수 있는 거죠.")
    S.line(text="하린이 아주 오래 나를 봤다. 그 시선을 피하지 않았다. 피하면 뭔가 틀리는 것 같았다.")
    S.line(who="유하린", e="blush", text="…그거, 좋아요. 좀 반칙인데.")
    S.line(who="나", text="오늘 반칙이라는 말, 두 번째예요.")
    S.line(who="유하린", text="…그건 제가 할 말이었는데.")
    S.goto("r_after_name")

    S.label("r_name_one")
    S.line(who="유하린", e="base", text="새벽 한 시. 마감 시간이잖아요.")
    S.line(who="나", text="네. 이 가게에서 제일 조용한 시간이에요. 그때 마시는 커피라서.")
    S.line(who="유하린", e="blush", text="…저는 그 시간에 항상 여기 있었는데. 한 번도 조용하다고 생각 안 했어요.")
    S.line(who="나", text="그럼 오늘부터 생각하시면 되죠.")
    S.line(text="하린이 컵을 들고 한 모금 마셨다. 크림이 윗입술에 묻었다. 그녀는 그걸 모른 채로 창밖을 봤다.")
    S.line(who="유하린", text="…이름, 마음에 들어요. 새벽 한 시 라떼. 제가 정한 거 맞죠?")
    S.goto("r_after_name")

    S.label("r_name_full")
    S.line(who="유하린", e="base", text="보름달… 크림이 반달이라서요?")
    S.line(who="나", text="네. 반만 남았으니까. 나머지 반은 마시는 사람 몫이고요.")
    S.line(who="유하린", e="blush", text="…그럼 마시면 보름달이 되는 거네요.")
    S.line(who="나", text="그렇네요. 그건 생각 못 했어요.")
    S.line(text="그녀가 컵을 들어 한 모금 마셨다. 그리고 크림이 사라진 자리를 한참 내려다봤다.")
    S.line(who="유하린", text="…아직 반달이에요. 조금만 남겨야겠다.")
    S.goto("r_after_name")

    S.label("r_after_name")
    S.line(bg="cafe_rain", text="그날부터 하린은 '아무거나'를 시키지 않았다. 대신 이렇게 말했다. 새벽 한 시 라떼, 혹은 달의 뒷면 라떼, 혹은 보름달 크림 라떼.")
    S.line(text="도연 씨는 그걸 보고 아무 말도 하지 않았다. 다만 메뉴판 구석에 작은 글씨로 한 줄을 추가했다. 없는 메뉴는 물어보세요.")
    S.line(show={"id": "doyeon", "expr": "base"}, who="한도연", text="이거, 정식 메뉴로 올릴까요?")
    S.line(who="나", text="…제가 만든 건데요.")
    S.line(who="한도연", e="base", text="그런 건 상관없어요. 손님이 이름을 붙였으면, 그건 이미 이 가게 메뉴예요.")
    S.line(who="한도연", text="대신 원가 계산은 내가 할게요. 그 크림, 재료가 만만치 않죠.")
    S.line(text="그녀는 알았다. 내가 크림을 두 번 다시 만든 걸, 아무도 못 봤는데.")

    S.line(bg="cafe_rain", bgm="lofi", text="마감 전, 하린이 이어폰을 꺼냈다. 한쪽을 나에게 건넸다.")
    S.line(show2={"id": "harin", "expr": "base"}, who="유하린", text="…들어볼래요? 오늘 녹음한 거예요.")
    S.line(who="나", text="제가요?")
    S.line(who="유하린", e="blush", text="…아, 싫으면 안 들어도 돼요.")
    S.line(text="이어폰 줄이 테이블 위로 늘어져 있었다. 그 한쪽이, 지금 이 가게에서 제일 무거운 물건처럼 보였다.")

    S.choice([
        {"t": "이어폰 한쪽을 받아 귀에 끼운다.", "to": "r_ear_take", "eff": {"harin": 2}, "flag": "earphone"},
        {"t": "\"여기서 스피커로 틀어 볼래요? 사장님도 들으시게요.\"", "to": "r_ear_speaker", "eff": {"harin": 1, "doyeon": 1}},
        {"t": "\"지금은 마감 준비 중이라, 다음에 들을게요.\"", "to": "r_ear_later", "eff": {"harin": 0}},
    ])

    S.label("r_ear_take")
    S.line(text="이어폰을 받아 끼웠다. 바깥 소리가 절반으로 줄었다. 비 소리, 컵 소리, 그리고 그 사이로 아주 작은 발소리.")
    S.line(text="그 곡에는 가게 소리가 들어 있었다. 의자 끄는 소리, 종소리, 누군가 물을 따르는 소리. 그 위에 낮게 깔린 피아노.")
    S.line(who="나", text="…이거, 우리 가게잖아요.")
    S.line(who="유하린", e="base", text="네. 두 달 동안 녹음했어요. 매일 조금씩.")
    S.line(who="나", text="왜요?")
    S.line(who="유하린", e="blush", text="…졸업 작품이요. 골목의 소리로 곡을 만드는 거. 근데 막상 하다 보니까, 가게 소리가 제일 좋아서.")
    S.line(text="그녀가 이어폰 줄을 손가락으로 감았다 풀었다 했다. 이어폰 한쪽은 아직 내 귀에 있었다.")
    S.line(who="유하린", text="…한쪽만 들으면, 반은 밖에 있어야 하잖아요. 그게 좋아요. 혼자 듣는 것보다.")
    S.goto("r_end")

    S.label("r_ear_speaker")
    S.line(who="나", text="사장님도 들으시게, 스피커로 틀어 볼래요?")
    S.line(who="유하린", e="surprised", text="…그건 좀 부끄러운데요.")
    S.line(show={"id": "doyeon", "expr": "base"}, who="한도연", text="저는 들어보고 싶은데요. 이 가게 소리가 어떻게 들리는지.")
    S.line(text="하린이 잠깐 망설이다가, 케이블을 꽂았다. 가게 안에 아주 작은 소리가 흘렀다. 종소리, 물소리, 의자 소리.")
    S.line(who="한도연", e="base", text="…이거, 우리 가게 맞네요. 저 종소리가 이렇게 들리는 줄은 몰랐어요. 안에서는 그냥 소리인데.")
    S.line(who="유하린", e="blush", text="…밖에서는 다르게 들려요. 골목이 소리를 한 번 감싸거든요.")
    S.line(text="도연 씨가 눈을 감고 그 소리를 끝까지 들었다. 하린은 그동안 테이블만 봤다.")
    S.goto("r_end")

    S.label("r_ear_later")
    S.line(who="나", text="지금은 마감 준비 중이라, 다음에 들을게요. 대신 그때 꼭 들려주세요.")
    S.line(who="유하린", e="base", text="…네. 다음에요.")
    S.line(text="그녀가 이어폰을 천천히 감았다. 표정이 나빠지지는 않았는데, 뭔가 접힌 것 같았다.")
    S.line(text="마감을 하면서, 나는 그 이어폰이 계속 신경 쓰였다. 다음에. 그 말이 다음을 만들어 주지는 않는다는 걸, 그날 밤에 알았다.")
    S.goto("r_end")

    S.label("r_end")
    S.line(bg="alley_dawn", rain=False, text="비가 그쳤다. 새벽 한 시 반, 셋이 함께 문을 나왔다.")
    S.line(show={"id": "doyeon", "expr": "base"}, show2={"id": "harin", "expr": "base"}, who="한도연", text="골목이 젖으면, 이 시간엔 조심해야 해요. 돌이 미끄러워요.")
    S.line(who="유하린", text="저는 저쪽이에요. 두 블록이요.")
    S.line(who="한도연", text="데려다줄까요?")
    S.line(who="유하린", e="blush", text="…아니요. 혼자 걸어도 돼요. 이 시간 골목이 좋아서.")
    S.line(text="하린이 먼저 계단을 내려갔다. 우산 대신 스케치북을 안고, 젖은 돌을 조심조심 밟으면서.")
    S.line(who="한도연", e="base", text="…저 애는요. 항상 저렇게 혼자 가요. 삼 개월 동안 한 번도 안 데려다줬어요.")
    S.line(who="나", text="왜요?")
    S.line(who="한도연", text="물어본 적이 없으니까요. 저 애는 거절을 잘 못 하니까, 물어보면 부담이 될까 봐.")
    S.line(text="그녀는 그렇게 말하고, 젖은 골목에서 담배도 피우지 않고 그냥 서 있었다. 손에 아무것도 없이.")
    S.line(who="한도연", text="…내일은 물어볼까요. 이제 두 명이니까, 한 명은 물어봐도 되잖아요.")

define config.name = "운명의 반쪽"
define gui.main_menu_background = "images/main_menu.png"

# 게임의 주요 캐릭터 정의
define m = Character("민수", color="#c8ffc8")
define y = Character("유나", color="#c8c8ff")

# 스토리 시작
label start:
    play music "audio/bgm.mp3"

    scene bg classroom
    with Dissolve(.5)
    "2024년 봄, 서울의 한 대학교..."

    "평범한 대학생활을 보내던 어느 날,"
    "내 인생은 180도 바뀌게 되었다."

    m "또 새로운 학기가 시작됐네..."

    "강의실에 들어서자 낯선 얼굴이 눈에 들어왔다."

    show yuna smile
    with Dissolve(.5)
    y "안녕하세요! 이번에 편입한 김유나라고 합니다."

    "그녀의 미소는 마치 봄날의 햇살 같았다."

    # Chapter 1: 만남
    m "안녕하세요. 저는 이민수입니다."

    y "혹시 수업 노트 좀 볼 수 있을까요? 지난 주 수업을 못 들어서..."

    menu:
        "노트를 보여준다":
            jump show_notes
        "거절한다":
            jump refuse_notes

label show_notes:
    m "그럼요, 여기 있습니다."

    y "정말 감사합니다! 덕분에 살았네요."

    "그렇게 우리의 인연은 시작되었다."
    jump chapter2

label refuse_notes:
    m "죄송하지만 제 필기가 좀 날림이라..."

    y "아, 네... 괜찮아요."

    "차가운 거절에도 그녀는 미소를 잃지 않았다."
    jump chapter2

# Chapter 2: 발전
label chapter2:
    scene bg cafe
    with Dissolve(.5)

    "그 후로 몇 주가 지났다."

    show yuna happy
    with Dissolve(.5)
    y "민수 씨는 정말 친절하시네요."
    
    m "별 말씀을요. 유나 씨야말로 항상 밝아서 좋아요."

    "우리는 자주 카페에서 만나 이야기를 나누었다."

    y "사실... 제가 말씀드리고 싶은 게 있어요."

    menu:
        "계속 듣는다":
            jump listen_story
        "자리를 피한다":
            jump avoid_story

label listen_story:
    y "저... 사실 제가 시한부 선고를 받았어요."

    m "뭐라고요...?"

    y "6개월... 그게 제게 남은 시간이에요."

    "갑작스러운 고백에 내 마음은 무너져 내렸다."
    jump chapter3

label avoid_story:
    "나는 그녀의 진지한 표정이 부담스러워 자리를 피했다."

    "하지만 그것이 내 인생의 가장 큰 후회가 될 줄은 몰랐다."
    jump chapter3

# Chapter 3: 위기
label chapter3:
    scene bg hospital
    with Dissolve(.5)

    "시간은 빠르게 흘러갔다."

    show yuna sick
    with Dissolve(.5)
    y "민수 씨... 죄송해요."

    m "무슨 말씀을..."

    y "제가 민수 씨를 속였어요."

    "그녀의 눈에서 눈물이 흘러내렸다."

    y "사실 제가 시한부 판정을 받은 게 아니라..."

    menu:
        "계속 듣는다":
            jump listen_truth
        "도망친다":
            jump run_away

label listen_truth:
    y "제가... 민수 씨의 쌍둥이 동생이에요."

    m "뭐... 라고요?"

    y "15년 전 그 사고로 헤어진..."

    "순간 머리를 강타당한 것 같았다."

    $ is_truth = True

    jump final_chapter

label run_away:
    "나는 그녀의 말을 더 듣지 못하고 병실을 뛰쳐나왔다."

    $ is_truth = False

    jump final_chapter

# Final Chapter: 진실
label final_chapter:
    scene black
    with Dissolve(.5)

    if is_truth:
        "15년 전, 한 가족이 교통사고를 당했다."

        "쌍둥이 남매는 서로 다른 보육원으로 보내졌고..."

        pause 1.0
        show yuna normal
        with Dissolve(.5)
        y "찾았어요, 오빠. 정말 오래 걸렸죠?"

        "기억이 하나둘 떠올랐다."
        "어린 시절의 기억들..."
        "그리고 그날의 사고..."
        
        m "유나야... 정말 너였구나..."
        
        y "이제 우리가 진짜 가족이 될 시간이에요."

        hide yuna
        with Dissolve(.5)

    "우리의 슬픈 사랑 이야기는 그렇게 끝이 났다."
    "하지만 새로운 시작이기도 했다."

    scene bg park
    with Dissolve(.5)
    # 엔딩 크레딧
    "The End"

    if is_truth:
        "우리가 찾은 것은 사랑이 아닌 잃어버린 가족이었다."
    else:
        "이제 곧 또 다른 사랑이 시작될 것이다."

    return
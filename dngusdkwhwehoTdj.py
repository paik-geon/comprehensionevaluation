import streamlit as st

# 키워드 사전
keywords = {
    "문장 1 - 과학": [
        "지구", "자전", "낮", "밤", "생태계", "기후", "회전", "속도", "영향", "생활", "방식",
        "환경", "변화", "지구의 자전", "주기", "태양", "날씨", "온도", "적도", "극지방",
        "계절", "열대", "대기", "생물", "지리", "우주", "별", "중력", "지구 자전", "환경 영향"
    ],
    "문장 2 - 역사": [
        "산업혁명", "기계화", "생산성", "경제", "노동", "부작용", "기술적", "변혁", "현대", "환경",
        "기반", "증가", "18세기", "발생", "혁명", "산업", "공장", "기계", "혁신", "자본주의",
        "기술", "경제 변화", "사회 변화", "도시화", "농업", "공업", "증기기관", "철도", "노동자", "분업"
    ],
    "문장 3 - 철학": [
        "행복", "목표", "일상", "만족", "삶", "의미", "중요", "진정한", "깨달음", "작은",
        "중요성", "평범한", "여정", "감정", "삶의 의미", "삶의 행복", "성공", "삶의 만족", "기쁨", "의식",
        "즐거움", "현재", "현재 순간", "긍정적", "소소한", "성찰", "평화", "소중함", "마음", "사랑"
    ],
}


# 이해도 계산 함수
def calculate_comprehension(user_input, selected_keywords):
    user_words = user_input.lower()  # 입력을 소문자로 변환
    matched_keywords = [word for word in selected_keywords if word in user_words]
    match_count = len(matched_keywords)

    # 키워드 매칭에 따른 점수 계산
    if match_count == 0:
        score = 0
    elif match_count <= 2:
        score = 30
    elif match_count <= 4:
        score = 50
    elif match_count <= 6:
        score = 70
    elif match_count <= 9:
        score = 85
    else:
        score = 100

    return score, matched_keywords


# 스트림릿 앱
st.title("RSVP 이해도 테스트")

# 문장 선택
st.sidebar.header("문장 선택")
sample_texts = {
    "문장 1 - 과학": "과학",
    "문장 2 - 역사": "역사",
    "문장 3 - 철학": "철학",
}
selected_text = st.sidebar.selectbox("시연에서 사용된 문장을 선택하세요:", list(sample_texts.keys()))

# 사용자 입력
st.write("RSVP 방식으로 문장을 읽으셨다면 이해한 내용을 아래에 작성해주세요!")
user_input = st.text_area("아래 박스에 문장에서 이해한 내용을 입력하세요")

# 평가
if st.button("평가하기"):
    if user_input.strip():
        selected_keywords = keywords[selected_text]
        score, matched_keywords = calculate_comprehension(user_input, selected_keywords)
        st.write(f"**이해도 점수**: {score:.2f}%")
        st.write(f"**일치하는 키워드**: {', '.join(matched_keywords) if matched_keywords else '없음'}")
    else:
        st.write("이해한 내용을 입력해주세요!")

# 선택된 문장 표시
st.sidebar.write("**선택된 문장:**")
st.sidebar.write(sample_texts[selected_text])


# 문장 1 (과학)
# 지구의 자전은 하루 동안 낮과 밤을 만들어냅니다. 이 과정은 인류의 생활 방식과 생태계에 중요한 영향을 미칩니다. 특히, 지구의 회전 속도는 기후 변화와도 밀접하게 연관되어 있습니다
#
# 문장 2 (역사)
# 산업혁명은 18세기에 시작된 기술적 변혁의 시기였습니다. 기계화를 통해 생산성이 급격히 증가하며, 현대 경제의 기반이 마련되었습니다. 그러나 노동 환경의 악화와 같은 부작용도 발생했습니다
#
# 문장 3 (철학)
# 행복은 특정 목표를 이루는 데서 오는 것이 아닙니다. 작은 일상 속에서 만족감을 느끼는 것이 중요합니다. 이를 통해 삶의 진정한 의미를 깨달을 수 있습니다
#

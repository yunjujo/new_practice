import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 궁합 분석", page_icon="❤️")

st.title("❤️ MBTI 유형별 궁합 확인")
st.write("나와 상대방의 MBTI를 선택하여 궁합을 확인해보세요!")

# 1. MBTI 목록 정의
mbti_list = [
    "ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# 2. 사용자 입력 (두 개의 선택 상자)
col1, col2 = st.columns(2)
with col1:
    my_mbti = st.selectbox("나의 MBTI", mbti_list)
with col2:
    your_mbti = st.selectbox("상대방의 MBTI", mbti_list)

# 3. 궁합 로직 (간단한 예시 버전)
# 실제 서비스에서는 모든 조합에 대한 결과값이 담긴 딕셔너리를 사용합니다.
st.divider()

if st.button("궁합 확인하기"):
    # 여기서는 예시로 랜덤하게 혹은 특정 조건으로 결과를 보여줍니다.
    # 실제 구현 시에는 mbti_compatibility_matrix 같은 데이터를 활용합니다.
    
    st.subheader(f"✨ {my_mbti} ❤️ {your_mbti} 결과")
    
    # 예시 결과값 배치
    score = 85 # 실제 로직에선 계산된 점수
    st.progress(score / 100)
    st.write(f"두 분의 궁합 점수는 **{score}점**입니다!")
    
    if score >= 90:
        st.success("💘 **천생연분!** 눈빛만 봐도 통하는 사이입니다.")
    elif score >= 70:
        st.info("😊 **좋은 관계!** 서로 배려한다면 아주 좋은 사이가 됩니다.")
    else:
        st.warning("🤔 **노력이 필요함!** 서로의 다름을 인정하는 자세가 중요해요.")

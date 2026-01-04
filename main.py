import streamlit as st

# 1. 페이지 설정 (웹 브라우저 탭에 표시될 이름과 아이콘)
st.set_page_config(
    page_title="2025 MBTI 분석 사이트",
    page_icon="📊",
    layout="wide"
)

# 2. 메인 타이틀과 설명
st.title("🚀 2025 MBTI 유형별 데이터 분석")
st.subheader("우리나라 사람들의 MBTI 분포는 어떨까요?")

st.markdown("""
---
이 사이트는 **2025년 최신 MBTI 데이터**를 바탕으로 제작되었습니다.
왼쪽의 **사이드바 메뉴**를 클릭하여 상세 분석 내용을 확인해보세요!

* **상위 10개 유형:** 가장 많은 비율을 차지하는 MBTI 확인
* **유형별 특징:** 각 MBTI의 성격과 장단점 분석
---
""")

# 3. 메인 화면에 시각적인 요소 추가 (이미지나 간단한 통계)
col1, col2 = st.columns(2)

with col1:
    st.info("💡 **데이터 출처**: 2025년 자체 설문조사 결과")
    st.metric(label="총 참여 인원", value="1,250명", delta="120명 증가")

with col2:
    st.success("✅ **업데이트 완료**: 2025년 1월 기준 데이터 반영")

# 4. 하단 강조 문구
st.warning("분석 결과는 재미로만 확인해 주세요!")

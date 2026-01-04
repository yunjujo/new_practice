import streamlit as st
import pandas as pd

# 페이지 제목 설정
st.set_page_config(page_title="국가별 MBTI 분석", page_icon="🌍")

st.title("🌍 국가별 MBTI 분포 현황")
st.write("전 세계 다양한 국가들의 주된 MBTI 유형을 확인해보세요.")

# 1. 가상의 국가별 데이터 생성 (실제 데이터를 여기에 입력하세요)
data = {
    "국가": ["대한민국", "미국", "일본", "독일", "브라질", "영국"],
    "주요 유형": ["ISTJ", "ENFP", "ISFJ", "INTJ", "ESFP", "ESTJ"],
    "비율 (%)": [14.7, 12.5, 13.2, 11.0, 15.1, 10.8],
    "특징": ["성실함과 질서", "자유와 창의성", "배려와 조화", "논리와 효율", "열정과 사교", "전통과 책임"]
}
df = pd.DataFrame(data)

# 2. 국가 선택 셀렉트박스
target_country = st.selectbox("궁금한 국가를 선택하세요:", df["국가"])

# 3. 선택한 국가의 데이터 보여주기
selected_row = df[df["국가"] == target_country].iloc[0]

col1, col2 = st.columns(2)
with col1:
    st.metric(label=f"{target_country}의 주요 유형", value=selected_row["주요 유형"])
with col2:
    st.metric(label="전체 비율", value=f"{selected_row['비율 (%)']}%")

st.info(f"💡 **{target_country}** 유형 특징: {selected_row['특징']}")

# 4. 전체 데이터 표 보여주기
st.divider()
st.subheader("📊 전체 국가별 데이터 확인")
st.dataframe(df, use_container_width=True) # 깔끔한 표 출력

# 5. 간단한 막대 그래프 추가
st.bar_chart(data=df, x="국가", y="비율 (%)")

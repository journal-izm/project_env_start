import streamlit as st
import pandas as pd

st.title("환경 세팅 테스트")
st.write("가상환경 및 라이브러리 연동 성공!")

# Pandas 데이터 테스트
df = pd.DataFrame({'열1': [1, 2, 3], '열2': [4, 5, 6]})
st.dataframe(df)

if st.button("테스트 버튼"):
    st.success("스트림릿이 정상적으로 작동합니다!")
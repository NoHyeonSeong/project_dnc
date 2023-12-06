# streamlit 라이브러리
# - Python으로 손쉽게 웹사이트를 생성할 수 있는 라이브러리
# - 기존에는 HTML,CSS, JS 등과 같은 기술을 공부해야 웹 사이트 구현 가능
# - Streamlit을 사용하면 위의 기술을 모르더라도 블럭 쌓듯이 손쉽게 구현 가능
# - 단, 단점은 우리가 원하는 디테일한 작업은 불가능

import streamlit as st

news_category = dict_news = {
    "society":    "사회",
    "politics":   "정치",
    "economic":   "경제",
    "foreign":    "경제",
    "culture":    "문화",
    "entertain":  "연예",
    "sports":     "스포츠",
    "digital":    "IT"
}
# streamlit run ./app.py

st.set_page_config(
    page_title= "뉴스 수집기"
    # page_icon="./impage/favicon_01.png"
)

st.title(":red[NEWS] COLLECTER")
st.text("DAUM 뉴스를 수집합니다.")

with st.form(key="form"):
    category = st.text_input("카테고리 입력").strip()
    subitted = st.form_submit_button("수집")
    if subitted:
        st.write(category)
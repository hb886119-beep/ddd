import streamlit as st

st.set_page_config(page_title="YouTube Data Tool", layout="wide")

st.title("🎬 YouTube Data Analyzer")
st.write("YouTube 링크를 넣으면 썸네일 / 댓글 / 영상 정보를 자동으로 분석합니다.")

st.markdown("""
### 📌 기능
- 🎥 영상 정보 확인
- 💬 댓글 수집
- 🖼️ 썸네일 추출
- 📺 채널 정보 확인

왼쪽 메뉴에서 기능을 선택하세요.
""")

import streamlit as st
from utils import get_video_id, get_video_details

st.title("🎬 Video Analyzer")

url = st.text_input("YouTube URL 입력")

if url:
    vid = get_video_id(url)
    data = get_video_details(vid)

    if data["items"]:
        v = data["items"][0]

        st.subheader(v["snippet"]["title"])
        st.image(v["snippet"]["thumbnails"]["high"]["url"])

        st.write("📄 Description")
        st.write(v["snippet"]["description"])

        stats = v["statistics"]
        col1, col2, col3 = st.columns(3)

        col1.metric("Views", stats.get("viewCount"))
        col2.metric("Likes", stats.get("likeCount"))
        col3.metric("Comments", stats.get("commentCount"))

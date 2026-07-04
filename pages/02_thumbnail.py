import streamlit as st
from utils import get_video_id, get_video_details

st.title("🖼️ Thumbnail Downloader")

url = st.text_input("YouTube URL 입력")

if url:
    vid = get_video_id(url)
    data = get_video_details(vid)

    t = data["items"][0]["snippet"]["thumbnails"]

    st.image(t["default"]["url"], caption="Default")
    st.image(t["medium"]["url"], caption="Medium")
    st.image(t["high"]["url"], caption="High")

    st.download_button("Download High Thumbnail", t["high"]["url"])

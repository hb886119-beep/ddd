import streamlit as st
import pandas as pd
from utils import get_video_id, get_comments

st.title("💬 Comments Explorer")

url = st.text_input("YouTube URL 입력")

if url:
    vid = get_video_id(url)
    data = get_comments(vid, 100)

    rows = []

    for item in data.get("items", []):
        c = item["snippet"]["topLevelComment"]["snippet"]
        rows.append([c["authorDisplayName"], c["textDisplay"], c["likeCount"]])

    df = pd.DataFrame(rows, columns=["Author", "Comment", "Likes"])

    st.dataframe(df)

    st.write("🔥 Most Liked Comments")
    st.dataframe(df.sort_values("Likes", ascending=False).head(10))

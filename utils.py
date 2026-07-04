from googleapiclient.discovery import build
import streamlit as st

API_KEY = st.secrets["YOUTUBE_API_KEY"]

youtube = build("youtube", "v3", developerKey=API_KEY)


def get_video_id(url: str):
    if "v=" in url:
        return url.split("v=")[-1].split("&")[0]
    return url


def get_video_details(video_id):
    request = youtube.videos().list(
        part="snippet,statistics",
        id=video_id
    )
    return request.execute()


def get_comments(video_id, max_results=20):
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=max_results,
        textFormat="plainText"
    )
    return request.execute()


def get_channel_details(channel_id):
    request = youtube.channels().list(
        part="snippet,statistics",
        id=channel_id
    )
    return request.execute()

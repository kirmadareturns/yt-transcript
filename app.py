import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi

st.set_page_config(page_title="YouTube Transcript Extractor", layout="centered")

st.title("🎬 YouTube Transcript Extractor")

url = st.text_input("Paste YouTube video link here:")

if st.button("Get Transcript"):
    if "v=" in url:
        video_id = url.split("v=")[1].split("&")[0]
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            text = " ".join([t["text"] for t in transcript])
            st.text_area("Transcript:", text, height=400)
        except Exception as e:
            st.error("❌ No transcript found or captions disabled.")
    else:
        st.warning("⚠️ Please enter a valid YouTube URL.")

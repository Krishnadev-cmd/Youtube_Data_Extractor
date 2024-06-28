import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
import os
import streamlit as st
import re
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt="""You are Yotube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here:  """
def extract_video_id(url):
    #Match common YouTube URL patterns
    patterns = [
    r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([a-zA-Z0-9_-]+)',  # Regular YouTube URL
    r'(?:https?://)?(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)',     # Embed URL
    r'(?:https?://)?(?:www\.)?youtube\.com/v/([a-zA-Z0-9_-]+)',         # /v/ URL
    r'(?:https?://)?youtu\.be/([a-zA-Z0-9_-]+)'                         # Shortened URL
    ]
    for pattern in patterns:
        match = re.match(pattern, url)
        if match:
            return match.group(1)
    raise ValueError(f"Invalid YouTube URL: {url}")

def get_text(video_id):   
    try:
        #video_id = extract_video_id(youtube_link)
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript
    except Exception as e:
        print(e)
        raise e

    
def generate_summary(transcript,prompt):
    model=genai.GenerativeModel("gemini-1.5-pro")
    response= model.generate_content(prompt+transcript_text)
    return response.text

st.title("Youtube Summary Generator")
youtube_url=st.text_input("Enter the Youtube URL")

if youtube_url:
    #youtube_link=youtube_url.split("=")[1]
    #print(youtube_link)
    id=extract_video_id(youtube_url)
    st.image(f"http://img.youtube.com/vi/{id}/0.jpg", use_column_width=True)

if st.button("Get Details"):
    transcript_text=get_text(id)
    if transcript_text:
        summary=generate_summary(transcript_text,prompt)
        st.markdown("##DETAILS##")
        st.write(summary)




    
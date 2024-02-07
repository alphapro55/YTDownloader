import streamlit as st
from pytube import YouTube
import os
from moviepy.editor import *

def download_audio(url):
    try:
        video = YouTube(url)
        audio_stream = video.streams.get_audio_only()
        audio_file = audio_stream.download()
        base, ext = os.path.splitext(audio_file)
        new_file = base + '.mp3'
        if os.path.exists(new_file):
            os.remove(new_file)
        os.rename(audio_file, new_file)
        return True, new_file  # Download was successful
    except Exception as e:
        return False, str(e)  # Download failed

def main():
    st.title("YouTube Audio Downloader")

    url = st.text_input("Enter the YouTube Video URL Here:")

    if st.button("Download Audio"):
        if url:
            with st.spinner('Downloading...'):
                success, filepath = download_audio(url)
                if success:
                    st.success("Downloaded successfully. Preparing file for download...")
                    with open(filepath, "rb") as file:
                        btn = st.download_button(
                            label="Download MP3",
                            data=file,
                            file_name=os.path.basename(filepath),
                            mime="audio/mp3"
                        )
                else:
                    st.error("An error occurred: {}".format(filepath))
        else:
            st.warning("Please enter a YouTube video URL.")

if __name__ == "__main__":
    main()
    

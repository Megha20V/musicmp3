import streamlit as st
import yt_dlp
import os

# Define default download location
DEFAULT_DOWNLOAD_DIR = os.path.join(os.path.expanduser("~"), "Downloads")

# Create the directory if it doesn't exist
if not os.path.exists(DEFAULT_DOWNLOAD_DIR):
    os.makedirs(DEFAULT_DOWNLOAD_DIR)

# Streamlit App Configuration
st.title("YouTube to MP3 Downloader")
st.write("Paste a YouTube URL or playlist below to download MP3 files.")

# Input field for YouTube URL
url = st.text_input("YouTube URL", placeholder="Enter YouTube video or playlist URL")

# Button to start download
if st.button("Download MP3"):
    if url:
        try:
            # Specify download options
            ydl_opts = {
                'format': 'mp3/bestaudio/best',  # Best available audio
                'outtmpl': os.path.join(DEFAULT_DOWNLOAD_DIR, '%(title)s.%(ext)s'),  # Save to default location
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                }]
            }

            # Download and convert using yt_dlp
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                st.info("Downloading and converting to MP3...")
                ydl.download([url])
                st.success(f"Download completed successfully! Files saved to {DEFAULT_DOWNLOAD_DIR}")

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid YouTube URL.")

st.write(f"Downloaded files will be saved to: `{DEFAULT_DOWNLOAD_DIR}`.")

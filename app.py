import streamlit as st
import instaloader

def download_instagram_reel(url):
    loader = instaloader.Instaloader()
    try:
        loader.download_post(url, target='#reels')
        st.success("Instagram reel downloaded successfully!")
    except Exception as e:
        st.error(f"An error occurred while downloading the Instagram reel: {str(e)}")


st.title("Instagram Reel Downloader")


url = st.text_input("Enter Instagram Reel URL")


if st.button("Download"):
    if url:
        download_instagram_reel(url)
    else:
        st.warning("Please enter a valid Instagram Reel URL.")

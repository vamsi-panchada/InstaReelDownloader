import streamlit as st

st.title('Instagram Reel Downloader')
st.text('This application is developed by vamsi panchada.\nIt allows you to download reels using reel share link.')

url = st.text_input('Enter url', help='Please paste url here')
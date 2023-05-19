import streamlit as st
import instaloader


st.title('Instagram Reel Downloader')
st.text('This application is developed by vamsi panchada.\nIt allows you to download reels using reel share link.')

url = st.text_input('Enter url', help='Please paste url here')

if url:
    if st.button('download'):
        loader = instaloader.Instaloader()
        # try:
        post = instaloader.Post.from_shortcode(loader.context, url)
        video_bytes = post.video_download_url().read()
            
        # except Exception as e:
        #     st.error(e)

        

# import streamlit as st
# import instaloader

# def download_instagram_reel(url):
#     loader = instaloader.Instaloader()
#     try:
#         post = instaloader.Post.from_shortcode(loader.context, url)
#         video_bytes = post.video_download_url().read()
#         return video_bytes
#     except Exception as e:
#         st.error(f"An error occurred while downloading the Instagram reel: {str(e)}")

# # Streamlit app code
# st.title("Instagram Reel Downloader")

# # Input field for the Instagram post URL
# url = st.text_input("Enter Instagram Reel URL")

# # Download button
# if st.button("Download"):
#     if url:
#         video_bytes = download_instagram_reel(url)
#         if video_bytes:
#             st.download_button(label="Click to Download", data=video_bytes, file_name="reel.mp4", mime="video/mp4")
#     else:
#         st.warning("Please enter a valid Instagram Reel URL.")

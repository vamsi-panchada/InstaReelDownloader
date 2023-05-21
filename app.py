# import streamlit as st
# import instaloader


# st.title('Instagram Reel Downloader')
# st.text('This application is developed by vamsi panchada.\nIt allows you to download reels using reel share link.')

# url = st.text_input('Enter url', help='Please paste url here')

# if url:
#     if st.button('download'):
#         loader = instaloader.Instaloader()
#         # try:
#         post = instaloader.Post.from_shortcode(loader.context, url)
#         video_bytes = post.video_download_url().read()
            
#         # except Exception as e:
#         #     st.error(e)

        

# # import streamlit as st
# # import instaloader

# # def download_instagram_reel(url):
# #     loader = instaloader.Instaloader()
# #     try:
# #         post = instaloader.Post.from_shortcode(loader.context, url)
# #         video_bytes = post.video_download_url().read()
# #         return video_bytes
# #     except Exception as e:
# #         st.error(f"An error occurred while downloading the Instagram reel: {str(e)}")

# # # Streamlit app code
# # st.title("Instagram Reel Downloader")

# # # Input field for the Instagram post URL
# # url = st.text_input("Enter Instagram Reel URL")

# # # Download button
# # if st.button("Download"):
# #     if url:
# #         video_bytes = download_instagram_reel(url)
# #         if video_bytes:
# #             st.download_button(label="Click to Download", data=video_bytes, file_name="reel.mp4", mime="video/mp4")
# #     else:
# #         st.warning("Please enter a valid Instagram Reel URL.")


import instaloader 
import re
import time
from pathlib import Path

loader = instaloader.Instaloader()

# link = 'https://www.instagram.com/reel/CsXr5MdAXPv'
link = 'https://www.instagram.com/reel/CqiHZssAh6O/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA=='

pattern = r"/reel/([^/?]+)"

match = re.search(pattern, link)

if match: 
    shortcode=match.group(1)
    try:
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        filePath = str(int(time.time()))
        loader.download_post(post, target=filePath)
        for file in Path(filePath).glob('*'):
            if not file.name.endswith('.mp4'):
                file.unlink()
        
    except Exception as e:
        print(e)

else:
    print('Invalid Link, Unable to extract reel short code in the provided link')
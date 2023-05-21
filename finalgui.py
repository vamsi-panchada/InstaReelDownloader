import streamlit as st
import instaloader
import re
import time
from pathlib import Path
import shutil
import os

st.title('Instagram reel downloader')
st.write('This application allows you to download reels.')
st.write('Developer : Vamsi Panchada')
st.write('Email : vamsipanchada@icloud.com')

st.write('© Vamsi Panchada')

url = st.text_input('paste your url here', help="paste instagram reel url.")

loader = instaloader.Instaloader()
pattern = r"/reel/([^/?]+)"

if url:
    match = re.search(pattern, url)
    if match:
        shortcode = match.group(1)
        print(shortcode)
        try:
            post = instaloader.Post.from_shortcode(loader.context, shortcode)
            filePath = str(int(time.time()))
            targetFile = ''
            loader.download_post(post, target=filePath)
            for file in Path(filePath).glob('*'):
                if not file.name.endswith('.mp4'):
                    file.unlink()
                else:
                    targetFile = filePath+'/'+file.name
            print(targetFile)
            with open(targetFile, "rb") as file:
                file_bytes = file.read()
            if file_bytes:
                st.download_button("Download File", file_bytes, file_name="reel.mp4")
            parent_dir = "."
            directories = next(os.walk(parent_dir))[1]
            for directory in directories:
                if filePath in directory:
                    folder_path = os.path.join(parent_dir, directory)
                    shutil.rmtree(folder_path)
                    print(f"Deleted folder: {folder_path}")
            
            st.write('Thank you for using our service.')

        
        except Exception as e:
            st.error(e)


    else:
        st.warning('Invalid url, Please try again with correct url.', icon="⚠️")

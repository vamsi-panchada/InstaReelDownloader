# # from instascrape import Reel
# # import time 

# # link = 'https://www.instagram.com/reel/CsXr5MdAXPv'
# # SESSIONID = "18614737527%3ApTLwFoXv5BZohu%3A4"
# # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43", "cookie":f'sessionid={SESSIONID};'}

# # google_reel=Reel(link)
# # google_reel.scrape(headers=headers)
# # google_reel.download(fp=f".\\reel{int(time.time())}.mp4")

# # from instascrape import Reel
# # import time

# # SESSIONID = "17f4c0258bf-db0f5c"

# # headers = {
# # 	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
# # 	AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 \
# # 	Safari/537.36 Edg/79.0.309.43",
# # 	"cookie": f'sessionid={SESSIONID};'
# # }

# # insta_reel = Reel(
# # 	'https://www.instagram.com/reel/CsXr5MdAXPv')

# # insta_reel.scrape(headers=headers)

# # insta_reel.download(fp=f".\\Desktop\\reel{int(time.time())}.mp4")

# # print('Reel downloaded successfully!')

# from instaloader import Instaloader, Post
# import re


# L = Instaloader()


# def linkdownload(link):
#     id_pattern = r"(/p/|/reel/)([a-zA-Z0-9_-]+)/"
#     match = re.search(id_pattern, link)

#     if not match:
#         print('match found')
#         # id = match.group(2)
#         post = Post.from_shortcode(L.context, 'CsXr5MdAXPv')
#         print(f"{post} downloading..")
#         L.download_post(post, target="downloads")
#     else:
#         print("Post ID not found in the link.")
#         print("Please provide a link to the function on line 19 !")
    
# linkdownload("https://www.instagram.com/reel/CsXr5MdAXPv")


import instaloader
import concurrent.futures
import PySimpleGUI as sg
from pathlib import Path


# Create an instance of Instaloader class
L = instaloader.Instaloader()

# Define function to download reel
def download_reel(reel_url):
    try:
        post = instaloader.Post.from_shortcode(L.context, reel_url.split("/")[-2])
        L.download_post(post, target=str(Path(post.owner_username)))

        # Delete all files except .mp4 in the post.owner_username directory
        for file in Path(post.owner_username).glob('*'):
            if not file.name.endswith('.mp4'):
                file.unlink()

        return True
    except Exception as e:
        print(f"Error downloading reel: {e}")
        return False

def download_reels(values):
    reel_urls = values['-URLS-'].split('\n')
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(download_reel, reel_urls))

    if all(results):
        sg.Popup('Success', 'All reels downloaded successfully.')
    else:
        sg.Popup('Error', 'One or more reels failed to download.')

# Define GUI layout
layout = [[sg.Text('Enter Instagram Reel URLs (one URL per line):')],
          [sg.Multiline(size=(50, 10), key='-URLS-')],
          [sg.Button('Download Reels'), sg.Button('Exit')]]

# Create GUI window
window = sg.Window('Instagram Reel Downloader', layout)

# Event loop to process "Download Reels" and "Exit" buttons
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Download Reels':
        download_reels(values)

# Close GUI window
window.close()
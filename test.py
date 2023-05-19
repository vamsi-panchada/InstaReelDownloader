# # # CrKZrkYKWsY

# # import instaloader
# # from instaloader import Post

# # L = instaloader.Instaloader()

# # post = Post.from_shortcode(L.context, "CrKZrkYKWsY")
# # L.download_post(post, target="#reels")


# # import instaloader

# # def download_instagram_reel(url):
# #     loader = instaloader.Instaloader()
# #     try:
# #         post = instaloader.Post.from_shortcode(loader.context, url)
# #         video_bytes = post.video_download_url().read()
# #         # You can save the video_bytes to a file or process it further
# #         # For example, you can save it to a local file:
# #         with open('reel.mp4', 'wb') as f:
# #             f.write(video_bytes)
# #         print("Instagram reel downloaded successfully!")
# #     except Exception as e:
# #         print(f"An error occurred while downloading the Instagram reel: {str(e)}")

# # # Provide the Instagram Reel URL
# # url = 'https://www.instagram.com/reel/CsIrqgbuYdd/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA=='

# # # Download the Instagram Reel
# # download_instagram_reel(url)


# # import instaloader

# # def download_instagram_reel(url):
# #     loader = instaloader.Instaloader()
# #     try:
# #         byte_array = loader.download_bytes(url)
# #         return byte_array
# #     except Exception as e:
# #         print(f"An error occurred while downloading the Instagram reel: {str(e)}")

# # # Example usage
# # reel_url = "https://www.instagram.com/reel/CsIrqgbuYdd/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA=="  # Replace with the actual Instagram Reel URL

# # reel_bytes = download_instagram_reel(reel_url)
# # if reel_bytes is not None:
# #     # Use the byte array as needed
# #     print(f"Reel downloaded successfully. Byte array size: {len(reel_bytes)} bytes")

# # import instaloader

# # instaloader = instaloader.Instaloader()
# # reel_url = "https://www.instagram.com/reel/CsIrqgbuYdd/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA=="  # Replace with the actual Instagram Reel URL
# # reel_video = instaloader.download_post(reel_url, 'reels')

# import requests

# # Replace the URL below with the URL of the Instagram reel video
# video_url = 'https://www.instagram.com/reel/CsYfQdNsWIR/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA=='

# # Send a GET request to download the video
# response = requests.get(video_url, stream=True)

# if response.status_code == 200:

#     with open('reel.mp4', 'wb') as f:
#         for chunk in response.iter_content(chunk_size=8124):
#             f.write(chunk)
#     print('success')



#     # Extract the video bytes
#     # video_bytes = response.content

#     # # Save the video bytes to a file or store it in a variable
#     # # Here, we are storing it in a variable named 'video_data'
#     # video_data = video_bytes
#     # print(video_data)

#     # with open('reel.mp4', 'wb') as f:
#     #     f.write(video_data)

#     # with open('reel.mp4', 'wb') as f:
#     #     for vb in video_data:
#     #         # f.write(vb)
#     #         print(vb)

#     # You can now use the 'video_data' variable as needed
# else:
#     print("Failed to download the video.")




from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
from tkinter import messagebox
from instascrape import Reel
import time

root =Tk()
root.title("Instagram Reel Downloader")
root.minsize(600,500)
root.maxsize(600,500)
HEIGHT = 500
WIDTH = 600
FONT = font.Font(family ="Times New Roman", size ="18", weight ="bold")


def download(link):
    try:
        if (link):
            SESSIONID = "18614737527%3ApTLwFoXv5BZohu%3A4"
            headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43",
            "cookie":f'sessionid={SESSIONID};'
            }

            google_reel=Reel(link)
            google_reel.scrape(headers=headers)
            google_reel.download(fp=f".\\reel{int(time.time())}.mp4")
            messagebox.showinfo("Status","Reel downloaded successfully")
        else:
            messagebox.showwarning("Empty field","Please fill out the field")
    except Exception as e:
        messagebox.showerror("Error","Something went wrong. Please try again later.")


canvas = Canvas(root,height = HEIGHT, width = WIDTH)
canvas.pack()

frame=Frame(root,bg="white")
frame.place(relwidth=1,relheight=1)

# background_image = ImageTk.PhotoImage(Image.open(r"instareel\insta5.jpg"))
# background_label = Label(frame, image = background_image)
# background_label.place(relx=-0.25,relwidth = 0.7, relheight =1)


label1 = Label(frame, text = "Download Reels in a Click!", font =FONT, bd =5, fg= "#0d1137",bg="white")
label1.place(relx = 0.48, rely = 0.1, relheight =0.1)



FONT = font.Font(family ="Times New Roman", size ="12", weight ="bold")
label2 = Label(frame, text = "Enter link address: ", font =FONT, bd =5, fg= "#e52165",bg="white")
label2.place(relx = 0.48, rely = 0.25, relheight =0.1)

entry = Entry(frame, font = FONT, fg = "#fbad50")
entry.place(relx = 0.48, rely = 0.35,relwidth=0.4, relheight = 0.05)

button1 = Button(root, text = "Download", font = FONT, bg = "pink", fg = "black", activeforeground = "pink", activebackground = "black",command=lambda:download(entry.get()))
button1.place(relx = 0.48,rely = 0.45,relwidth = 0.2, relheight = 0.06)

label2 = Label(frame, text = "Instructions: ", font =FONT, bd =5, fg= "#0d1137",bg="white")
label2.place(relx = 0.48, rely = 0.6, relheight =0.1)

FONT = font.Font(family ="Times New Roman", size ="10", weight ="bold")
TEXT="1.Only public account reels can be downloaded\n2.Enter the link address of reel from the Instagram\n3.This is not meant to be used for mischeif"
label2 = Label(frame, text = TEXT, font =FONT, bd =5, fg= "#cd486b",justify=LEFT,bg="white")
label2.place(relx = 0.48, rely = 0.7, relheight =0.1)



root.mainloop()
from instascrape import Reel
import time 

link = 'https://www.instagram.com/reel/CsXr5MdAXPv'
fname = str(time.time)
google_reel=Reel(link)
google_reel.download(fp=f".\\reel{int(time.time())}.mp4")
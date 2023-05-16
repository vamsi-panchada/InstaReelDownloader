# CrKZrkYKWsY

import instaloader
from instaloader import Post

L = instaloader.Instaloader()

post = Post.from_shortcode(L.context, "CrKZrkYKWsY")
L.download_post(post, target="#reels")

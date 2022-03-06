# importing the module
from pytube import YouTube
link = "https://www.youtube.com/watch?v=iF6L0mB1bEA"
myvideo = YouTube(link)
print(myvideo.title)
print(myvideo.thumbnail_url)
myvideo = myvideo.streams.all()
vid = list(enumerate(myvideo))
for i in vid:
	print(i)
strm = int(input("Enetr :  "))
myvideo[strm].download()
print("successfully")





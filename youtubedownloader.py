from pytube import YouTube

print("Creating youtube object...")
yt = YouTube("https://www.youtube.com/watch?v=dxfu33O_nT4")

print("Attempting to download...")
yt.streams[0].download()

"""

print("youtube object created...")
print("getting itags...")

filtered = yt.streams.filter(only_audio=True).filter(subtype='mp4')

print(filtered)

print("printing filtered[0]")

print(filtered[0])



filtered[0].download()



print("Done")


 """
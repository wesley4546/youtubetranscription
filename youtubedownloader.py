from pytube import YouTube

def download_youtubevideo(url):
    print("Creating YouTube Object from URL...")
    yt = YouTube(url)

    print("Which itag would you like to Download?")
    print(yt.streams)
    streamindex = int(input("Select itag using array indexing: "))

    print("Attempting to Download...")
    yt.streams[streamindex].download()

    print("Done!")


if __name__ == "__main__":
    url = input("Enter Youtube URL:")
    download_youtubevideo(url)









from pytube import YouTube

"""
This is not used in main.py - I thought I would have to use this method of getting videos but figured an alternative 
way to get it done. This function could be useful in other contexts so I am not deleting it.
"""

def download_youtubevideo(URL):
    """
    This function takes a URL and leads the user through downloading it.
    """

    # Creates YouTube object
    print("Creating YouTube Object from URL...")
    yt = YouTube(URL)

    # Displays the streams and itags from object for user-choosing
    print("Which itag would you like to Download?")
    print(yt.streams)
    streamindex = int(input("Select itag using array indexing: "))

    # Downloads video based off user-chosen indexing
    print("Attempting to Download...")
    yt.streams[streamindex].download()

    print("Done!")


if __name__ == "__main__":
    url = input("Enter Youtube URL: ")
    download_youtubevideo(url)

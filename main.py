import time
import csv
import sys
from source.youtubescraper import get_video_info
from source.get_transcription import get_transcription
from source.youtubescraper import get_youtube_urls


# Creation of youtubevideo class
class youtubevideo:
    def __init__(self, url, title, description, views, published, likes, dislikes, channel_name, channel_url,
                 channel_subscribers, transcription):
        self.url = url
        self.title = title
        self.description = description
        self.views = views
        self.published = published
        self.likes = likes
        self.dislikes = dislikes
        self.channel_name = channel_name
        self.channel_url = channel_url
        self.channel_subscribers = channel_subscribers
        self.transcription = transcription

    def get_like_ratio(self):
        # Gets the ratio of likes to dislikes
        ratio = self.likes / self.dislikes
        return ratio


# Creates a function to create a file name based off the keyword
def paste_filename(keyword):
    cleaned_keyword = keyword.replace(' ', '_')

    filename = cleaned_keyword + "_videos.csv"

    return filename


# MAIN PROGRAM
def search_video_extraction_program():
    """
    Function starts the process of extracting videos from YouTube using a user-input search

    I'm not sure of any restrictions when it comes to API calls from other modules in this program so I have a delay
    of 2 seconds between each function call in the looping process and a 2 second delay between each URL. If this causes
    and issue then it can certainly be changed.
    """
    url_number = 1

    # Takes a YouTube URL as input
    input_keyword = input("Enter YouTube Search: ")

    # Data used as each column
    csv_column_names = ['keyword', 'url', 'title', 'description', 'views', 'published', 'likes', 'dislikes',
                        'channel_name', 'channel_url',
                        'channel_subscribers', 'transcription']

    # Creates a file
    print("Creating New CSV File...")
    with open(paste_filename(input_keyword), 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(csv_column_names)

    print("Getting YouTube URLs based off search...")

    # Gets the list of URLs based off the keyword received
    list_of_urls = get_youtube_urls(input_keyword)

    # The number of URLS found
    length_of_URLs = len(list_of_urls)

    print(f"{length_of_URLs} YouTube video URLs found from search")

    # Keeps track of the iteration of the URLS
    list_of_urls_index_counter = 0

    for url in list_of_urls:
        print(f"Starting URL {url_number}...")

        # Extracts the video information
        youtube_video_info = get_video_info(url)
        time.sleep(2)

        # Gets the YouTube transcriptions
        clean_transcription = get_transcription(url)
        time.sleep(2)

        # Stores them as a youtubevideo object
        yt_v = youtubevideo(
            url=list_of_urls[list_of_urls_index_counter],
            title=youtube_video_info['title'],
            description=youtube_video_info['description'],
            views=youtube_video_info['views'],
            published=youtube_video_info['date_published'],
            likes=youtube_video_info['likes'],
            dislikes=youtube_video_info['dislikes'],
            channel_name=youtube_video_info['channel']['name'],
            channel_url=youtube_video_info['channel']['url'],
            channel_subscribers=youtube_video_info['channel']['subscribers'],
            transcription=clean_transcription
        )

        # Increments index counter
        list_of_urls_index_counter += 1

        # Creates the row in which will be appended to the CSV file
        csv_file_rows = (input_keyword,
                         yt_v.url,
                         yt_v.title,
                         yt_v.description,
                         yt_v.views,
                         yt_v.published,
                         yt_v.likes,
                         yt_v.dislikes,
                         yt_v.channel_name,
                         yt_v.channel_url,
                         yt_v.channel_subscribers,
                         yt_v.transcription)

        # Appends the CSV file with the found video information/transcripts
        with open(paste_filename(input_keyword), 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(csv_file_rows)

        print(f"{url_number} / {length_of_URLs} YouTube URLs Complete.")

        # Increments URL number
        url_number += 1
        time.sleep(2)


if __name__ == '__main__':
    print("Welcome to the YouTube Transcription Program found at https://github.com/wesley4546/youtubetranscription")
    print("Feel free to make an issue on GitHub if you find a bug or have a suggestion")
    search_video_extraction_program()

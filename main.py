import time
import csv
from source.youtubescraper import get_video_info
from source.get_transcription import get_transcription
from source.youtubeurlsearch import get_keyword_urls


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


if __name__ == '__main__':

    url_number = 1

    # Takes a YouTube URL as input
    input_keyword = input("Enter Keyword: ")

    # Data used as each column
    csv_column_names = ['keyword', 'url', 'title', 'description', 'views', 'published', 'likes', 'dislikes',
                        'channel_name', 'channel_url',
                        'channel_subscribers', 'transcription']

    # Creates a file
    print("Creating New CSV File...")
    with open(paste_filename(input_keyword), 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(csv_column_names)

    print("Getting YouTube URLs based off keyword...")
    list_of_urls = get_keyword_urls(input_keyword)

    list_of_urls_index_counter = 0

    for url in list_of_urls:
        print(f"URL {url_number} started")
        # Extracts the video information
        youtube_video_info = get_video_info(url)

        # Gets the YouTube transcriptions
        clean_transcription = get_transcription(url)

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

        with open(paste_filename(input_keyword), 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(csv_file_rows)

        print(f"URL {url_number} done")
        url_number += 1
        time.sleep(3)

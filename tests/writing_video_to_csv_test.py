import time
import csv
from source.youtubescraper import get_video_info
from source.get_transcription import get_transcription
from source.youtubescraper import get_youtube_urls
from main import keyword_video_extraction_program
from main import youtubevideo



# Main Program
keyword_video_extraction_program()

# Testing
csv_column_names = ['keyword', 'url', 'title', 'description', 'views', 'published', 'likes', 'dislikes',
                    'channel_name', 'channel_url',
                    'channel_subscribers', 'transcription']

with open("testing_main.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(csv_column_names)

input_keyword = input("Enter Keyword: ")

list_of_urls = get_youtube_urls(input_keyword)

list_of_urls_index_counter = 0

for url in list_of_urls:

    # Extracts the video information
    youtube_video_info = get_video_info(url)
    time.sleep(5)
    # Gets the YouTube transcriptions
    clean_transcription = get_transcription(url)
    time.sleep(5)

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
    with open("testing_main.csv", 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(csv_file_rows)

    time.sleep(5)

from source.youtubescraper import get_video_info
from source.transcriptor import get_transcription


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


if __name__ == '__main__':
    # Takes a YouTube URL as input
    input_url = input("Enter YouTube URL: ")

    # Extracts the video information
    youtube_video_info = get_video_info(input_url)

    # Gets the YouTube transcriptions
    clean_transcription = get_transcription(input_url)

    # Stores them as a youtubevideo object
    youtube_video = youtubevideo(
        url=input_url,
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
    print("Done!")
    print("Access your video through 'youtube_video' variable")

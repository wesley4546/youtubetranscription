import requests
from bs4 import BeautifulSoup as bs

class video:
    def __init__(self, url, title, description, views, published, likes, dislikes, channel_name, channel_url,
                 channel_subscribers):
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


def get_video_info(url):
    # from https://www.thepythoncode.com/article/get-youtube-data-python
    print("Downloading URL...")
    # download HTML code
    content = requests.get(url)

    # create beautiful soup object to parse HTML
    soup = bs(content.content, "html.parser")
    print("Initializing Variables...")
    # initialize the result
    result = {}

    print("Extracting values...")
    # video title
    result['title'] = soup.find("span", attrs={"class": "watch-title"}).text.strip()

    # video views (converted to integer)
    result['views'] = int(soup.find("div", attrs={"class": "watch-view-count"}).text[:-6].replace(",", ""))

    # video description
    result['description'] = soup.find("p", attrs={"id": "eow-description"}).text

    # date published
    result['date_published'] = soup.find("strong", attrs={"class": "watch-time-text"}).text

    # number of likes as integer
    result['likes'] = int(soup.find("button", attrs={"title": "I like this"}).text.replace(",", ""))

    # number of dislikes as integer
    result['dislikes'] = int(soup.find("button", attrs={"title": "I dislike this"}).text.replace(",", ""))

    # channel details
    channel_tag = soup.find("div", attrs={"class": "yt-user-info"}).find("a")
    # channel name
    channel_name = channel_tag.text
    # channel URL
    channel_url = f"https://www.youtube.com{channel_tag['href']}"
    # number of subscribers as str
    channel_subscribers = soup.find("span", attrs={"class": "yt-subscriber-count"}).text.strip()
    result['channel'] = {'name': channel_name, 'url': channel_url, 'subscribers': channel_subscribers}
    # return the result
    print("Done!")
    return result


if __name__ == '__main__':

    input_url = input("Enter YouTube URL: ")

    youtube_video_info = get_video_info(input_url)

    youtube_video = video(
        url=input_url,
        title=youtube_video_info['title'],
        description=youtube_video_info['description'],
        views=youtube_video_info['views'],
        published=youtube_video_info['date_published'],
        likes=youtube_video_info['likes'],
        dislikes=youtube_video_info['dislikes'],
        channel_name=youtube_video_info['channel']['name'],
        channel_url=youtube_video_info['channel']['url'],
        channel_subscribers=youtube_video_info['channel']['subscribers']
    )

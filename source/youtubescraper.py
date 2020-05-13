import requests
import urllib.request
from bs4 import BeautifulSoup as bs


def get_video_info(url):
    """
      from https://www.thepythoncode.com/article/get-youtube-data-python

      Function takes a YouTube URL and extracts the different parts of the video:
      title, view number, description, date-published, likes, dislikes, channel name,
      channel url, and channel subscribers. Returned as python dictionary.
    """
    # from https://www.thepythoncode.com/article/get-youtube-data-python
    # download HTML code
    try:

        content = requests.get(url)

        # create beautiful soup object to parse HTML
        soup = bs(content.content, "html.parser")
        # initialize the result
        result = {}

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
        return result
    except:
        # Returns an no video information found dictionary
        print("No Video Information Found.")
        result = {'title': "No Video Information Found",
                  'views': "No Video Information Found",
                  'description': "No Video Information Found",
                  'date_published': "No Video Information Found",
                  'likes': "No Video Information Found",
                  'dislikes': "No Video Information Found"}
        # channel details
        channel_tag = 'No Video Information Found'
        # channel name
        channel_name = 'No Video Information Found'
        # channel URL
        channel_url = 'No Video Information Found'
        # number of subscribers as str
        channel_subscribers = 'No Video Information Found'
        result['channel'] = {'name': channel_name, 'url': channel_url, 'subscribers': channel_subscribers}

        return result


def get_youtube_url(keyword):
    list_of_urls = []

    query = urllib.parse.quote(keyword)

    # Constructs URL
    url = "https://www.youtube.com/results?search_query=" + query

    # Get's a response
    response = urllib.request.urlopen(url)

    # Saves response
    html = response.read()

    # Creates Soup Object
    soup = bs(html, 'html.parser')

    # Loops through
    for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
        if not vid['href'].startswith("https://googleads.g.doubleclick.net/"):
            url = ('https://www.youtube.com' + vid['href'])
            list_of_urls.append(url)

    return list_of_urls

import requests
import urllib.request
import re
from bs4 import BeautifulSoup as bs


def get_video_info(url):
    """
      from https://www.thepythoncode.com/article/get-youtube-data-python

      Function takes a YouTube URL and extracts the different parts of the video:
      title, view number, description, date-published, likes, dislikes, channel name,
      channel url, and channel subscribers. Returned as python dictionary.
    """

    # TODO: This works for most videos however there are videos that come up
    #       that have video info but are reported missing

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

        try:
            # number of likes as integer
            result['likes'] = int(soup.find("button", attrs={"title": "I like this"}).text.replace(",", ""))

            # number of dislikes as integer
            result['dislikes'] = int(
                soup.find("button", attrs={"title": "I dislike this"}).text.replace(",", ""))
        except:
            try:
                # This took me so long to figure out. If you can find a better way PLEASE let me know
                # Saves FULL html file into a variable
                video_html = soup.prettify()

                # pattern to extract html code that has the like count
                pattern_like = re.compile(r'\\"likeCount\\":[0-9]+[0-9]')

                # pattern to extract numbers our of like count
                pattern_like2 = re.compile(r'[0-9]+[0-9]')

                # Finds the html code with likecount
                matches_in_html_like = pattern_like.findall(video_html)

                # Extracts the numbers from the html code
                cleaned_html_number_like = int((pattern_like2.findall(''.join(matches_in_html_like)))[0])

                result['likes'] = cleaned_html_number_like

                pattern_dislike = re.compile(r'\\"dislikeCount\\":[0-9]+[0-9]')
                # pattern to extract numbers our of like count
                pattern_dislike2 = re.compile(r'[0-9]+[0-9]')

                # Finds the html code with likecount
                matches_in_html_dislike = pattern_dislike.findall(video_html)

                # Extracts the numbers from the html code
                cleaned_html_number_dislike = int((pattern_dislike2.findall(''.join(matches_in_html_dislike)))[0])

                result['dislikes'] = cleaned_html_number_dislike
            except:
                result['likes'] = "Not Found (Perhaps Hidden)"
                result['dislikes'] = "Not Found (Perhaps Hidden)"

        # channel details
        channel_tag = soup.find("div", attrs={"class": "yt-user-info"}).find("a")
        # channel name
        channel_name = channel_tag.text
        # channel URL
        channel_url = f"https://www.youtube.com{channel_tag['href']}"

        # Some youtubers can hide their subscription count from public - This tests that
        try:
            channel_subscribers = soup.find("span", attrs={"class": "yt-subscriber-count"}).text.strip()
        except:
            channel_subscribers = "Not Found (Perhaps Hidden)"

        result['channel'] = {'name': channel_name, 'url': channel_url, 'subscribers': channel_subscribers}

        # return the result
        print("Video Information Found.")
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
        channel_tag = 'No Video Information Found'
        channel_name = 'No Video Information Found'
        channel_url = 'No Video Information Found'
        channel_subscribers = 'No Video Information Found'
        result['channel'] = {'name': channel_name, 'url': channel_url, 'subscribers': channel_subscribers}

        return result


def get_youtube_urls(keyword):
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

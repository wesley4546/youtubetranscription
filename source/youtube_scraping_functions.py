import requests
import urllib.request
import re
from bs4 import BeautifulSoup as bs


def get_video_info(url):
    """
      adapted from https://www.thepythoncode.com/article/get-youtube-data-python

      Function takes a YouTube URL and extracts the different parts of the video:
      title, view number, description, date-published, likes, dislikes, channel name,
      channel url, and channel subscribers. Returned as python dictionary.
    """

    # TODO: This works for most videos however there are videos that come up
    #       that have video info but are reported missing

    # adapted from https://www.thepythoncode.com/article/get-youtube-data-python
    # Starts the process of scraping the video information
    try:

        # requests URL
        content = requests.get(url)

        # create beautiful soup object to parse HTML
        soup = bs(content.content, "html.parser")

        # initialize the result
        result = {}

        # video title
        try:
            result['title'] = soup.find("span", attrs={"class": "watch-title"}).text.strip()
        except:
            result['title'] = "Not Found (Perhaps Hidden)"

        # try-catch for finding video views using the HTML 'watch-view-count'
        try:
            # video views (converted to integer)
            result['views'] = int(
                soup.find("div", attrs={"class": "watch-view-count"}).text[:-6].replace(",", ""))
        except:
            try:
                # Tries to find the views using the 'stat view-count'
                result['views'] = int(
                    soup.find("span", attrs={"class": "stat view-count"}).text[:-6].replace(",", "").replace("views",
                                                                                                             ""))
            except:
                # If views can't be found
                result['views'] = "Not Found (Perhaps Hidden)"

        # video description
        try:
            result['description'] = soup.find("p", attrs={"id": "eow-description"}).text
        except:
            result['description'] = "Not Found (Perhaps Hidden)"

        # date published
        try:
            result['date_published'] = soup.find("strong", attrs={"class": "watch-time-text"}).text.replace(
                "Published on ", "").replace("Premiered ", "")
        except:
            result['date_published'] = "Not Found (Perhaps Hidden)"

        # try-catch for finding the likes and dislikes
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

                # Finds the html code with dislikeCount
                matches_in_html_dislike = pattern_dislike.findall(video_html)

                # Extracts the numbers from the html code
                cleaned_html_number_dislike = int((pattern_dislike2.findall(''.join(matches_in_html_dislike)))[0])

                result['dislikes'] = cleaned_html_number_dislike
            except:
                result['likes'] = "Not Found (Perhaps Hidden)"
                result['dislikes'] = "Not Found (Perhaps Hidden)"

        # channel details
        try:
            channel_tag = soup.find("div", attrs={"class": "yt-user-info"}).find("a")
        except:
            channel_tag = "Not Found (Perhaps Hidden)"

        # channel name
        try:
            channel_name = channel_tag.text
        except:
            channel_name = "Not Found (Perhaps Hidden)"

        # channel URL
        try:
            channel_url = f"https://www.youtube.com{channel_tag['href']}"
        except:
            channel_url = "Not Found (Perhaps Hidden)"

        # try-catch for subscription count (youtube user can hide these)
        try:
            channel_subscribers = soup.find("span", attrs={"class": "yt-subscriber-count"}).text.strip()
        except:
            channel_subscribers = "Not Found (Perhaps Hidden)"

        result['channel'] = {'name': channel_name, 'url': channel_url, 'subscribers': channel_subscribers}

        # return the result
        print("Video Information Found.")
        return result


    # If none of the information can be found will result in this a blank video info
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
    """
    Function takes a keyword and searches youtube to obtain a list of URLs
    """
    list_of_urls = []

    # Parses the keyword
    query = urllib.parse.quote(keyword)

    # Constructs URL
    url = "https://www.youtube.com/results?search_query=" + query

    # Get's a response
    response = urllib.request.urlopen(url)

    # Saves response
    html = response.read()

    # Creates Soup Object
    soup = bs(html, 'html.parser')

    # Loops through URLs and appends them to list
    for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
        if not vid['href'].startswith("https://googleads.g.doubleclick.net/"):
            url = ('https://www.youtube.com' + vid['href'])
            list_of_urls.append(url)

    return list_of_urls

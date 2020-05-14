import requests
import urllib.request
import re
from bs4 import BeautifulSoup as bs
from source.youtubescraper import get_video_info

"""
This is a test to check if a URL is outputting the correct video information

Tutorial:
1.) Place URL in url_to_test variable and check video_info object
2.) Run Debug feature in Pycharm

Excepted: 
All the keys should be filled in with the video information found on YouTube. 
"""

url_to_test = "https://www.youtube.com/watch?v=Fqw-9yMV0sI"

# Main program
video_info = get_video_info(url_to_test)

# Testing
content = requests.get(url_to_test)

# create beautiful soup object to parse HTML
soup = bs(content.content, "html.parser")


# initialize the result
test_video_info = {}

# video title
test_video_info['title'] = soup.find("span", attrs={"class": "watch-title"}).text.strip()

try:
    # video views (converted to integer)
    test_video_info['views'] = int(soup.find("div", attrs={"class": "watch-view-count"}).text[:-6].replace(",", ""))
except:
    try:
        test_video_info['views'] = int(
            soup.find("span", attrs={"class": "stat view-count"}).text[:-6].replace(",", "").replace("views", ""))
    except:
        test_video_info['views'] = "Not Found (Perhaps Hidden)"

# video description
test_video_info['description'] = soup.find("p", attrs={"id": "eow-description"}).text

# date published
test_video_info['date_published'] = soup.find("strong", attrs={"class": "watch-time-text"}).text.replace(
    "Published on ", "").replace("Premiered ", "")

try:
    # number of likes as integer
    test_video_info['likes'] = int(soup.find("button", attrs={"title": "I like this"}).text.replace(",", ""))

    # number of dislikes as integer
    test_video_info['dislikes'] = int(soup.find("button", attrs={"title": "I dislike this"}).text.replace(",", ""))
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

        test_video_info['likes'] = cleaned_html_number_like

        pattern_dislike = re.compile(r'\\"dislikeCount\\":[0-9]+[0-9]')
        # pattern to extract numbers our of like count
        pattern_dislike2 = re.compile(r'[0-9]+[0-9]')

        # Finds the html code with likecount
        matches_in_html_dislike = pattern_dislike.findall(video_html)

        # Extracts the numbers from the html code
        cleaned_html_number_dislike = int((pattern_dislike2.findall(''.join(matches_in_html_dislike)))[0])

        test_video_info['dislikes'] = cleaned_html_number_dislike
    except:
        test_video_info['likes'] = "Not Found (Perhaps Hidden)"
        test_video_info['dislikes'] = "Not Found (Perhaps Hidden)"

# channel details
channel_tag = soup.find("div", attrs={"class": "yt-user-info"}).find("a")
# channel name
channel_name = channel_tag.text
# channel URL
channel_url = f"https://www.youtube.com{channel_tag['href']}"
# number of subscribers as str
try:
    channel_subscribers = soup.find("span", attrs={"class": "yt-subscriber-count"}).text.strip()
except:
    channel_subscribers = "Not Found (Perhaps Hidden)"

test_video_info['channel'] = {'name': channel_name, 'url': channel_url, 'subscribers': channel_subscribers}

are_they_equal = test_video_info == video_info

test = soup.prettify()

print("End")

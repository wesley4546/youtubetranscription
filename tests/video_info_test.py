import requests
import urllib.request
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

url_to_test = "https://www.youtube.com/watch?v=TyLcR-QwCyY"

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

# video views (converted to integer)
test_video_info['views'] = int(soup.find("div", attrs={"class": "watch-view-count"}).text[:-6].replace(",", ""))

# video description
test_video_info['description'] = soup.find("p", attrs={"id": "eow-description"}).text

# date published
test_video_info['date_published'] = soup.find("strong", attrs={"class": "watch-time-text"}).text

# number of likes as integer
test_video_info['likes'] = int(soup.find("button", attrs={"title": "I like this"}).text.replace(",", ""))

# number of dislikes as integer
test_video_info['dislikes'] = int(soup.find("button", attrs={"title": "I dislike this"}).text.replace(",", ""))

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
    channel_subscribers = "No Subscribers Found (Perhaps Hidden)"

test_video_info['channel'] = {'name': channel_name, 'url': channel_url, 'subscribers': channel_subscribers}

are_they_equal = test_video_info == video_info

print("End")

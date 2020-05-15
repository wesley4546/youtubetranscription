import requests
import urllib.request
import re
from bs4 import BeautifulSoup as bs
from source.youtube_scraping_functions import get_video_info

"""
This is a test to check if a URL is outputting the correct video information

Tutorial:
1.) Place URL in url_to_test variable and check video_info object
2.) Run script

Excepted: 
All the keys should be filled in with the video information found on YouTube. 
"""


# Url to test
url = "https://www.youtube.com/watch?v=unLLM3Jann8"


def test_video_info_url(get_video_info_list):
    """
    Function evaluates the list generated from get_video_info() against a blank one to see any missing info and
    prints out results
    """
    print("Testing URL...")
    # Blank result for logical testing
    result_blank = {'title': "No Video Information Found",
                    'views': "No Video Information Found",
                    'description': "No Video Information Found",
                    'date_published': "No Video Information Found",
                    'likes': "No Video Information Found",
                    'dislikes': "No Video Information Found"}
    blank_channel_tag = 'No Video Information Found'
    blank_channel_name = 'No Video Information Found'
    blank_channel_url = 'No Video Information Found'
    blank_channel_subscribers = 'No Video Information Found'
    result_blank['channel'] = {'name': blank_channel_name, 'url': blank_channel_url,
                               'subscribers': blank_channel_subscribers}

    print("#----------------------- Results ------------------------#")
    # Checks to see if the blank result object was returned
    if get_video_info_list == result_blank:
        print("Blank result object returned")

    # Prints out each result
    for item in get_video_info_list:
        if get_video_info_list[item] == "Not Found (Perhaps Hidden)":
            print(f"{item}: Missing - X")
        else:
            print(f"{item}: Found - V")

    for channel_descriptor in get_video_info_list['channel']:
        if get_video_info_list['channel'][channel_descriptor] == "Not Found (Perhaps Hidden)":
            print(f"channel {channel_descriptor}: Missing - X")
        else:
            print(f"channel {channel_descriptor}: Found - V")

    print("Testing Complete!")


if __name__ == '__main__':
    # Test
    test_video_info_url(get_video_info(url))

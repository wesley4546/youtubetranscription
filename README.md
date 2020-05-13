# YouTube Transcription

## Introduction
This repository houses a progam that can extract key details and the auto-generated transcriptions from youtube videos. It uses `BeautifulSoup` for the details and `youtube_transcript_api` for the transcriptions. (All which are found in the `requirements.txt`)

## Tutorial
It's rather easy!

 1) Run `main.py`
 1) Enter what you would like to search
 1) It will get the youtube videos from your search and download the different details of each video as well as the transcript into a csv file format.


### `youtubevideo` class
The `youtubevideo` class has the following variables:
 * `url` (the video's URL)
 * `title` (title of video)
 * `description` (description of video)
 * `views` (number of views of video)
 * `published` (date of publication)
 * `likes` (likes of video)
 * `dislikes` (dislikes of video)
 * `channel_name` (name of channel)
 * `channel_url` (URL of channel from video)
 * `channel_subscribers` (number of subscribers)
 * `transcription` (auto-generated transcripts of video)


## Useful Links
https://python.gotrained.com/youtube-api-extracting-comments/


## References
Big shout-out to Abdou Rockikz for their post found: https://www.thepythoncode.com/article/get-youtube-data-python

from youtube_transcript_api import YouTubeTranscriptApi

# Youtube video ID https://www.youtube.com/watch?v=XXXXXXXXXXXX (Only the X's)
video_id = "kuOEpC4u6Tg"

# Creates a blank list to iterate over
text_parts = []

# Counter variable
iteration_of_raw = 0

# Gets a list of dictionaries of the youtube transcriptions
raw_transcription = YouTubeTranscriptApi.get_transcript(video_id)

# Iterates over each dictionary and extracts 'text' key then appends the blank text_parts list
for dictonary in raw_transcription:
    indexed_dictionary = raw_transcription[iteration_of_raw]
    text_from_dictionary = indexed_dictionary['text']
    text_parts.append(text_from_dictionary)
    iteration_of_raw += 1

# Defines how we want each text element to be separated with
separator_for_each_text = ". "

# Joins the separator with the text_parts
clean_transcription = separator_for_each_text.join(text_parts)

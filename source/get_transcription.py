import sys
from youtube_transcript_api import YouTubeTranscriptApi


def get_transcription(url):
    """
    Function takes a YouTube video URL and extracts the automatically-generated transcripts from it
    """

    # Checks the format of the URL
    if "https://www.youtube.com/watch?v=" in url:
        input_url_id = url.replace("https://www.youtube.com/watch?v=", "")
    elif "https://youtu.be/" in url:
        input_url_id = url.replace("https://youtu.be/", "")

    # Creates a blank list to iterate over
    text_parts = []

    # Gets a list of all available transcripts
    try:

        list_of_transcripts = YouTubeTranscriptApi.list_transcripts(input_url_id)
        print("Checking for Transcriptions...")
        # Checks to see if a manual transcript is created if not, checks to see if a generated one is created
        if 'en-US' in list_of_transcripts._manually_created_transcripts:
            print("Manual Transcription Found")
            transcript = list_of_transcripts.find_manually_created_transcript(['en-US'])
        elif 'en' in list_of_transcripts._manually_created_transcripts:
            print("Manual Transcription Found")
            transcript = list_of_transcripts.find_manually_created_transcript(['en'])
        elif 'en' in list_of_transcripts._generated_transcripts:
            print("Auto-Generated Transcription Found")
            transcript = list_of_transcripts.find_generated_transcript(['en'])

        # Saves the transcript into a variable to iterate over
        raw_transcription = transcript.fetch()

        # Indexing of raw transcripts
        iteration_of_raw = 0

        # Iterates over each dictionary and extracts 'text' key then appends the blank text_parts list
        for i in raw_transcription:
            indexed_dictionary = raw_transcription[iteration_of_raw]
            text_from_dictionary = indexed_dictionary['text']
            text_parts.append(text_from_dictionary)
            iteration_of_raw += 1
        # Defines how we want each text element to be separated with
        separator_for_each_text = " "

        # Joins the separator with the text_parts
        clean_transcription = separator_for_each_text.join(text_parts)

        # Returns the cleaned transcripts
        return clean_transcription

    except:
        print("No Transcriptions Found")
        clean_transcription = "No Transcriptions Found"
        return clean_transcription




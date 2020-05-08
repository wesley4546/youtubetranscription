from youtube_transcript_api import YouTubeTranscriptApi


def get_transcription(url):

    """
    Function takes a YouTube video URL and extracts the automatically-generated transcripts from it
    """

    #Checks the format of the URL
    if "https://www.youtube.com/watch?v=" in url:
        input_url_id = url.replace("https://www.youtube.com/watch?v=", "")
    elif "https://youtu.be/" in url:
        input_url_id = url.replace("https://youtu.be/", "")

    # Creates a blank list to iterate over
    text_parts = []

    # Counter variable
    iteration_of_raw = 0

    print("Getting Transcriptions...")

    # Gets a list of dictionaries of the youtube transcriptions
    raw_transcription = YouTubeTranscriptApi.get_transcript(input_url_id)

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

import speech_recognition as sr
import subprocess
"""
This is not used in main.py - I thought I would have to use this method of getting videos but figured an alternative 
way to get it done. This function could be useful in other contexts so I am not deleting it.
"""

command = "ffmpeg" \
          " -i test.mp4" \
          " -ab 160k " \
          " -ac 2 " \
          " -ar 44100 " \
          " -vn audio.wav"

subprocess.call(command, shell=True)




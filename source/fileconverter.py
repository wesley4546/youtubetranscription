import speech_recognition as sr
import subprocess


command = "ffmpeg" \
          " -i test.mp4" \
          " -ab 160k " \
          " -ac 2 " \
          " -ar 44100 " \
          " -vn audio.wav"

subprocess.call(command, shell=True)




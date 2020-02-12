import speech_recognition as sr

"""
All this does is list all available devices on your pi
will confirm if all mics can been seen
"""

for i, n in enumerate(sr.Microphone.list_microphone_names()):
    print(f"mic_name{n}, index {i}")

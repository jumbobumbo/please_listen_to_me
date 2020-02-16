import speech_recognition as sr
from time import sleep

# can we connect to our mic?
"All I do is try and repeat what you said"


def callback(recognizer_instance, audio):
    # received audio data
    print("do we ever go in here?")
    print(audio)
    audio_data = recognizer_instance.recognize_sphinx(audio, language='en-US', keyword_entries=[("hello", 1.0)], grammar=None, show_all=False)
    print(f"sphinx captured data: {audio_data}")


r = sr.Recognizer()
m = sr.Microphone(2, 16000)
with m as source:
    print("Say something!")
    r.adjust_for_ambient_noise(source)
    print("listening")

# wait
sleep(2)

# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback)

# wait
sleep(8)

# calling this function requests that the background listener stop listening
stop_listening(wait_for_stop=False)

# let things tidy up
sleep(5)


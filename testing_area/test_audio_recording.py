import speech_recognition as sr
from time import sleep

# can we connect to our mic?
"All I do is try and repeat what you said"

r = sr.Recognizer()
m = sr.Microphone(2)
with m as source:
    print("Say something!")
    audio = r.listen(source)


def callback(recognizer, audio_data):
    # received audio data, now we'll recognize it using Google Speech Recognition
    print("sphinx thinks you said: " + recognizer.recognize_sphinx(audio_data))


# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback)

# wait
sleep(5)

# calling this function requests that the background listener stop listening
stop_listening(wait_for_stop=False)

# let things tidy up
sleep(2)

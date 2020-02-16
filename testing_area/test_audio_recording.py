import speech_recognition as sr
from time import sleep

# can we connect to our mic?
"All I do is try and repeat what you said"


def callback(recognizer_instance, audio):
    # received audio data
    print("do we ever go in here?")
    print("sphinx thinks you said: " + recognizer_instance.recognize_sphinx(audio))


r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    print("Say something!")
    r.adjust_for_ambient_noise(source)
    print("listening")

# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback)

# wait
sleep(5)

# calling this function requests that the background listener stop listening
stop_listening(wait_for_stop=False)

# let things tidy up
sleep(2)
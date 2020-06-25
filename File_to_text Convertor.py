import speech_recognition as sr
filename='hi.wav'
r=sr.Recognizer()
#open the file
with sr.AudioFile(filename) as source:
    #listen for the data(load audio to memory)
    audio = r.record(source)
    #recognize(convert from speech to text)
    text = r.recognize_google(audio)
    print(text)

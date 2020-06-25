import speech_recognition as sr
#initialize the recognizer
r=sr.Recognizer()
print("Please talk")
with sr.Microphone() as source:
    try:
        #read the audio data from the default microphone
        audio_data=r.record(source,duration=5)
        print("Recognizing...")
        #convert speech to text
        text=r.recognize_google(audio_data)
        print(text)
    except:
        print("Voice not Recognized")
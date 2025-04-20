import pyttsx3, speech_recognition as sr, wikipedia

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            return r.recognize_google(audio)
        except:
            return "Sorry, I didn't catch that."

while True:
    command = listen()
    if 'Wikipedia' in command:
        topic = command.replace('Wikipedia', '')
        result = wikipedia.summary(topic, sentences=2)
        speak(result)
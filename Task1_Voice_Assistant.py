# Voice Assistant - OIBSIP Python Programming Task

import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import requests

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture voice input and convert to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio).lower()
            print(f"You said: {query}")
            return query
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Network error. Please check your internet connection.")
            return ""

def get_time():
    """Get the current time."""
    time_now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {time_now}")

def get_date():
    """Get the current date."""
    date_now = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today is {date_now}")

def search_wikipedia(query):
    """Search Wikipedia for a given query."""
    try:
        speak(f"Searching Wikipedia for {query}...")
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except wikipedia.DisambiguationError:
        speak("There are multiple results for your query. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("Sorry, no information was found.")
    except Exception:
        speak("An error occurred while searching.")

def get_weather():
    """Fetch current weather information."""
    api_key = "your_api_key_here"
    city = "Mumbai"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url).json()
        temp = response['main']['temp']
        description = response['weather'][0]['description']
        speak(f"The current temperature in {city} is {temp} degrees Celsius with {description}.")
    except:
        speak("Unable to fetch weather data.")

def main():
    """Main function to run the voice assistant."""
    speak("Hello! I am your voice assistant. How can I help you?")
    while True:
        query = listen()

        if "exit" in query or "stop" in query:
            speak("Goodbye!")
            break
        elif "time" in query:
            get_time()
        elif "date" in query:
            get_date()
        elif "wikipedia" in query:
            query = query.replace("wikipedia", "").strip()
            search_wikipedia(query)
        elif "weather" in query:
            get_weather()
        elif "hello" in query:
            speak("Hello! How can I assist you?")
        else:
            speak("I can only help with time, date, Wikipedia, and weather information right now.")

if __name__ == "__main__":
    main()

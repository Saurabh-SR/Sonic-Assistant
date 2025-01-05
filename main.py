import random
from time import strftime
import speech_recognition as sr
import os
import win32com.client
import webbrowser
import datetime
import requests

speaker = win32com.client.Dispatch("SAPI.SpVoice")
weather_api = "aec1373f6bea4568890133636250201"

def say(text):
        speaker.Speak(text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        audio = r.listen(source)
        try:
            print("recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said {query}")
        except Exception as e:
            return "Some error occurred, Sorry from AI Bot"

        return query

def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={weather_api}&q={city}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp_c = data['current']['temp_c']
            condition = data['current']['humidity']
            return f"The current temperature in {city} is {temp_c}°C"
        else:
            return "I couldn't fetch the weather data."
    except Exception as e:
        return "An error occurred while getting the weather."


if __name__ == '__main__':
    say("Hello, I am Sonic Assistant, How can I help you?")
    while True:
        print("Listening...")
        query = takeCommand()
        #say(query)
        sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"], ["google", "https://google.com"],["amazon", "https://amazon.com"], ["instagram", "https://instagram.com"],
        ["facebook", "https://facebook.com"], ["Spotify", "https://spotify.com"]]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...... ")
                webbrowser.open(site[1])
                break

        if "play music" in query:       #For Song present in my laptop at music folder
            musicpath = '"C:/Users/monur/Music/Moonlight Sonata.mp3"'
            os.startfile(musicpath)

        elif "current time" in query:       #For time
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir the time is {hour} hour {min} minutes")

        elif "open tableau".lower() in query.lower():
            os.startfile( 'C:/Program Files/Tableau/Tableau Public 2024.1/bin/tabpublic.exe')

        elif "weather in" in query.lower():
            city = query.split("in")[-1].strip()
            weather_info = get_weather(city)
            say(weather_info)

        elif "search for" in query.lower():
            webbrowser.open(f"https://www.google.com/search?q={query.split("for")[-1].strip()}")

        elif "make note" in query.lower():
            say("What Should I write Down sir?Start with the name for the note")
            note = takeCommand()
            filename = f"{note[:5].strip()}.txt"
            say(f"You can start dictating your note. say 'stop' to finish")
            content = ""
            while True:
                note_content = takeCommand()
                if "stop" in note_content.lower():
                    say("Stopping the note taking")
                    break
                elif "Some error occurred" in note_content:
                    say("I couldn't understand. Please repeat.")
                else:
                    content += f"{note_content}"
                    print(f"writing to note: {note_content}")
                    say(f"writing to note: {note_content}")

            if content:
                with open(filename, 'a') as file:
                    file.write(content)
                say(f"Note saved successfully as {filename}.")

            else:
                say("No content to save. The note has been discarded.")


        elif "read note" in query.lower():
            say("Please provide the name of the note to read.")
            note = takeCommand()
            filename = f"{note[: 5].strip()}.txt"
            if os.path.exists(filename):
                with open(filename, "r") as file:
                    say(f"Here is the content of your note")
                    content = file.readlines()

                    for line in content:
                        say(line.strip())
                        print(f"Reading...:{line}")
                        say("Say stop to Stop reading")
                        read_command = takeCommand()
                        if "stop" in read_command.lower():
                            say("Stopping the reading process.")
                            break
            else:
                say(f"Sorry, I couldn't find a note with {filename} name.")

        elif "delete note" in query.lower():
            say("Please provide the name of the note to delete.")
            note = takeCommand()
            filename = f"{note[: 5].strip()}.txt"
            if os.path.exists(filename):
                os.remove(filename)
                say(f"Note {filename} has been deleted successfully")
            else:
                say(f"Sorry, the file {filename} does not exist.")


        elif any(cmd in query.lower() for cmd in ["close", "shutdown", "stop"]):
            say("shutting down. Goodbye!!!!")
            exit()












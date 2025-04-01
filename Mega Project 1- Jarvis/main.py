import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import google.generativeai as genai
from gtts import gTTS
import pygame
import os

genai.configure(api_key="AIzaSyDp3AsBK7SO3wockzLUnT7ixhEqjw-JQbk")

recognizer = sr.Recognizer()
engine  = pyttsx3.init()
newsapi = "4332fafa45d747a7b0cc6d0cbe0f46e5"


# def speak_old(text):
#     engine.say(text)
#     engine.runAndWait()


# AI integration code
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    
    
    # mp3 play in
      # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")
    
    # end mp in play
    


def aiProcess(command):
    model = genai.GenerativeModel('models/gemini-1.5-pro')
    response = model.generate_content(command)
    return response.text
    # end AI integration
    
def processCommand(c):
   if "open google" in c.lower():
       webbrowser.open("https://www.google.com")
   elif  "open facebook" in c.lower():
       webbrowser.open("https://facebook.com")
   elif  "open youtube" in c.lower():
       webbrowser.open("https://youtube.com")
   elif  "open linkedin" in c.lower():
       webbrowser.open("https://linkedin.com")
   elif  "open instagram" in c.lower():
       webbrowser.open("https://instagram.com")
        # musicLibrary.py
   elif c.lower().startswith("play"):
    song = c.lower().replace("play", "").strip()
    link = musicLibrary.music.get(song.title())  # Capitalize the first letter of each word for exact match
    if link:
        webbrowser.open(link)
    else:
        speak(f"Sorry, I couldn't find '{song}' in the music library.")


    
   elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?q=india&apiKey={newsapi}")

        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
                
   else:
        output = aiProcess(c)
        # print(f"AI Response: {output}")
        speak(output)
 

if __name__ == "__main__":
    speak("Initializing Jarvis....")
while True:  
    # Listion for the wake word "jarvis"
    # obtain audio from the microphone
    r = sr.Recognizer()
   
        
        
    print("Recongnizing...")
   
    try:
        with sr.Microphone() as source:
           print("Listening...")
           audio = r.listen(source,  )
        word = r.recognize_google(audio)  # pylint: disable=no-member
        if(word.lower() == "jarvis"):
            speak("Har har Mhaadev")
            # listion for command
            with sr.Microphone() as source:
                print("Jarvis active...")
                audio = r.listen(source)
                command = r.recognize_google(audio)
                
                processCommand(command)
                
                
    except Exception as e: 
        print("Error; {0}".format(e))
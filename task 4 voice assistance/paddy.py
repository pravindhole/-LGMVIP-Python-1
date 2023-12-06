# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 12:00:41 2023

@author: PC-5
"""

import speech_recognition as aa  # for speech recognition library and aliasing it as 'aa'
import pyttsx3  # for  text-to-speech library
import pywhatkit  #  for performing various tasks using Python
import datetime  # e for working with dates and times
import wikipedia  #  for fetching information from Wikipedia

listener = aa.Recognizer()  # Creating a Recognizer instance from the speech recognition library
machine = pyttsx3.init()  # Initializing the text-to-speech engine

def talk(text):
    machine.say(text)   # Using the text-to-speech engine to speak the given text
    machine.runAndWait()  

def input_instruction():
    try:
        with aa.Microphone() as origin:   
            print("Listening.......")  
            speech = listener.listen(origin)  # Listening to the speech input
            instruction = listener.recognize_google(speech)   # Converting the speech input to text using Google's speech recognition
            instruction = instruction.lower()  
            if "paddy" in instruction:  
                instruction = instruction.replace('paddy',' ')  
                print(instruction)  
            return instruction  
    except aa.UnknownValueError:  # Handling unrecognized speech input error
        talk("Sorry, I couldn't understand that.")  
        return ""  
    except aa.RequestError:  # Handling request error
        talk("Sorry, there was an issue with the service.") 
        return ""  
    except Exception as e:  # Catching any other unexpected errors
        print(e)  
        talk("Sorry, there was an error.")  
        return ""  

def play_paddy():
    instruction = input_instruction()  # Calling the function to get user instructions
    print(instruction) 
    if "play" in instruction: 
        song = instruction.replace("play", "")  
        talk("playing" + song) 
        pywhatkit.playonyt(song)  # Using pywhatkit to play the requested song on YouTube
        
    

play_paddy() #start the program

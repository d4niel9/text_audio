from gtts import gTTS
import pathlib
import shutil
import sys
import pandas as pd
from datetime import datetime
from tkinter import *
from tkinter import filedialog


def menu():
    instructions =  """
    *******************************************
                CONVERT TEXT IN AUDIO
    * Instructions:
    - Select the language
    - Select option to convert text to audio
    - Choose name of the audio file
    *******************************************
    """
 
    print("{}".format(instructions))


def option_lenguage():
    lenguage_memu =  """
    *******************************************
    * Language:
    [0] Exit
    [1] Español -> es
    [2] English -> en 
    [3] Italiano -> it
    *******************************************
    """
    print("{}".format(lenguage_memu))
    option_lenguage = int(input("Option -> "))
    return option_lenguage


def option_text_input():
    text_input_menu =  """
    *******************************************
    * Text input:
    [1] Write text
    [2] Import file .txt 
    [3] Import file .csv
    *******************************************
    """
    print("{}".format(text_input_menu ))
    option_text_input = int(input("Option -> "))
    return option_text_input


def text_input():
    text_input = input("Text -> ")
    return text_input


def text_txt():
    path = filedialog.askopenfilename(title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*")))
    text_txt = ""
    with open(path, "r", encoding="utf-8") as t:
        for line in t:
            print(line)
            text_txt += line.strip("\n")
    return text_txt


def text_csv():
    path = filedialog.askopenfilename(title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.csv*"), 
                                                       ("all files", 
                                                        "*.*")))
    df = pd.read_csv(path)
    columns = df.columns
    print("{}\n".format(df))
    cont = 0
    for col in columns:
        print("[{}] {}".format(cont, col))
        cont +=1
    try:
        option_column = int(input("Option -> "))
        text_csv = df.iloc[:,option_column]
        text_csv = list(text_csv)
        return text_csv
    except ValueError:
        print("###############################################")
        print("ValueError: invalid option, try again with numeric option")
        print("###############################################")

def text_data():
    while True:
        try:
            option_text = option_text_input()
        except ValueError:
            print("###############################################")
            print("ValueError: invalid option, try again with numeric option")
            print("###############################################")
            continue

        if option_text == 1: # Write text
            text= ""
            while True:
                try:
                    text = text_input()
                    if(not(text and text.strip())):
                        raise ValueError("*Cannot enter an empty string")
                    return text
                except ValueError as ve:
                    print(ve)
                    continue

        elif option_text == 2: # Import file .txt
              text= ""
              text = text_txt()
              return text

        elif option_text == 3: # CSV
            text= ""
            text = text_csv()
            return text

        else: # Option invalid
            print("###############################################")
            print("Choose a valid option from the menu")
            print("###############################################")

def audio_name():
    while True:    
        try:
            name_audio = input("Name audio .mp3 -> ")
            if(not(name_audio and name_audio.strip())):
                raise ValueError("**Cannot enter an empty string")
            return name_audio
        except ValueError as ve:
            print(ve)
            continue


def audio_convert(LANG, TLD):
    text = text_data() # Input text
    name = audio_name() # Choose name for file
    if type(text) == str:
      now_time = str(datetime.now())
      now_time = now_time[0:22]
      name_mp3 = name + "-" + now_time
      name_mp3 += ".mp3"
      audio = gTTS(text, lang=LANG, tld=TLD) # Convert texto to audio
      print("Your text is converting...")
      audio.save(name_mp3) # Save audio file
      # Output move file
      path = pathlib.Path().absolute() # Get path
      path = str(path) + '/output/'
      shutil.move(name_mp3, path) # move file audio to output folder
      print("Save >>> " + path + name_mp3)

    if type(text) == list:
      print(text)
      cont = 1
      for word in text:
        now_time = str(datetime.now())
        now_time = now_time[0:22]
        name_mp3 = name + str(cont) + "-" + now_time
        cont += 1
        name_mp3 += ".mp3"
        audio = gTTS(word, lang=LANG, tld=TLD) # Convert texto to audio
        print("Your text '{}' is converting...".format(word))
        audio.save(name_mp3) # Save audio file
        path = './output'
        shutil.move(name_mp3, path) # move file audio to output folder
        print("Save >>> " + path + "/" + name_mp3)


def main():
    while True:
        try:
            menu()
            option = option_lenguage()
        except ValueError:
            print("###############################################")
            print("ValueError: invalid option, try again with numeric option")
            print("###############################################")
            continue

        if option == 0: # Exit program
            print("Exit...")
            quit()
        elif option == 1: # Spanish
            LANG = "es"
            TLD = "es"
            audio_convert(LANG, TLD)
        elif option ==2: # English
            LANG = "en"
            TLD = "com"
            audio_convert(LANG, TLD)
        elif option == 3: # Italian
            LANG = "it"
            TLD = "it"
            audio_convert(LANG, TLD)
        else: # Option invalid
            print("###############################################")
            print("Choose a valid option from the menu")
            print("###############################################")


def run():
    try:
        main()
    except KeyboardInterrupt as keyin:
        print("\n" + str(keyin))
        sys.exit()

if __name__ == "__main__":
    run()

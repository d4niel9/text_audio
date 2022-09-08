from gtts import gTTS
import pathlib
import shutil
import sys



def option_menu():
    instructions =  """
    *******************************************
                CONVERT TEXT IN AUDIO
    * Instructions:
    - Select the language
    - Write text you want to convert
    - Choose name of the audio file
    *******************************************
    """

    lenguage =  """
    *******************************************
    * Language:
    [0] Exit
    [1] Español -> es
    [2] English -> en 
    [3] Italiano -> it
    *******************************************
    """

    print(instructions)
    print(lenguage)
    option = int(input("Option -> "))
    return option


def text_input():
    while True:
        try:
            text = text = input("Convert text -> ")
            print (end= "")
            if(not(text and text.strip())):
                raise ValueError("*Cannot enter an empty string")
            return text
        except ValueError as ve:
            print(ve)
            continue


def audio_name():
    while True:    
        try:
            name_audio = input("Name audio .mp3 -> ")
            print (end= "")
            if(not(name_audio and name_audio.strip())):
                raise ValueError("**Cannot enter an empty string")
            return name_audio
        except ValueError as ve:
            print(ve)
            continue


def audio_convert(LANG, TLD):
    text = text_input() # Input text
    name_mp3 = audio_name() # Choose name file
    name_mp3 += ".mp3"
    audio = gTTS(text, lang=LANG, tld=TLD) # Convert texto to audio
    print("Your text is converting...")
    audio.save(name_mp3) # Save audio file

    # Output move file
    path = pathlib.Path().absolute() # Get path
    path = str(path) + '/output/'
    shutil.move(name_mp3, path) # move file audio to output folder
    print("Save >>> " + path)


def main():
    while True:
        try:
            option = option_menu()
        except ValueError:
            print("###############################################")
            print("ValueError: invalid option, try again with numeric option")
            print("###############################################")
            continue

        if option == 0: # Exit program
            print("Exit...")
            break
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
    except KeyboardInterrupt:
        print("\n Ciao")
        sys.exit()

if __name__ == "__main__":
    run()
    
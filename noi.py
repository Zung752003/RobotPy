import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
# import input

friday = pyttsx3.init()
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[1].id)


def speak(audio):
    print('F.R.I.D.A.Y:' + audio)
    friday.say(audio)
    friday.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I: %M : %p")
    speak(Time)


def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak("Good Morning sir")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon sir")
    elif hour >= 18 and hour <= 24:
        speak("Good night sir")
    speak('How can i help you')
    


def PyRobot_Nghe():
    nghe = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Adjusting noise")
        nghe.adjust_for_ambient_noise(source, duration= 1)
        print("Recording for 4 seconds")
        recorded_audio = nghe.listen(source,timeout = 4)
        print("Done recording")
    # try:
    #     print("Convert speech to text")
    #     your_text = nghe.recognize_google(recorded_audio, language = "vi")
    #     print(" --Python convert speech to text:", your_text)
    # except:
    #     your_text = "sorry, i can't hear you"
    #     print("--PyRobot:",your_text)
    # return your_text
        # nghe.pause_threshold = 5
        # recorded_audio = nghe.listen(source)
    try:
        your_text = nghe.recognize_google( recorded_audio, language='en')
        print("Tony Chung:",your_text)
    except sr.UnknownValueError:
        print("please report or typing the command")
        your_text = input("Your order is:")
    return your_text
    
if __name__ == "__main__":
    welcome()
    while True:
        your_text = PyRobot_Nghe().lower()
        if "google" in your_text:
            speak("What should i search boss")
            search = input("What do you want to search for on Google? ")
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'here is your  {search}  on Google')



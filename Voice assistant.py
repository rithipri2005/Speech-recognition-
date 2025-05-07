import speech_recognition as sr
import pyttsx3
import datetime
# Initialize the speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# Select female voice
def speak(text):
    """Speaks the given text."""
    engine.say(text)
    engine.runAndWait()
def listen():
    """Listens for user input and returns it as a string."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query
def process_command(query):
    """Processes the user's command and performs actions."""
    query = query.lower()
 if 'time' in query:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {current_time}")
    elif 'date' in query:
         current_date = datetime.datetime.now().strftime("%Y-%m-%d")
         speak(f"The date is {current_date}")
    elif 'hello' in query:
        speak("Hello! How can I help you?")
    elif 'stop' in query:
        speak("Goodbye!")
        return True
    else:
        speak("I can't understand that, please try again.")
    return False
if __name__ == "__main__":
    speak("Initializing the voice assistant...")
    while True:
        query = listen()
        if query != "None":
            if process_command(query):
                break

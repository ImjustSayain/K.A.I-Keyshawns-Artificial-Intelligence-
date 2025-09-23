import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
from random import choice
import time  # Added for delays
import win32com.client

# Initialize Windows speech
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def windows_speak(audio):
    """Convert text to speech using Windows built-in"""
    print(f"K.A.I: {audio}")
    speaker.Speak(audio)
    time.sleep(0.5)  # Small delay between speeches

def get_time():
    """Speak the current time"""
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    windows_speak(f"The current time is {current_time}")

def get_date():
    """Speak today's date"""
    today = datetime.datetime.now()
    windows_speak(f"Today's date is {today.strftime('%A, %B %d, %Y')}")

def get_news():
    """Get latest news headlines"""
    windows_speak("Fetching the latest news headlines")
    webbrowser.open("https://news.google.com")
    windows_speak("I've opened Google News in your browser")

def search_wikipedia(query):
    """Search Wikipedia"""
    try:
        search_query = query.replace("wikipedia", "").replace("search", "").replace("look up", "").strip()
        if not search_query:
            windows_speak("What would you like me to search on Wikipedia?")
            return
        
        windows_speak(f"Searching Wikipedia for {search_query}")
        results = wikipedia.summary(search_query, sentences=2)
        windows_speak("According to Wikipedia")
        windows_speak(results)
    except wikipedia.exceptions.DisambiguationError:
        windows_speak("There are multiple results for that topic. Please be more specific.")
    except wikipedia.exceptions.PageError:
        windows_speak("Sorry, I couldn't find any information on that topic.")
    except Exception as e:
        windows_speak("Sorry, I encountered an error while searching.")

def open_website(website):
    """Open specific websites"""
    websites = {
        'google': 'https://www.google.com',
        'youtube': 'https://www.youtube.com',
        'github': 'https://www.github.com'
    }
    
    if website in websites:
        webbrowser.open(websites[website])
        windows_speak(f"Opening {website}")
    else:
        windows_speak(f"I don't know how to open {website}")

def wish_me():
    """Greet the user based on time of day"""
    windows_speak("Systems now online and operational")
    
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        windows_speak("Good Morning Sir")
    elif 12 <= hour < 18:
        windows_speak("Good Afternoon Sir")
    elif 18 <= hour < 24:
        windows_speak("Good Evening Sir")
    else:
        windows_speak("Good Night Sir")
    
    windows_speak("KAI at your service. All systems are ready for your commands")

def take_command():
    """Take microphone input and return text output"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n" + "="*50)
        print("K.A.I is listening...")
        recognizer.pause_threshold = 1
        recognizer.energy_threshold = 300
        
        try:
            print("Speak now...")
            audio = recognizer.listen(source, timeout=10)
        except sr.WaitTimeoutError:
            print("No speech detected")
            return "none"

    try:
        print("Processing your command...")    
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"USER: {query}")
        return query.lower()

    except sr.UnknownValueError:
        windows_speak("I didn't catch that. Could you please repeat?")
        return "none"
    except sr.RequestError:
        windows_speak("There's an issue with speech recognition. Please check your microphone.")
        return "none"
    except Exception as e:
        windows_speak("An error occurred while processing your command.")
        return "none"

# Main program execution
if __name__ == "__main__":
    print("=== K.A.I SYSTEM BOOTUP ===")
    
    # SPEAK ALL BOOT MESSAGES WITH PROPER DELAYS
    windows_speak("Initializing Knowledgeable Artificial Intelligence")
    time.sleep(1)  # 1 second delay
    windows_speak("Loading all core systems and memory modules")
    time.sleep(1)  # 1 second delay
    windows_speak("Boot sequence complete")
    time.sleep(1)  # 1 second delay
    
    # Automatic greetings and information
    windows_speak("Starting system status report")
    time.sleep(0.5)
    get_time()
    time.sleep(0.5)
    get_date()
    time.sleep(0.5)
    wish_me()
    
    windows_speak("I am now ready for voice commands")
    
    # Main command loop
    while True:
        query = take_command()
        
        if query == "none":
            continue
            
        # Process commands
        if 'time' in query:
            get_time()
            
        elif 'date' in query:
            get_date()
            
        elif 'news' in query:
            get_news()
            
        elif 'wikipedia' in query:
            search_wikipedia(query)
            
        elif 'open google' in query:
            open_website('google')
            
        elif 'open youtube' in query:
            open_website('youtube')
            
        elif 'hello' in query or 'hi kai' in query:
            windows_speak("Hello Sir! How can I assist you today?")
            
        elif 'how are you' in query:
            windows_speak("I'm functioning perfectly, thank you for asking Sir")
            
        elif 'your name' in query:
            windows_speak("I am K A I, your Knowledgeable Artificial Intelligence assistant")
            
        elif 'thank you' in query:
            windows_speak("You're welcome Sir")
            
        elif 'exit' in query or 'goodbye' in query or 'shutdown' in query:
            windows_speak("Shutting down all systems. Goodbye Sir!")
            break
            
        else:
            windows_speak("I heard you say: " + query)
            windows_speak("Try saying 'time', 'date', 'news', or 'open google'")

    print("K.A.I system shutdown complete")
import pyttsx3
import re
import webbrowser  # Import the webbrowser module

# Initialize the pyttsx3 engine for text-to-speech
engine = pyttsx3.init('sapi5')

# Get the available voices and set the first voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Function to speak the given text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()  # This command is necessary to produce audible speech

# Pairs of patterns and responses
pairs = [
    [r"(.*)my name is (.*)", ["Hello {1}, How are you today?"]],
    [r"(.*)help(.*)", ["I can help you!"]],
    [r"(.*) your name ?", ["My name is thecleverprogrammer, but you can just call me robot."]],
    [r"how are you (.*) ?", ["I'm doing very well!", "I am great!"]],
    [r"sorry (.*)", ["It's alright", "It's OK, never mind that"]],
    [r"i'm (.*) (good|well|okay|ok)", ["Nice to hear that!", "Alright, great!"]],
    [r"(hi|hey|hello|hola|holla)(.*)", ["Hello", "Hey there"]],
    [r"what (.*) want ?", ["Make me an offer I can't refuse"]],
    [r"(.*)created(.*)", ["Aman Kharwal created me using Python's NLTK library", "Top secret ;)"]],
    [r"(.*) (location|city) ?", ["New Delhi, India"]],
    [r"(.*)raining in (.*)", ["No rain in the past 4 days here in {1}", "In {1} there is a 50% chance of rain"]],
    [r"how (.*) health (.*)", ["Health is very important, but I am a computer, so I don't need to worry about my health"]],
    [r"(.*)(sports|game|sport)(.*)", ["I'm a very big fan of Cricket"]],
    [r"who (.*) (Cricketer|Batsman)?", ["Virat Kohli"]],
    [r"quit", ["Bye for now. See you soon :)", "It was nice talking to you. See you soon :)"]],
    [r"(.*)", ["That is nice to hear"]]
]

# Function to process user input and find matching response
def respond(user_input):
    # Check if the user input contains the phrase 'open google'
    if 'open google' in user_input.lower():
        webbrowser.open("https://www.google.com")  # Open Google in the browser
        speak("Opening Google now.")
        return "Opening Google now."

    # Check if the user input contains the phrase 'open youtube'
    elif 'open youtube' in user_input.lower():
        webbrowser.open("https://www.youtube.com")  # Open YouTube in the browser
        speak("Opening YouTube now.")
        return "Opening YouTube now."
    
    # Check if the user input contains the phrase 'open linkedin'
    elif 'open linkedin' in user_input.lower():
        webbrowser.open("https://www.linkedin.com")  # Open LinkedIn in the browser
        speak("Opening LinkedIn now.")
        return "Opening LinkedIn now."
    
    # Check if the user input contains the phrase 'open IGDTUW'
    elif 'open igdtuw' in user_input.lower():
        webbrowser.open("https://www.igdtuw.ac.in/")  # Open IGDTUW website in the browser
        speak("Opening IGDTUW website now.")
        return "Opening IGDTUW website now."

    # Loop through each pair of pattern and response
    for pattern, responses in pairs:
        match = re.search(pattern, user_input)  # Use re.search instead of re.match
        if match:
            try:
                # If there are groups in the match, format the response accordingly
                if match.groups():
                    response = responses[0].format(*match.groups())  # Use .format instead of % formatting
                else:
                    response = responses[0]  # No formatting needed
                return response
            except IndexError:
                # If there's a formatting error, just return the response as is
                return responses[0]
            except TypeError:
                # Handle cases where the number of groups doesn't match
                return "Oops! Something went wrong with my response."
    return "Sorry, I don't understand that."  # Default response if no match is found

# Main function
if __name__ == "__main__":
    speak("Hello, I am your chatbot. How can I assist you today?")
    
    while True:
        user_input = input("You: ")  # Allow the user to type their input
        if user_input.lower() == 'quit':  # Check if the user wants to quit the conversation
            speak("Bye for now. See you soon :)")
            print("Bot: Bye for now. See you soon :)")
            break
        
        # Get response from the chatbot
        response = respond(user_input)
        
        # Speak the response
        speak(response)
        
        # Print the response to the console
        print(f"Bot: {response}")

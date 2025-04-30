import random as rd
import pyttsx3

# Speak function that will speak
def speak(text):
    print("Gamer:", text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# Generate random number
e = rd.randint(1, 100)

# Ask how many chances the user wants
speak("How many chances do you want?")
try:
    f = int(input("How many chances do you want: "))
except ValueError:
    speak("Invalid input for chances. Exiting the game.")
    exit()

# Ask user whether to start or exit
speak("Insert 1 to start the game and 2 to exit.")
try:
    d = int(input("Enter your choice: "))
except ValueError:
    speak("Invalid input. Exiting the game.")
    exit()

if d == 1:
    speak("The computer has successfully guessed the number.")
    speak("Let's start the game!")
    
    for i in range(f):
        try:
            a = int(input(f"Attempt {i+1} - Enter your guess: "))
            if a == e:
                speak("Good job! You guessed the correct number.")
                break
            elif a > e:
                speak("You chose a greater number. Try a lower one.")
            elif a < e:
                speak("You chose a smaller number. Try a higher one.")
        except ValueError:
            speak("Invalid input. Please enter a valid number.")
            break
    else:
        speak(f"Sorry, you've used all your chances. The correct number was {e}.")
else:
    speak("You have completely exited the game.")

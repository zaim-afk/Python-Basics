import time  #Adding delays
import random  #Generating random choices
import sys  #Allow the program to exit when conditions are met

#Function to simulate typing effect on the screen
def slow_typing(text, rate):
    for char in text:
        print(char, end='', flush=True)  #Print each character without a newline
        time.sleep(rate)  #Pause for the specified time between characters
    print()  #Move to the next line after the loop finishes

#Function to pause the game until the user presses Enter
def pause(text):
    input(text + ' [Enter]')  #Displays a message and waits for input

madlibs = []
#Function to collect input for Mad Libs with validation to avoid empty input
def mad_add(text):
    while True:
        user_input = input(text).strip()  #Collect and strip unnecessary spaces
        if user_input:  #Ensure the input is not empty
            madlibs.append(user_input)  #Add valid input to the madlibs list
            break
        else:
            print("Input cannot be empty. Please try again.")  #Prompt again

#Function to ensure an empty input is not provided
def no_empty_input(input_prompt, second_prompt):
    value = input(input_prompt).strip().lower()  #Prompt for input and convert to lowercase
    while True:
        if value == '':  #If input is empty, ask again
            value = input(second_prompt).strip().lower()
        else:
            return value  #Return valid input

#Function to ensure a valid option is selected
def check_valid_input(first_prompt, second_prompt, valid_options):
    choice = input(first_prompt).strip().lower()  #Collect input and strip spaces
    while True:
        if choice in valid_options:  #If input is valid, break the loop
            break
        else:
            choice = input(second_prompt).strip().lower()  #Re-prompt for valid input
    return choice

#Function to simulate a 50/50 chance of returning "yes" or "no"
def fifty_fifty_chance():
    number = random.randint(1, 100)  #Generate a random number between 1 and 100
    if number % 2 == 0:  #Even numbers represent "yes"
        return "yes"
    else:  #Odd numbers represent "no"
        return "no"

# Function to check player stats and handle game over conditions
def check_stats():
    if stats['health'] <= 30:  #Health too low
        print("oh no,")
        time.sleep(1)
        print(f"Your health has dropped too much.")
        time.sleep(1)
        slow_typing(". . .", 0.5)
        time.sleep(1)
        print("*THUD*")
        time.sleep(1)
        slow_typing("*You fainted!*", 0.06)
        time.sleep(1)
        pause("An ambulance arrives and you're rushed to the hospital.")
        time.sleep(2)
        print("You can't continue going to school in this state.")
        sys.exit("<Game Over>")  # Ends the program
    if stats['safety'] <= 30:  #Safety too low
        print("oh no,")
        time.sleep(1)
        pause(f"Your safety dropped too low.")
        time.sleep(1)
        slow_typing(". . .", 0.5)
        time.sleep(1)
        pause("*You are now extremely vulnerable to monster attacks*")
        print("It's too dangerous to continue the game.")
        sys.exit("<Game Over>")
    if stats['academics'] <= 15:  #Academics too low
        print("oh no,")
        time.sleep(1)
        pause(f"Your academics have dropped too much.")
        time.sleep(1)
        slow_typing(". . .", 0.5)
        time.sleep(1)
        print("Unfortunately, you're forced to drop out of Year 11.")
        sys.exit("<Game Over>")

#Initial player stats
stats = {'health': 80, 'safety': 50, 'academics': 30, 'social': 50}

#List of possible classmates
classmates = ['Adam', 'Laila', 'Kimi', 'Alara', 'Dave', 'Jake']

#List of classes and teachers
classes = [
    'Physics with br Rizwan',
    'Chemistry with br James',
    'Methods with sr Meenu',
    'English with sr Jamila',
    'Computer Science with br Zaim',
    'Sports with miss Fee'
]

#List of teachers
teachers = ['br Rizwan', 'br James', 'sr Meenu', 'sr Jamila', 'br Zaim', 'sr Dina']

#Mapping of classes to their respective teachers
teacher_of_class = {
    'Physics with br Rizwan': 'br Rizwan',
    'Chemistry with br James': 'br James',
    'Methods with sr Meenu': 'sr Meenu',
    'English with sr Jamila': 'sr Jamila',
    'Computer Science with br Zaim': 'br Zaim',
    'Sports with miss Fee': 'miss Fee'
}


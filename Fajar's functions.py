import time
import random

def slow_typing(text):
    for char in text:
        print(char, end='', flush=True)  # Print each character on the same line
        time.sleep(0.08)  # Pause for 0.08 seconds
    print()  # Move to the next line after the loop
    
def pause(text):
    input(text + ' [Enter]')
    
madlibs = []
def mad_add(text):
    madlibs.append(input(text))

def no_empty_input(input_prompt, second_prompt):
    value = input(input_prompt).strip().lower()
    while True:
        if value == '':
            value = input(second_prompt).strip().lower()
        else:
            return value
        
def check_valid_input(first_prompt, second_prompt, valid_options):
    choice = input(first_prompt).strip().lower()
    while True:
        if choice in valid_options:
            break
        else:
            choice = input(second_prompt).strip().lower()
    return choice

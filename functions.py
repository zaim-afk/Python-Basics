
import time
import random

def slow_typing(text, rate):
    for char in text:
        print(char, end='', flush=True)  # Print each character on the same line
        time.sleep(rate)  # Pause for 0.08 seconds
    print()  # Move to the next line after the loop
    
def check_stats():
    if stats['health'] > 10:
        print

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

stats = {'health':80, 'safety':50, 'academics':30, 'social':50 }
classmates = ['Adam', 'Laila', 'Kimi', 'Alara', 'Dave', 'Jake']
classes = [
    'Physics with br Rizwan',
    'Chemistry with br James',
    'Methods with sr Meenu',
    'English with sr Jamila',
    'Computer Science with br Zaim',
    'Sports with miss Fee']
teachers = ['br Rizwan', 'br James', 'sr Meenu', 'sr Jamila', 'br Zaim', 'sr Dina']
teacher_of_class = {
    'Physics with br Rizwan':'br Rizwan',
    'Chemistry with br James':'br James',
    'Methods with sr Meenu':'sr Meenu',
    'English with sr Jamila':'sr Jamila',
    'Computer Science with br Zaim':'br Zaim',
    'Politics and Law with sr Dina':'sr Dina'}


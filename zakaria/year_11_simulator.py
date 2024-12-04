import random
import time
import os
import simulator_functions
from simulator_functions import attributes, teachers, suspensions, term


gender = simulator_functions.gender_check()
name = simulator_functions.choose_name()
time.sleep(0.5)
simulator_functions.cl_s()
time.sleep(0.5)
print(f"You are {name}. You are a Year 11 student at A.I.C. Kewdale.")
simulator_functions.slow_text("This game will have you play through Year 11, facing all the challenges and dealing with all the obstacles. During this game, you will be faced with options, and every choice you make affects your game. Beware, if your attributes go too low, you will lose.", 0.025)
print()
simulator_functions.slow_text(f"These are the attributes you have to watch out for:\nGrades (currently at {attributes['grades']})\nEnergy (currently at {attributes['energy']})\nFun (currently at {attributes['fun']})\nSocial (currently at {attributes['social']}\nTrouble (currently at {attributes['trouble']}. This is the one attribute that you have to try to keep as low as possible)", 0.025)
print()
print()
time.sleep(0.8)
for line in ["The subjects you take are ", "English, ", "Mathematics, ", "Science, ", "Physical Education Studies, and", "Computer Science."]:
    simulator_functions.slow_text(line, 0.03)
    print()
print()

simulator_functions.select_teachers()
time.sleep(1)

for line in ["Your teachers are", f"English: {teachers['english']}", f"Maths: {teachers['maths']}", f"Science: {teachers['science']}", f"Sports: {teachers['sports']}", f"Computer Science: {teachers['compsci']}"]:
    simulator_functions.slow_text(line, 0.02)
    print()
if teachers['compsci'] == 'Br Nahian':
    print("Lucky! You got the best and smartest teacher in the whole school for Computer Science!")
time.sleep(1)

simulator_functions.cl_s()

time.sleep(0.5)
simulator_functions.first_morning_feelings()

simulator_functions.cl_s()

time.sleep(0.5)
simulator_functions.breakfast_choice()
print()

simulator_functions.cl_s()


time.sleep(1)
print("You arrive at school.")
person, person_choice, principal = simulator_functions.first_person()
print()
simulator_functions.cl_s()
time.sleep(1)

if principal == True:
    for line in ["The teacher walks you to the principal's office.", "You enter and have a seat.", 'The principal looks up at you. "What were you thinking, punching poor Adam like that?']:
        simulator_functions.slow_text(line, 0.2)
        print()
    simulator_functions.principal_office()
    simulator_functions.attributes_check()
    simulator_functions.cl_s()


for line in ["You check your timetable, and see you have Maths first.", "Do you choose to go to Maths, or skip the class?"]:
    simulator_functions.slow_text(line, 0.05)
    print()
    time.sleep(0.2)
choice = ''
while choice != '1' and choice != '2':
    choice = input("(1) Go to class\n(2) Skip class\n").strip().lower()
if choice == '1':
    simulator_functions.slow_text("You decide to go to class.", 0.05)
    print()
    attributes['grades'] += 20
    time.sleep(0.2)
    print(f"Your grades increased! It is now at {attributes['grades']}.")
elif choice == '2':
    simulator_functions.slow_text("You decide to skip class.", 0.05)
    attributes['grades'] -= 20
    print()
    time.sleep(0.2)
    print(f"Your grades decreased! It is now at {attributes['grades']}.")
    simulator_functions.skip_class()
simulator_functions.attributes_check()

print()
simulator_functions.cl_s()
time.sleep(1)


simulator_functions.slow_text("You continued going to school for the next few weeks, and luckily, no incidents happened.", 0.05)
print()
time.sleep(2)
simulator_functions.slow_text("Then, in Week 4, it was announced that Year 11 students would be performing their mid-term tests the next week.", 0.05)
print()
simulator_functions.weekend()
print()

simulator_functions.cl_s()
simulator_functions.test()
simulator_functions.cl_s()


simulator_functions.term_report()
simulator_functions.cl_s()

time.sleep(2)
simulator_functions.new_term()
simulator_functions.cl_s()

simulator_functions.slow_text("Year 11's are told that they're going on an excursion this term. 🥳🥳", 0.1)
print()
simulator_functions.excursion()
simulator_functions.cl_s()


simulator_functions.slow_text("It is announced that Semester exams would be taking place at the end of the term for all Year 11s.", 0.1)
print()
simulator_functions.weekend()

simulator_functions.slow_text("It is Week 6, and you realise you aren't doing so well in English. You look at your timetable, and, coincidentally (or not), you have English.", 0.05)
print()
simulator_functions.slow_text("Do you choose to go to English class, or skip it?", 0.05)
choice = input("(1) Go to class\n(2) Skip class\n")
while choice != '1' and choice != '2':
    choice = input("I said choose 1 or 2 ")
if choice == '1':
    simulator_functions.slow_text("You decide to go to class.", 0.05)
    print()
    attributes['grades'] += 20
    time.sleep(0.2)
    print(f"Your grades increased! It is now at {attributes['grades']}.")
elif choice == '2':
    simulator_functions.slow_text("You decide to skip class.", 0.05)
    attributes['grades'] -= 20
    print()
    time.sleep(0.2)
    print(f"Your grades decreased! It is now at {attributes['grades']}.")
    simulator_functions.skip_class()
simulator_functions.attributes_check()

simulator_functions.cl_s()
simulator_functions.weekend()
simulator_functions.cl_s()


simulator_functions.slow_text("It is now semester exams. You start doing the test.", 0.05)
simulator_functions.test()
simulator_functions.cl_s()

simulator_functions.term_report()
simulator_functions.cl_s()

time.sleep(2)
simulator_functions.new_term()
simulator_functions.cl_s()

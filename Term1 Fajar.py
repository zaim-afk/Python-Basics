import time

def slow_typing(text):
    for char in text:
        print(char, end='', flush=True)  # Print each character on the same line
        time.sleep(0.08)  # Pause for 0.08 seconds
    print()  # Move to the next line after the loop
def pause(text):
    input(text + ' [Enter]')
    return
def no_empty_input(input_prompt, second_prompt):
    value = input(input_prompt).strip().lower()
    while True:
        if value == '':
            value = input(second_prompt).strip().lower()
        else:
            return value
def check_valid_input(input_prompt, second_prompt, valid_options=None):
    while True:
        value = input(input_prompt).strip().lower()
        if valid_options and value not in valid_options:
            value = input(second_prompt).strip().lower()
        elif not value:  # Handle empty input
            value = input(second_prompt).strip().lower()
        else:
            return value

stats = {'health':80, 'safety':50, 'academics':30, 'social':50 }
valid_options = ['yes', 'no', 'a', 'b', 'im sure', 'fine, ill pack', 'run', 'stay', 'i guess', 'how']
inventory = {'books':1, 'weapon':1}

name = no_empty_input("Enter your name:", "Please enter a name:")

print(f'''
                        -------------------------------
                        ~~ Welcome {name} 
                        -------------------------------
    In this text based adventure game, your aim is to make it to the end of
    year 11 alive...

Current stats:
Health: 80
Academics: 30
Social: 50
Safety: 50
----------------------------------------------------------------------------''')

time.sleep(8)

print(f'Good morning {name}, today is your first day of year 11!')
time.sleep(3)

choice = check_valid_input("Are you excited? (yes/no)", "Just a reminder to choose from the options provided :)\nAre you excited? (yes/no)")    
while True:
    if choice == 'yes':
        print("Well then, let's get ready for school!")
        stats['academics'] += 1
        break
    elif choice == "no":
        slow_typing('. . .')
        time.sleep(1)
        print('Well you have to get ready anyway :\ ')
        stats['academics'] -= 1
        break
    else:
        choice = input("Just a reminder to choose from the options provided :)\nAre you excited? (yes/no)")
        
        
            
time.sleep(3)
print("\nAre you gonna put your books in your bag?\na)Why would I? its the first day, no one does work.\nb)Yeah, i'll get to it.")
choice_books = no_empty_input("(choose a or b)", "(please choose a or b)")
while True:
    if choice_books == 'b':
        slow_typing('*you packed your bag, good job!*')
        stats['academics'] += 1
        break
    elif choice_books == 'a':
        slow_typing('. . .')
        time.sleep(1)
        print("This is your game so whatever you want i guess.")
        time.sleep(2)
        choice_books = input("You sure?  (im sure/fine, ill pack)").strip().lower()
        if choice_books == 'im sure':
            print("alright then.")
            stats['academics'] -= 2
            break
        elif choice_books == 'fine, ill pack':
            print("Good choice.")
            stats['academics'] += 2
            break
        else:
            choice_books = input("Choose one of the options please
    else:
        choice_books = input("(please choose a or b)")

time.sleep(3)
print("----------------------------------------------------------------------------")
slow_typing('*After that, you get going to school*')
time .sleep(1)
choice = input("Hey, since we have some time right now, some rules:\n[press Enter]")
pause("Throughout the game, only type what's written in ( / ) or [] as your responses. If there are no options, don't type anything.")
pause("You have stats in the game as you saw at the start. Every choice you make affects them, so make sure to choose wisely. Rememeber, your goal is to survive till the end.")
slow_typing('*The wind picks up, you hear a crow in the distance*')
time.sleep(2)
pause("I really hope your day goes well today, and none of *those* guys come.")
slow_typing('. . .')
print("What guys am i talking about? You know! th-them -->")
time.sleep(3)
print('''
                                   𓌹  𓌺
      ¯\༼ ༎ຶ ෴ ༎ຶ༽/¯     {¬ºཀ°}¬  (꒪ཀ꒪)
       ༼   _ ¯ -   ༽       ||       {-}
      ༼  ¯  - _  ¯  ༽  	  / \      ||
      ''')
time.sleep(2)
print("RUNNN!!!!")
time.sleep(2)
choice = no_empty_input("[run] or [stay]", "Chose one of the options dude, quickly!\n[run] or [stay]")
while True:
    if choice == 'stay':
        print("What are you doing? They're gonna get you! Get away!")
        time.sleep(1)
        choice = no_empty_input("[run] or [stay]", '[run] or [stay]!')        
        if choice == 'run':
            slow_typing('*You chose to run*')
            pause("What on earth were you thinking!")
            slow_typing('*Your heart rate increases.',end='')
            time.sleep(1)
            print('What were those things?!*')
            time.sleep(2)
            pause(slow_typing("*You run all the way to school without looking back*"))
            stats['health'] -= 5
            break
        elif choice == 'stay':
            slow_typing('. . .')
            choice = input("What are you gonna do then? Fight? \n[i guess] or [how]").strip().lower()
            if choice == 'how':
                time.sleep(1)
                slow_typing('. . .')
                time.sleep(1)
                print("You're screwed dude\n")
                time.sleep(2)
                print('''
      ¯\༼ ༎ຶ ෴ ༎ຶ༽/¯ RAAAA!
       ༼   _ ¯ -   ༽ 
      ༼  ¯  - _  ¯  ༽''')
                time.sleep(2)
                print("\n*squash*")
                time.sleep(1)
                print('\n*smack*')
                time.sleep(1)
                print('\n*squelch*')
                time.sleep(2)
                slow_typing('*you were crushed by the monster*')
                pause("If you were gonna stay, you could have atleast tried to fight back :/ ")
                stats['health'] -=15
                break
            elif choice == 'i guess':
                time.sleep(1)
                print("You're screwed dude\n")
                time.sleep(1)
                slow_typing('*you chose to fight*')
                time.sleep(1)
                print("You dont know how to fight yet!")
                time.sleep(3)
                print('''
      ¯\༼ ༎ຶ ෴ ༎ຶ༽/¯ RAAAA!
       ༼   _ ¯ -   ༽ 
      ༼  ¯  - _  ¯  ༽''')
                time.sleep(2)
                print("\n*squash*")
                time.sleep(1)
                print('\n*smack*')
                time.sleep(1)
                print('\n*squelch*')
                time.sleep(2)
                pause("*you tried fighting the monster, but you couldn't, and you were crushed.*")
                time.sleep(2)
                pause("Well that was dumb.")
                stats['health'] -=10
                stats['safety'] +=5
                break
            else:
                slow_typing("*You didn't choose a valid option fast enough and ended up just standing where you were.*")
                slow_typing('. . .')
                time.sleep(1)
                print("You're screwed dude\n")
                time.sleep(2)
                print('''
      ¯\༼ ༎ຶ ෴ ༎ຶ༽/¯ RAAAA!
       ༼   _ ¯ -   ༽ 
      ༼  ¯  - _  ¯  ༽''')
                time.sleep(2)
                print("\n*squash*")
                time.sleep(1)
                print('\n*smack*')
                time.sleep(1)
                print('\n*squelch*')
                time.sleep(2)
                slow_typing('*you were crushed by the monster*')
                pause("next time, type one of the options!")
                stats['health'] -=15
                break
        else:
            choice = input('[run] or [stay]!')
    if choice == 'run':
        slow_typing('*You chose to run*')
        time.sleep(1)
        pause("Thankgoodness! Why on earth would you choose to stay?")
        stats['safety'] -= 8
        break
    else:
        choice = input("Chose one of the options dude, quickly! \n[run] or [stay]")


print("----------------------------------------------------------------------------")
slow_typing('*you finally get to school*')
time.sleep(1)
print("Let's hope the rest of your day goes easier")

time.sleep(3)
pause("\n*You walk into the familiar building and head to your coordinators office. You collect your timetable. Your first class is Physics with Br.James. Lets go!*")
print("\n*BRINNGGGG!!")
time.sleep(2)
pause("*The bell goes just as you walk in. Suddenly your teacher looks at you*") 
if choice_books == 'b':
    pause(f"Br James: {name}!, come sit down!")
    stats['social'] += 2
    slow_typing("*Since you brought your books, you had a productive lesson*")
    time.sleep(3)
    pause("The rest of your day went amazing. You met alot of your friends, and you enjoyed most of your classes.")
elif choice_books == 'fine, ill pack':
    pause(f"Br James: {name}!, come sit down!")
    stats['social'] += 2
    slow_typing("*Since you brought your books, you had a productive lesson*")
    time.sleep(3)
    pause("The rest of your day went amazing. You met alot of your friends, and you enjoyed most of your classes.")
else:
    print(f"\nBr James: {name}, why are you walking in empty handed, where are your books?")
    time.sleep(4)
    print(f"{name}: I didn't think we'd need them today.")
    time.sleep(3)
    slow_typing("*Br James was very disapointed with you and gave you a negative*")
    time.sleep(1)
    pause("Looks like you messed up dude.")
    stats['academics'] -= 3
    time.sleep(3)
    pause("The rest of your day was pretty bad. You got in trouble again for not bringing your books, and you had detention at lunch.")
    stats['social'] -=3
    
time.sleep(2)
print("----------------------------------------------------------------------------")
slow_typing("*After a long, tiring day at school, you finally head home.")
pause()
pause("You kick off your shoes, throw your bag on your chair and plop onto your bed.")
pause("You think to yourself, 'Will every day of year 11 be like this?'")

print("----------------------------------------------------------------------------")
slow_typing("9 Weeks later...",)
time.sleep(2)
pause("*Lets find out how the rest of your term went*")
print("----------------------")
madlibs = []
madlibs.append(input("Insert a Subject:"))
madlibs.append(input("Something you do with your mates:"))
madlibs.append(input("A friends name:"))
madlibs.append(input("Another:"))
madlibs.append(input("Adjective:"))
madlibs.append(input("Piece of stationary:"))
madlibs.append(input("Preposition:"))
madlibs.append(input("Plural noun:"))
slow_typing("processing...")
time.sleep(1)
pause("Everyday you would look forward to {0}. On the weekends you enjoyed {1} with {2} and {3}. Studying was {4}. Once, you even lost your {5} {6} some {7} XD.".format(*madlibs))



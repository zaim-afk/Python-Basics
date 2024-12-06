from functions import *

stats = {'health':80, 'safety':50, 'academics':30, 'social':50 }
classes = [
    'Physics with br Rizwan',
    'Chemistry with br James',
    'Methods with sr Meenu',
    'English with sr Jamila',
    'Computer Science with br Zaim',
    'Sports with miss Fee']
teacher_of_class = {
    'Physics with br Rizwan':'br Rizwan',
    'Chemistry with br James':'br James',
    'Methods with sr Meenu':'sr Meenu',
    'English with sr Jamila':'sr Jamila',
    'Computer Science with br Zaim':'br Zaim',
    'Sports with miss Fee':'miss Fee'}

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

time.sleep(1)

print(f'Good morning {name}, today is your first day of year 11!')
time.sleep(3)
choice = check_valid_input("Are you excited? (yes/no)", "Just a reminder to choose from the options provided :)\nAre you excited? (yes/no)", ['yes','no'])    
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
choice_books = check_valid_input("(choose a or b)", "(please choose a or b)", ['a','b'])
while True:
    if choice_books == 'b':
        slow_typing('*you packed your bag, good job!*')
        stats['academics'] += 1
        break
    else:
        slow_typing('. . .')
        time.sleep(1)
        print("This is your game so whatever you want i guess.")
        time.sleep(2)
        choice_books = check_valid_input("You sure?  (im sure/fine, ill pack)", "Choose one of the options please", ['im sure','fine, ill pack']).strip().lower()
        if choice_books == 'im sure':
            print("alright then.")
            stats['academics'] -= 2
            break
        else:
            print("Good choice.")
            stats['academics'] += 2
            break

time.sleep(3)
print("----------------------------------------------------------------------------")
slow_typing('*After that, you get going to school*')
time .sleep(1)
choice = input("Hey, since we have some time right now, some rules: [press Enter]")
pause("Throughout the game, only type what's written in ( / ) or [] as your responses. If there are no options, don't type anything.")
pause("You have stats in the game as you saw at the start. Every choice you make affects them, so make sure to choose wisely.")
pause("Infact, some of the choices you've made have already affected them.")
pause("You can view stats at the end of each term.")
slow_typing('*The wind picks up, you hear a crow in the distance*')
time.sleep(2)
pause("I really hope your day goes well today, and none of *those* guys come.")
slow_typing('. . .')
print("What guys am i talking about? You know! th-them -->")
time.sleep(3)
print('''
                                   𓌹  𓌺
      ¯\༼ ༎ຶ ෴ ༎ຶ༽/¯     {¬ºཀ°}¬   (꒪ཀ꒪)
       ༼   _ ¯ -   ༽       ||      `{-}`
      ༼  ¯  - _  ¯  ༽  	  / \       ||
      ''')

time.sleep(2)
print("RUNNN!!!!")
time.sleep(2)
choice = check_valid_input("[run] or [stay]", "Chose one of the options dude, quickly!\n[run] or [stay]", ['run', 'stay'])
while True:
    if choice == 'stay':
        print("What are you doing? They're gonna get you! Get away!")
        time.sleep(1)
        choice = check_valid_input("[run] or [stay]", '[run] or [stay]!', ['run', 'stay'])        
        if choice == 'run':
            slow_typing('*You chose to run*')
            pause("What on earth were you thinking!")
            slow_typing('*Your heart rate increases.*')
            time.sleep(3)
            slow_typing("*You end up running all the way to school without looking back*")
            stats['health'] -= 5
            break
        else:
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
                pause("*you tried fighting the monster, but you couldn't, and you were crushed.*")
                pause("Well that was dumb.")
                stats['health'] -=10
                stats['safety'] +=5
                break
            else:
                print("A valid option was not selected.")
                time.sleep(2)
                slow_typing("*You end up just standing where you were*")
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
                time.sleep(1)
                pause("next time, type one of the options!")
                stats['health'] -=15
                break
    else:
        slow_typing('*You chose to run*')
        time.sleep(1)
        pause("Thankgoodness! Why on earth would you choose to stay?")
        stats['safety'] -= 8
        break

print("----------------------------------------------------------------------------")
slow_typing('*you finally get to school*')
time.sleep(1)
print("Let's hope the rest of your day goes easier")

period1_class = random.choice(classes)
teacher1 = teacher_of_class[period1_class]

time.sleep(3)
pause(f"\n*You walk into the familiar building and head to your coordinators office. You collect your timetable. Your first class is {period1_class}. Lets go!*")
print("\n*BRINNGGGG!!")
time.sleep(2)
pause("*The bell goes just as you walk in. Suddenly your teacher looks at you*") 
if choice_books in ['b' ,'fine, ill pack']:
    pause(f"{teacher1}: {name}!, come sit down!")
    stats['social'] += 2
    slow_typing("*Since you brought your books, you had a productive lesson*")
    time.sleep(3)
    pause("The rest of your day went amazing. You met your friends, and you enjoyed most of your classes.")
else:
    print(f"\n{teacher1}: {name}, why are you walking in empty handed, where are your books?")
    time.sleep(4)
    print(f"{name}: I didn't think we'd need them today.")
    time.sleep(3)
    slow_typing(f"*{teacher1} was very disapointed with you and gave you a negative*")
    time.sleep(1)
    pause("Looks like you messed up.")
    stats['academics'] -= 3
    pause("The rest of your day was pretty bad. You got in trouble again for not bringing your books, and you had detention at lunch.")
    stats['social'] -=3

print("----------------------------------------------------------------------------")
slow_typing("*After a long, tiring day at school, you finally head home.*")
choice = input('[Enter]')
pause("You kick off your shoes, throw your bag on your chair and plop onto your bed.")
pause("You think to yourself, 'Will every day of year 11 be like this?'")
time.sleep(2)
slow_typing("\n*¨¨*:·..·:*¨¨*:·..·:*¨¨*:·..·:*¨¨*:·..·:*¨¨*")
slow_typing("9 Weeks later...",)
time.sleep(2)
pause("*Lets find out how the rest of your term went*")
print("----------------------")

madlibs = []
def mad_add(text):
    madlibs.append(input(text))
    
prompts = [
    "Insert a Subject:",
    "Something you do with your mates: (eg. eating, gaming)",
    "A friends name:",
    "Another:",
    "Abstract Adjective: (eg. nice, terrible)",
    "Piece of stationary:",
    "Preposition: (eg. between, behind)",
    "Plural noun:",
    "A common noun of a person: (eg. buddy, mum)"]
    
for i in prompts:
    mad_add(i)

slow_typing("processing...")
time.sleep(1)
slow_typing('''Every day you would look forward to {0}. On the weekends you enjoyed {1} with {2} and {3}. Studying was {4}.
Once, you even lost your {5} {6} some {7}. Those same {7} were a gift by your {8} after completing your tests. Speaking of tests, should'nt you be studying for your finals?'''.format(*madlibs))

convo = [
    "BEEP",
    "{madlibs[2]}: Hello?",
    "{name}: Hi! What're you doing right now {madlibs[2]}",
    "{madlibs[2]}: . . .",
    '{name}: {madlibs[2]?}',
    "{madlibs[2]}: ITS 1:47 AM DUDE. GO TO SLEEP",
    "BEEP"]


choice = check_valid_input("Will you study or not?\na) Ofcourse, i can't fail my finals!\nb) nah\n", "choose from [a] or [b]:", ['a', 'b'])
if choice == 'a':
    slow_typing("*You chose to study*")
    time.sleep(1)
    stats['academics'] += 10
    pause("You focus in class and do your homework when you come home. You spend hours revising your lessons and preparing for your tests")
    pause("You're getting tired and bored now.")
    choice = check_valid_input("Do you keep studying?\na) I have to\nb)I'll take a break", "choose from [a] or [b]",['a', 'b'])
    if choice == 'a':
        stats['academics'] += 10
        slow_typing("*You keep studying*")
        stats['health'] -=6
        time.sleep(2)
        slow_typing("z z zzzz...")
        time.sleep(2)
        print("You fell asleep!")
        time.sleep(2)
        pause("You exhausted yourself studying.")
        pause("Let's hope that all this studying will be worth it in the end atleast :/")
    else:
        slow_typing("You decide to take a break")
        time.sleep(2)
        choice = check_valid_input("Do you:\na)Spend time with friends or \nb)Go for a walk outside?", 'choose [a] or [b]', ['a', 'b'])
        if choice == 'a':
            stats['social'] += 5
            slow_typing(f"You pull out your phone and call {madlibs[2]}")
            time.sleep(1)
            slow_typing("ringgg...ringgg...ring...")
            time.sleep(1)
            slow_typing(". . .")
            time.sleep(1)
            for i in convo:
                print(i)
                time.sleep(1)
            slow_typing(". . .")
            time.sleep(1)
            pause("Yeah, I should get some sleep.")
        else:
            print("1")
            #copy paste the moster thing
else:
    slow_typing("*You chose to not study*")
    time.sleep(1)
    stats['academics'] -= 10
    pause("You step out of your house to take a walk outside. You feel the wind on your face and hear some crows in the distance.")
    slow_typing(". . .")
    choice = input("Do you walk back inside? (yes/no)")
    while True:
        if choice == 'yes':
            slow_typing("*You start walking back*")
            time.sleep(2)
            pause("You feel a strange sense of deja vu...")
            pause("You spot a cricket bat on the lawn infront of your window. You bring it in with you.")
            print("-------------------------------------------------------")
            break
        elif choice == 'no':
            stats['health'] -= 5
            slow_typing("*You start walking*")
            time.sleep(1)
            print("You intend on walking to the park two roads across")
            time.sleep(4)
            print("dhjfggfd...")
            time.sleep(2)
            print("")
            time.sleep(2)
            print("olkjuyghjmnhjiukjtresdfgt...")
            time.sleep(4)
            print('''
          _ -  ¯¯ - _
        {     𓌹  𓌺     }
       {     (꒪ཀ꒪)     } AWESDRTGFDRT!!!!
        {    `{-}`    }
         {    | |    }
         ''')
            time.sleep(2)
            print("AAAAAAHHHHHH!!")
            time.sleep(1)
            print("*RUN*")
            time.sleep(1)
            print("*and you run,*")
            time.sleep(1)
            print("*and you keep running until you make it back, grabbing the cricket bat that was lying on your lawn on your way in*")
            time.sleep(5)
            slow_typing(". . .")
            pause("Why do these monsters keep showing up?")
            slow_typing("*You don't know what to do*")
            time.sleep(2)
            pause("Maybe you should've just studied.")
            break
        else:
            choice = input("(yes/no)")

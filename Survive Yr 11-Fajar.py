from functions import *
stats = {'health':80, 'safety':50, 'academics':30, 'social':50 }

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
choice = check_valid_input("Are you excited? (yes/no)", "Just a reminder to choose from the options provided :)\nAre you excited? (yes/no)", ['yes','no'])    
while True:
    if choice == 'yes':
        print("Well then, let's get ready for school!")
        stats['academics'] += 1
        break
    elif choice == "no":
        slow_typing('. . .', 0.1)
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
        slow_typing('*you packed your bag, good job!*', 0.06)
        stats['academics'] += 2
        break
    else:
        slow_typing('. . .', 0.1)
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
slow_typing('*After that, you get going to school*', 0.06)
time .sleep(1)
choice = input("Hey, since we have some time right now, some rules: [press Enter]")
pause("Throughout the game, only type what's written in ( / ) or [] as your responses. If there are no options, don't type anything.")
pause("You have stats in the game as you saw at the start. Every choice you make affects them, so make sure to choose wisely.")
pause("Infact, some of the choices you've made have already affected them.")
pause("You can view stats at the end of each term.")
slow_typing('*The wind picks up, you hear a crow in the distance*', 0.06)
time.sleep(2)
pause("I really hope your day goes well today, and none of *those* guys come.")
slow_typing('. . .',0.1)
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
            slow_typing('*You chose to run*', 0.06)
            pause("What on earth were you thinking!")
            slow_typing('*Your heart rate increases.*', 0.06)
            time.sleep(3)
            slow_typing("*You end up running all the way to school without looking back*", 0.06)
            stats['health'] -= 5
            break
        else:
            slow_typing('. . .', 0.1)
            choice = input("What are you gonna do then? Fight? \n[i guess] or [how]").strip().lower()
            if choice == 'how':
                time.sleep(1)
                slow_typing('. . .',0.1)
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
                slow_typing('*you were crushed by the monster*', 0.06)
                pause("If you were gonna stay, you could have atleast tried to fight back :/ ")
                stats['health'] -=20
                stats['safety'] -=5
                break
            elif choice == 'i guess':
                time.sleep(1)
                print("You're screwed dude\n")
                time.sleep(1)
                slow_typing('*you chose to fight*', 0.06)
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
                stats['health'] -=15
                stats['safety'] +=5
                break
            else:
                print("A valid option was not selected.")
                time.sleep(2)
                slow_typing("*You end up just standing where you were*", 0.06)
                slow_typing('. . .',0.1)
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
                slow_typing('*you were crushed by the monster*', 0.06)
                time.sleep(1)
                pause("next time, type one of the options!")
                stats['health'] -=20
                stats['safety'] -=5
                break
    else:
        slow_typing('*You chose to run*', 0.06)
        time.sleep(1)
        pause("Thankgoodness! Why on earth would you choose to stay?")
        stats['safety'] -= 5
        break

print("----------------------------------------------------------------------------")
slow_typing('*you finally get to school*', 0.06)
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
    stats['social'] += 3
    slow_typing("*Since you brought your books, you had a productive lesson*", 0.06)
    time.sleep(3)
    pause("The rest of your day went amazing. You met your friends, and you enjoyed most of your classes.")
else:
    print(f"\n{teacher1}: {name}, why are you walking in empty handed, where are your books?")
    time.sleep(4)
    print(f"{name}: I didn't think we'd need them today.")
    time.sleep(3)
    slow_typing(f"*{teacher1} was very disapointed with you and gave you a negative*", 0.06)
    time.sleep(1)
    pause("Looks like you messed up.")
    stats['academics'] -= 3
    pause("The rest of your day was pretty bad. You got in trouble again for not bringing your books, and you had detention at lunch.")
    stats['social'] -=3

print("----------------------------------------------------------------------------")
slow_typing("*After a long, tiring day at school, you finally head home.*", 0.06)
choice = input('[Enter]')
pause("You kick off your shoes, throw your bag on your chair and plop onto your bed.")
pause("You think to yourself, 'Will every day of year 11 be like this?'")
time.sleep(2)
slow_typing("\n*¨¨*:·..·:*¨¨*:·..·:*¨¨*:·..·:*¨¨*:·..·:*¨¨*", 0.08)
slow_typing("9 Weeks later...",0.08)
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

slow_typing("processing...", 0.08)
time.sleep(1)
slow_typing('''Every day you would look forward to {0}. On the weekends you enjoyed {1} with {2} and {3}. Studying was {4}.
Once, you even lost your {5} {6} some {7}. Those same {7} were a gift by your {8} after completing your tests. Speaking of tests, should'nt you be studying for your finals?'''.format(*madlibs),0.08)

cricket_bat = ''

def weekend():
    time.sleep(2)
    choice = check_valid_input("Will you study or not?\na) Ofcourse, i can't fail my finals!\nb) nah\n", "choose from [a] or [b]:", ['a', 'b'])
    if choice == 'a':
        slow_typing("*You chose to study*", 0.06)
        time.sleep(1)
        stats['academics'] += 10
        pause("You focus in class and do your homework when you come home. You spend hours revising your lessons and preparing for your tests")
        pause("You're getting tired and bored now.")
        choice = check_valid_input("Do you keep studying?\na) I have to\nb)I'll take a break", "choose from [a] or [b]",['a', 'b'])
        if choice == 'a':
            stats['academics'] += 10
            slow_typing("*You keep studying*", 0.06)
            stats['health'] -=6
            stats['academics'] +=5
            time.sleep(2)
            slow_typing("z z zzzz...", 0.1)
            time.sleep(2)
            print("You fell asleep!")
            time.sleep(2)
            pause("You exhausted yourself studying.")
            pause("Let's hope that all this studying will be worth it in the end atleast :/")
        else:
            slow_typing("*You decide to take a break*", 0.06)
            time.sleep(2)
            choice = check_valid_input("Do you:\na)Spend time with friends or \nb)Go for a walk outside?", 'choose [a] or [b]', ['a', 'b'])
            if choice == 'a':
                stats['social'] += 5
                slow_typing(f"You pull out your phone and call {madlibs[2]}",0.06)
                time.sleep(1)
                slow_typing("ringgg...ringgg...ring...", 0.18)
                time.sleep(1)
                slow_typing(". . .", 0.1)
                time.sleep(1)
                print("BEEP")
                time.sleep(1)
                print(f"{madlibs[2]}: Hello?")
                time.sleep(1)
                print("{0}: Hi! What're you doing right now {1}".format(name, madlibs[2]))
                time.sleep(2)
                print(f"{madlibs[2]}: . . .")
                time.sleep(2)
                print(f"{madlibs[2]}: ITS 1:47 AM DUDE. GO TO SLEEP")
                time.sleep(1)
                print("BEEP")
                time.sleep(2)
                slow_typing(". . .", 0.15)
                time.sleep(1)
                pause("Yeah, I should get some sleep.")
            else:
                slow_typing("*You decide to get some fresh air.*", 0.06)
                time.sleep(1)
                pause("It's a lovely day out isn't it?")
                slow_typing("*Your destination is the park two roads across*", 0.06)
                time.sleep(4)
                print("dhjfggfd...")
                time.sleep(2)
                print("?")
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
                print("\n─=≡Σ ﾍ( ´Д`)ﾉ")
                time.sleep(1)
                print("*and you keep running until you make it back, grabbing the cricket bat that was lying on your lawn on your way in*")
                cricket_bat == 'yes'
                time.sleep(5)
                slow_typing(". . .", 0.1)
                pause("Why do these monsters keep showing up?")
                slow_typing("*You don't know what to do*" ,0.06)
                time.sleep(2)
                stats['safety'] -= 5
                pause("Maybe you should've just kept studying :\ ")
    else:
        slow_typing("*You chose to not study*",0.06)
        time.sleep(1)
        stats['academics'] -= 10
        pause("You step out of your house to take a walk outside. You feel the wind on your face and hear some crows in the distance.")
        slow_typing(". . .", 0.1)
        choice = input("Do you walk back inside? (yes/no)")
        while True:
            if choice == 'yes':
                slow_typing("*You start walking back*",0.06)
                time.sleep(2)
                pause("You feel a strange sense of deja vu...")
                pause("You spot a cricket bat on the lawn infront of your window. You bring it in with you.")
                cricket_bat == 'yes'
                break
            elif choice == 'no':
                stats['safety'] -= 5
                slow_typing("*You start walking*",0.06)
                time.sleep(1)
                print("You intend on walking to the park two roads across")
                time.sleep(4)
                print("dhjfggfd...")
                time.sleep(2)
                print("?")
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
                print("\n─=≡Σ ﾍ( ´Д`)ﾉ")
                time.sleep(1)
                print("*and you keep running until you make it back, grabbing the cricket bat that was lying on your lawn on your way in*")
                cricket_bat == 'yes'
                time.sleep(5)
                slow_typing(". . .", 0.1)
                pause("Why do these monsters keep showing up?")
                slow_typing("*You don't know what to do*",0.06)
                time.sleep(2)
                pause("Maybe you should've just studied.")
                break
            else:
                choice = input("(yes/no)")
weekend()

score = ''
def exam():
    global score
    time.sleep(2)
    print("\n\n----------------------------------------------------------------------------")
    print("                         »»—— Exam time! ——««")
    time.sleep(2)
    slow_typing("*You walk into the exam hall*", 0.06)
    if stats['academics'] == 49:
        time.sleep(1)
        pause("You feel confident knowing you've studied hard.")
        slow_typing("*Your eyes droop a bit*", 0.08)
        time.sleep(1)
        pause("But you also feel tired.")
        time.sleep(1)
        print("---------------------------------------------------------------")
        time.sleep(1)
        slow_typing("55 minutes later...", 0.18)
        time.sleep(1)
        slow_typing("z z zzzz...", 0.1)
        time.sleep(2)
        print(f"{teacher1}: {name}, wake up!")
        time.sleep(2)
        slow_typing("*You ended up falling asleep during your test because you were so tired!*", 0.08)
        time.sleep(2)
        pause("Did you finish atleast?")
        score = random.randint(70,79)
    elif 42 < stats['academics'] <= 48:
        time.sleep(1)
        pause("You feel confident, trusting yourself because you studied.")
        pause("You are alert and ready")
        print("---------------------------------------------------------------")
        time.sleep(1)
        slow_typing("55 minutes later...", 0.18)
        time.sleep(3)
        pause("You completed your test and triple checked it.")
        pause("You have a good feeling about this.")
        score = random.randint(80,100)
    elif 30 <= stats['academics'] <= 42:
        time.sleep(1)
        pause("you sit down and stare at your paper.")
        pause("It'll be fine right?")
        print("---------------------------------------------------------------")
        time.sleep(1)
        slow_typing("55 minutes later...", 0.18)
        time.sleep(3)
        print("*sigh*")
        time.sleep(2)
        pause("it wasn't that good, but atleast you finished the test.")
        score = random.randint(50,69)
    elif 18 <= stats['academics'] < 30:
        time.sleep(1)
        pause("Its dawning on you now just how much trouble you're in.")
        pause("You sit down and flick through the paper as the timer starts.")
        pause("You honestly wonder if you're even sitting in the correct exam hall.")
        print("---------------------------------------------------------------")
        time.sleep(1)
        slow_typing("55 minutes later...", 0.18)
        time.sleep(3)
        pause("Welp, you definitely failed that.")
        score = random.randint(1,49)
    else:
        time.sleep(1)
        slow_typing("and you walk out.", 0.08)
        time.sleep(1)
        pause("You can't be bothered.")
        print("---------------------------------------------------------------")
        time.sleep(1)
        slow_typing("55 minutes later...", 0.1)
        time.sleep(2)
        pause("*You're currently leaning on the school gate scrolling through your phone*")
        pause(f"{name}: whatever ¯\_(•-•)_/¯")
        score = 0
    return score
exam()

def end_of_term(term):
    time.sleep(3)
    print("\n\n*It is now the end of the term*")
    time.sleep(1)
    slow_typing("You have recieved your report...", 0.1)
    time.sleep(2)
    print(f'''
    --------------------------------------------------------------------
                             [End card]
                      ..........................''')
    slow_typing(f"Exam results: Your average is {score}%", 0.05)
    time.sleep(2)
    print(f"Your stats currently are:")
    time.sleep(2)
    print(f"Health: {stats['health']}")
    time.sleep(0.8)
    print(f"Academics: {stats['academics']}")
    time.sleep(0.8)
    print(f"Social: {stats['social']}")
    time.sleep(0.8)
    print(f"Safety: {stats['safety']}")
    time.sleep(3)
    check_stats()
    print(f"*End of term {term}*")
end_of_term(1)


#term 2
teacher2 = random.choice(teachers)
bud = random.choice(classmates)
bud2 = random.choice(classmates)
group = random.randint(1,2)
marks = ['full marks', 'an A']
mark = random.choice(marks)

time.sleep(3)
print("︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶︶")
pause("After a nice term break, you get back to school.")
pause(f"On literally the second day, {teacher2} gives you a big group project.")
slow_typing(f"\nYour team mates are: {madlibs[3]}, {bud} and {bud2}.", 0.06)

if group == 1:
    stats['social'] += 5
    time.sleep(2)
    slow_typing("*You ended up being grouped with your friends!*", 0.06)
    time.sleep(1)
    pause("Since you 4 are friends, you get on just fine.")
    print("You work on your project efficiently for the rest of the period.")
    time.sleep(5)
    print("\n*BRINNGGGG!!")
    time.sleep(2)
    pause(f"{bud2}: Oh! The periods over guys.")
    slow_typing("You divide up the rest of the project fairly", 0.06)
    time.sleep(1)
    pause(f"{teacher2}: Remember guys! This project is due in Week 5. And no extentions!")
    time.sleep(3)
    print("--------------------------------------------------------------------")
    slow_typing("*Back at home:", 0.06)
    time.sleep(1)
    choice = check_valid_input("You have the choice to \na) Work on your project or \nb) Procrastinate", "choose [a] or [b]", ['a', 'b'])    
    if choice == 'a':
        stats['academics'] += 6
        time.sleep(1)
        slow_typing("*You chose to work on your project*", 0.06)
        time.sleep(2)
        for i in ['scribble scribble...', 'snip snip', '*glue*', '. . .', 'snip', 'click, click, click...']:
            print(i)
            time.sleep(2)
        time.sleep(2.5)
        slow_typing(". ݁₊⊹. ݁˖ .˖⁺‧₊˚✦", 0.07)
        time.sleep(0.5)
        pause("You've finished your part! ☆")
        time.sleep(2)
        print("--------------------------------------------------------------------")
        slow_typing("*At school: Wk 5", 0.1)
        time.sleep(2)
        pause(f"{teacher2}: Everyone! Your projects are due today, please hand them in.")
        slow_typing("*you walk up to the teacher's desk and submit your work", 0.06)
        time.sleep(1.5)
        print(f"{teacher2}: Thankyou {name}! This is excellent! You and your group did an amazing job ദ്ദി(ᵔᗜᵔ)")
        time.sleep(2)
        slow_typing("*Your group looks around at each other with smiles all around*", 0.06)
        time.sleep(2)
        print("--------------------------------------------------------------------")
        pause("A while later you get your marks back.")
        pause("You got an A on your project. Good job!")        
    else:
        stats['academics'] -= 3
        time.sleep(1)
        slow_typing("*You chose to not work on your project at the moment*", 0.06)
        time.sleep(2)
        choice = check_valid_input("What are you gonna do instead then? \n[sleep] or [chat to smn]","choose from the options please",['sleep', 'chat to smn'])
        if choice == 'sleep':
            stats['health'] += 5
            time.sleep(1)
            print(". . .")
            time.sleep(1)
            slow_typing("z z zzzz...", 0.1)
            time.sleep(1)
            slow_typing("*You went to sleep*", 0.06)
        else:
            stats['social'] += 5
            slow_typing(f"You pull out your phone and call {madlibs[3]}",0.06)
            time.sleep(1)
            slow_typing("ringgg...ringgg...ring...", 0.18)
            time.sleep(1)
            slow_typing(". . .", 0.1)
            time.sleep(1)
            print("BEEP")
            time.sleep(1)
            print(f"{name}: Hello?")
            time.sleep(1)
            print(f"{madlibs[3]}: Hi! What're you doing right now?")
            time.sleep(2)
            print(f"{name}: Procrastinating the project.")
            time.sleep(2)
            print(f"{madlibs[3]}: . . .")
            time.sleep(1)
            print(f"{name}:{madlibs[3]}?")
            time.sleep(2)
            print(f"{madlibs[3]}:DO THE PROJECT DUDE")
            time.sleep(1)
            print("BEEP")
            time.sleep(2)
            slow_typing(". . .", 0.15)
            time.sleep(1)
            pause(f"Maybe you should work on the project {name}, just a suggestion.")
        stats['social'] -= 2
        time.sleep(2)
        print("--------------------------------------------------------------------")
        slow_typing("*At school: Wk 5", 0.1)
        time.sleep(2)
        pause(f"{teacher2}: Everyone! Your projects are due today, please hand them in.")
        slow_typing("*you walk up to the teacher's desk and submit your rushed work", 0.06)
        time.sleep(1.5)
        print(f"{teacher2}: Thankyou for submitting your work {name}'s group.")
        time.sleep(2)
        pause("*Your group looks around at each other, uncertain what mark you're going to get.*")
        print("*They look at you in particular*")
        time.sleep(1.5)
        print('oops ¯\_ (ᵕ—_—)_/¯')
        time.sleep(2)
        print("--------------------------------------------------------------------")
        pause("A while later you get your marks back.")
        pause("It's not the best mark, but you passed!")
        time.sleep(2)
        print("\nNext time, don't procrastinate if you want better marks (¬_¬ )")
else:
    stats['social'] -= 5
    time.sleep(2)
    slow_typing(". . .", 0.1)
    slow_typing("*You got grouped with your enemies*", 0.06)
    time.sleep(1)
    pause("You guys hate each other (cuz of some past history or smt), so you can imagine what happens next, or rather, what doesn't.")
    print("You get nothing done the whole period.")
    time.sleep(4)
    print("\n*BRINNGGGG!!")
    time.sleep(2)
    pause(f"{name}: Finally! The period's over.")
    slow_typing("You agree to divide up the work and do your bits by yourselves", 0.06)
    time.sleep(1)
    pause(f"{teacher2}: Remember guys! This project is due in Week 5. And no extentions!")
    time.sleep(3)
    print("--------------------------------------------------------------------")
    slow_typing("*Back at home:", 0.06)
    time.sleep(1)
    choice = check_valid_input("You have the choice to \na) Work on your project  \nb) Procrastinate  \nc) Just not do it at all", "choose [a], [b] or [c]", ['a', 'b', 'c'])    
    if choice == 'a':
        stats['academics'] += 6
        time.sleep(1)
        slow_typing("*You chose to work on your project*", 0.06)
        time.sleep(2)
        for i in ['scribble scribble...', 'snip snip', '*glue*', '. . .', 'snip', 'click, click, click...']:
            print(i)
            time.sleep(2)
        time.sleep(2.5)
        slow_typing(". ݁₊⊹. ݁˖ .˖⁺‧₊˚✦", 0.07)
        time.sleep(0.5)
        pause("You've finished your part! ☆")
        time.sleep(2)
        print("--------------------------------------------------------------------")
        slow_typing("*At school: Wk 5", 0.1)
        time.sleep(2)
        pause(f"{teacher2}: Everyone! Your projects are due today, please hand them in.")
        slow_typing("*you walk up to the teacher's desk and submit your work", 0.06)
        time.sleep(1.5)
        print(f"{teacher2}: Thankyou {name}! This looks nice. You and your group did well ദ്ദി")
        time.sleep(2)
        slow_typing("*Everyone in your group smiles to themselves*", 0.06)
        print("Even though you don't like each other, you all still worked hard on your owns at least.")
        time.sleep(2)
        print("--------------------------------------------------------------------")
        pause("A while later you get your marks back.")
        pause("You got an A on your project. Good job!")
    elif choice == 'b':
        stats['academics'] -= 3
        time.sleep(1)
        slow_typing("*You chose to not work on your project at the moment*", 0.06)
        time.sleep(2)
        choice = check_valid_input("What are you gonna do instead then? \n[sleep] or [chat to smn]","choose from the options please",['sleep', 'chat to smn'])
        if choice == 'sleep':
            stats['health'] += 5
            time.sleep(1)
            print(". . .")
            time.sleep(1)
            slow_typing("z z zzzz...", 0.1)
            time.sleep(1)
            slow_typing("*You went to sleep*", 0.06)
        else:
            stats['social'] += 5
            slow_typing(f"You pull out your phone and call {madlibs[3]}",0.06)
            time.sleep(1)
            slow_typing("ringgg...ringgg...ring...", 0.18)
            time.sleep(1)
            slow_typing(". . .", 0.1)
            time.sleep(1)
            print("BEEP")
            time.sleep(1)
            print(f"{name}: Hello?")
            time.sleep(1)
            print(f"{madlibs[3]}: Hi? What's up {name}?")
            time.sleep(2)
            print(f"{name}: Procrastinating the project.")
            time.sleep(2)
            print(f"{madlibs[3]}: . . .")
            time.sleep(1)
            print(f"{name}:{madlibs[3]}?")
            time.sleep(2)
            print(f"{madlibs[3]}:DO THE PROJECT DUDE")
            time.sleep(1)
            print("BEEP")
            time.sleep(2)
            slow_typing(". . .", 0.15)
            time.sleep(1)
            pause(f"Maybe you should work on the project {name}, just a suggestion.")
        stats['social'] -= 2
        time.sleep(2)
        print("--------------------------------------------------------------------")
        slow_typing("*At school: Wk 5", 0.1)
        time.sleep(2)
        pause(f"{teacher2}: Everyone! Your projects are due today, please hand them in.")
        slow_typing("*you walk up to the teacher's desk and submit your rushed work", 0.06)
        time.sleep(1.5)
        print(f"{teacher2}: Thankyou for submitting your work {name}'s group.")
        time.sleep(2)
        pause("*Your group looks around at each other, not quite happy.*")
        print("*They look at you in particular*")
        time.sleep(1.5)
        print('oops ¯\_ (ᵕ—_—)_/¯')
        time.sleep(2)
        print("--------------------------------------------------------------------")
        pause("A while later you get your marks back.")
        pause("It's not the best mark, but you passed!")
        time.sleep(2)
        print("\nNext time, don't procrastinate if you want better marks (¬_¬ )")
    else:
        stats['academics'] -= 6
        time.sleep(1)
        slow_typing("*You chose to not do the project at all*", 0.06)
        time.sleep(1)
        pause(f"{name}: {bud} and {bud2} can suck it. I won't help them with a project >:C")
        time.sleep(3)
        print("--------------------------------------------------------------------")
        slow_typing("*At school: Wk 5", 0.1)
        time.sleep(2)
        pause(f"{teacher2}: Everyone! Your projects are due today, please hand them in.")
        slow_typing("*Everyone in your group just looks around at each other", 0.06)
        time.sleep(2)
        print("No one did anything.")
        time.sleep(2)
        print(f"{teacher2}:{name}, where is your group's project?")
        time.sleep(1)
        print(f"{name}: . . .")
        time.sleep(1)
        print(f"{teacher2}: You mean to tell me that NONE of you guys did ANYTHING? You have nothing to submit at all?")
        time.sleep(4)
        slow_typing("*slowly nod your head*", 0.06)
        time.sleep(2)
        print(f"{teacher2}: DETENTION! ALL OF YOU! you disgust me! ᕙ( ᗒᗣᗕ )ᕗ")
        time.sleep(23)
        print("--------------------------------------------------------------------")
        slow_typing("*You attend detention*", 0.06)
        stats['social'] -= 5
        time.sleep(2)
        print("Just do the project next time (¬_¬ )")
        
time.sleep(3)
print("--------------------------------------------------------------------")
slow_typing("One night you were just sleeping, as some students do. But suddenly you awoke, your throat as dry as a rock. You walked to the kitchen to get some water.", 0.04)
slow_typing("Gulp gulp gulp...", 0.1)
slow_typing("Refreshed, you walk back to your room, bearly keeping your eyelids open. But what you see next opens them right up.", 0.06)
time.sleep(2)
slow_typing("Something is trying to climb in through your window...", 0.15)
time.sleep(1)
print("""
⠀⡐⠀⠆⡐⢀⠂⠄⠠⠀⢀⡘⠀⠀⠀⠰⢁⠂⡘⠐⡀⠒⡀⢂⠁⠊⠄⠡⢈⠐⠡⠈⠄⠃⠌⡐⠠⠑⠂⠡⠐⢂⠑⡈⠄⠃⠄⠑⠂⠌⢂⠀⠀⠀⣞⠀⠀⠄⡈⠰⠉⠁⡉⢉⠉⡉⢋⠉⢉⠃⡑⢋⠒⠓⠒⡒
⠞⠒⡉⠒⡐⠂⡞⠐⠃⠘⠂⡆⠉⠀⠀⠘⠀⠂⠐⠀⠐⠀⠐⠀⠈⠐⠈⠐⠀⠈⠀⡡⠈⠐⠀⠐⠀⠂⠁⠀⠁⠀⠂⠀⠐⠈⠀⠠⠁⠌⢂⠀⠀⢰⢨⠆⠥⠲⢤⠓⣤⣥⡰⣤⣌⣄⡣⢌⡄⣂⡄⢣⣄⣃⣐⡁
⠠⡁⢄⠡⠐⢨⢀⠂⣌⠐⡠⠁⠀⠀⠀⣠⢄⣠⣀⣄⣠⣀⢄⣠⢀⡄⣠⢀⣠⢶⣻⣿⣿⡿⣶⢀⢀⡀⣀⢀⡀⣀⠀⡀⢀⠀⣀⠀⣀⢀⡀⠀⠀⢈⡚⡄⠀⠐⡀⠂⢄⠠⡐⢠⠐⡄⡐⠠⠈⡄⢉⠡⠌⡉⢉⡉
⡉⠙⢨⠉⢋⠡⠉⢉⠈⠉⢸⠀⠀⠀⠀⠛⣉⣉⣉⣉⣉⣉⣋⣉⣉⣉⣉⣩⡟⡴⣻⣿⡏⠷⣜⣻⣮⣉⣉⣍⣉⣉⣍⣩⣉⣍⣤⣉⣤⣄⡈⠀⠀⠀⢏⡔⠚⠒⠒⠞⡒⠖⠳⢦⠳⠖⡤⠧⢦⠤⡥⢮⢦⡕⡦⣔
⣄⣉⣐⣈⣄⣂⣁⣂⣈⣀⠣⠀⠀⠀⠀⠂⠉⠈⠁⠉⠈⠁⠈⠁⠉⠈⠉⣿⣿⣕⢣⡚⣿⢈⣶⣹⣿⣃⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢩⠁⠀⠀⠀⡈⠆⡐⠈⡐⠨⢅⡘⡐⢢⠐⡌⠰⠀⠆⡐⡀⠂⡇⠐⢤⠠
⢉⠋⡉⢉⠉⡏⠩⢉⠩⠙⠦⠀⠀⠀⠀⢰⣶⣶⣶⢶⣶⣶⣶⣶⣶⣶⡶⣿⣿⣿⣬⠳⢩⡎⣽⡟⣯⢏⣴⣦⣴⣤⣤⣤⣤⣤⣤⣤⣤⣬⡆⠀⠀⠀⠁⡖⠓⠒⠓⠲⠬⠥⠷⠬⢦⡵⢦⠴⣤⢥⣣⣤⣓⣰⣈⣄
⣀⣂⡐⣀⢰⡡⣁⡂⣄⢡⠒⠀⠀⠀⠀⢸⣿⣿⣿⢻⣿⣾⣽⣿⣿⣽⣿⣿⣿⣿⣚⣧⣿⣿⢼⣿⡇⡏⠈⠙⠛⠻⢿⡿⡿⢿⣽⣿⣿⣿⡇⠀⠀⠀⠀⢧⠀⠡⢂⠑⠠⢌⠰⣁⠢⢸⠀⠆⢠⠀⡄⡀⢠⠐⠌⡄
⡉⢉⠉⢉⠁⡁⠉⠁⡈⢘⠆⠀⠀⠀⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⡿⠉⣓⢃⣿⣿⣿⣗⣿⣽⣷⡦⠀⠀⠀⠀⠹⣽⣿⣿⣿⣿⣿⡧⠀⠀⠀⠈⡶⠙⠂⠃⢋⢳⠊⠖⠲⠲⠹⠚⠶⠒⠖⢦⠱⠤⣉⠶⢤
⣐⣠⣊⣄⣂⣀⣁⣂⣐⡌⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⡃⠀⠌⣳⣾⣿⣿⣿⠼⣿⣿⣧⠄⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣗⠀⠀⠀⠀⡱⢀⠠⠁⢂⠸⡁⢌⠱⢈⠡⢚⠠⠉⢆⠐⡂⠄⡇⡐⢂
⠄⠡⢀⠨⢇⠠⠀⠄⡠⢛⢀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣾⣿⣾⣟⣿⣿⡇⠀⠀⠹⣿⣿⡏⣱⡂⢽⣿⣿⠀⡀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣯⠀⠀⠀⢀⢸⠋⡉⢉⡉⢋⠙⠋⠛⡙⠓⡟⠒⠓⠲⠚⠶⠲⠳⠶⠳
⣊⣔⣡⣘⢢⣄⣡⣂⣄⢇⠂⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣟⡀⣀⢀⢻⣿⣿⣄⠀⢻⣿⣿⣿⡄⠀⣀⡠⣴⣾⣿⣿⣿⣿⣷⠀⠀⠀⠀⢪⠇⡐⠠⠐⢂⡉⠄⠃⠆⠓⣸⠀⡍⢂⠱⣀⠡⢒⠠⠐
⠠⠄⡀⠀⠄⡀⠀⠀⣘⠣⠀⠀⠀⠀⢸⣿⣿⣿⣿⢿⣷⣿⣿⣿⣿⣿⣿⢯⡷⣐⠊⠜⣿⣿⣿⣄⣼⣿⣿⣿⡧⢉⠄⡒⣿⡧⠹⣿⣿⣿⣿⠀⠀⠀⠀⢸⠋⡑⠋⠙⠒⡛⠚⡛⢓⠓⡘⠒⠳⠚⠓⠦⠳⢎⡶⠵
⣁⣆⣠⣁⣂⣐⣠⣀⡔⠂⠀⠀⠀⠀⣻⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣆⢁⠊⢽⣿⣿⣿⣿⣿⣿⣿⡗⡀⢂⢱⡿⠁⠀⠀⠙⢿⣿⠀⠀⠀⠀⢨⠃⢀⠘⠠⠁⣏⠠⡑⢌⡘⡄⢩⡐⠡⢈⠂⠡⢀⡇⡀
⢈⠠⢉⡆⠡⢀⠁⠄⡹⠀⠀⠀⠀⠀⣿⣟⡽⢫⠝⢫⠛⣾⣿⣟⣯⣿⣹⣿⣿⣿⡂⠌⣸⣿⣿⣿⣿⣿⣿⣿⡧⠐⠠⢹⠁⠀⠀⠠⠔⢺⣿⡀⠀⠀⠀⢬⠟⠉⢋⠙⡙⠘⢛⡙⠖⠓⢳⡓⠚⠳⠲⠳⠖⢖⠺⠰
⣂⡐⣸⡄⣁⣂⢌⡀⢇⠀⠀⠀⠀⠠⣿⣾⢥⠣⢌⠢⣵⣾⣟⣿⡽⣻⣿⣿⣿⣿⣓⠰⠠⣿⣿⣿⣿⣿⣿⣿⣷⢁⠂⡹⣡⠌⢀⠀⠉⠢⣽⠂⠀⠀⠀⣈⠆⢀⠢⠐⣈⠢⡁⠆⡅⠊⡔⡇⢀⠑⡠⠑⡌⢢⡑⠢
⡉⢉⠡⢉⠉⠉⠉⠙⠦⠀⠀⠀⠀⢸⢿⣍⠲⢁⡊⠷⢻⣾⣿⣻⣽⣿⣿⣿⣿⣿⣧⠊⣅⢻⣯⣿⣿⣿⣿⣛⣟⢢⢂⢱⠏⠀⠂⠈⠄⠠⣘⠆⠀⠀⠀⢠⡗⡒⠒⠲⡒⢖⡓⠾⠔⠳⠼⠣⠶⠼⠵⠼⠤⠧⢼⠥
⢈⢂⡐⠂⠌⡐⢁⠘⡂⠀⠀⠀⠀⢸⡯⢆⢃⠆⡌⢧⠡⢻⣽⣿⣽⣷⣿⣿⣿⣿⣷⢃⡌⢺⣿⣿⣿⣿⢷⡿⣼⢃⠎⣜⠀⢂⠀⠐⡈⢄⣿⡇⠀⠀⠀⠠⣣⠑⠌⡡⢉⢼⡀⠄⠐⡈⠄⠂⠄⠰⡀⢂⠰⡀⢊⡇
⠛⢺⡜⠛⠙⠙⠋⠳⡄⠀⠀⠀⠀⣸⢟⡬⣌⠰⣌⢣⠹⣘⠿⢳⣿⣞⣿⣿⣿⣿⣿⡆⠬⢹⣿⣿⣿⣿⣿⣿⣯⢇⡺⣇⠈⠀⢀⠂⣐⣾⣿⡇⠀⠀⠀⠐⣧⠚⠶⠱⠎⠶⡱⠖⠶⡴⠭⢖⠬⠰⠴⣠⠦⡤⢥⠦
⠄⣻⠄⡐⢈⠐⠀⡓⠀⠀⠀⠀⠀⠾⠙⠶⠉⠳⠌⠃⠛⠌⠳⠸⠷⠛⠿⠻⠿⠟⠿⢇⠡⣃⠿⢿⠿⡿⢿⡿⣿⢧⣻⡷⣜⡠⠀⠀⠘⣿⣿⡇⠀⠀⠀⠈⣷⠀⢢⠁⡌⢂⠔⡨⠐⠠⢐⢺⠀⣁⠂⡀⠄⡠⠄⡀
⠷⠷⠶⠶⠶⣶⠶⢭⢀⠀⠀⠀⠀⠐⠀⠂⠂⠐⠀⠂⠐⠀⠂⠀⠂⠐⠂⠒⠐⠒⠒⢂⠣⠄⡋⠄⡒⠐⠢⠰⡜⢢⢽⣿⣭⠳⣁⠂⠀⠀⠄⠠⠀⠀⠀⠈⣶⡬⣤⣒⣬⣡⣊⣔⣡⡜⣀⣫⣐⣤⣃⣐⣁⣢⣁⣢
⢂⠐⠠⢂⠐⣈⢿⡀⢥⡈⢴⡦⠔⠦⡴⢴⡐⠦⣐⠰⡤⢤⠴⡤⢦⡄⢂⡐⠠⢤⡤⢦⢱⡎⡔⢧⣸⣧⣎⡗⣨⢀⣋⢾⣾⣿⣆⠆⡐⠈⠀⠤⣤⢀⡀⠡⠻⡄⢢⠐⢤⠂⡧⢀⠠⠀⡔⠠⢀⠄⡰⠄⠤⢀⠄⡰
⢎⡴⣡⢆⡦⣤⡗⡌⢦⠑⣮⠇⡎⠵⣈⢯⠐⡎⣌⠓⡏⠤⢋⡜⢥⠋⢦⢙⡱⢻⡜⡿⣿⣿⣿⣿⣿⠹⣿⣾⣧⣾⣼⣿⣿⣿⣿⡼⣄⠠⠀⠐⢸⢎⡵⣋⠥⣇⣂⣙⣢⢁⣇⣠⢘⣐⢠⣑⣈⠰⣀⢃⢆⣈⢆⢰
⢠⡓⢄⠢⡐⡜⣧⣜⣡⣋⣼⣟⣘⣣⣃⣯⣘⣰⣈⣦⣙⣣⣭⣜⣣⣝⣢⢏⡜⣧⡽⢼⡱⢮⡟⡰⠎⢳⢹⡏⠛⡟⢫⣿⡟⣿⣿⣷⡞⡴⠀⠂⠈⢒⠶⡩⠖⡍⡉⢉⠡⢉⠜⡩⢩⡍⣩⠱⡎⢱⡈⠎⣬⢡⢊⡍
⣄⣧⣈⣦⣱⣼⣟⣨⣡⣍⣩⣉⣉⣡⢉⣩⡁⢋⠉⣌⢩⡑⢌⡩⡹⢌⢣⠋⡙⢩⠛⢋⠙⡋⢿⠙⢋⠛⣏⠛⡛⢛⡛⣿⢛⡟⡿⣿⣿⡵⢣⠐⠀⠘⣻⢛⡿⡇⡱⢈⠆⡌⠤⡑⢢⢒⡱⢌⠇⠢⣍⠲⠰⣌⠣⣌
⠿⢇⡘⢤⠣⣽⢨⢃⡑⡏⢡⢁⠆⢠⢁⠣⢘⢡⠘⡌⢢⠜⡠⢃⣍⢙⡎⠡⢈⠍⢨⠁⣍⠹⣨⠉⡍⢫⡉⢝⡩⢋⡝⣟⢫⡟⣽⣻⣟⡿⣧⢣⠄⠀⠰⣏⡾⡻⣝⠋⠾⢙⠚⣙⠚⡋⣖⠋⣆⡑⢒⢂⢋⠰⢃⠒
⣋⢤⡙⢤⡓⢼⣧⢂⢜⡇⢜⠢⠎⡰⣈⠳⢨⢎⡘⢜⢠⠓⡌⢒⡌⢸⠇⠘⣄⠋⢤⢃⠤⢓⠴⡈⢜⢠⠚⡤⣑⠣⢎⣯⢳⢪⢵⡳⣯⢿⣽⣳⢎⡀⠀⢫⡹⢧⡯⢌⡱⢨⡙⡠⢋⡅⢲⡑⠴⡡⢍⢂⠎⢸⠂⡏
⡟⢋⠟⣛⢛⢻⡛⠿⡾⢾⢿⣿⣷⣷⣷⣿⣞⣞⣾⢾⣞⡿⣜⣳⣞⣯⣻⢾⣶⣻⢶⣞⣾⣼⣾⣴⣞⡶⣿⣴⣧⣿⣶⣧⣿⣷⣮⣷⣿⣿⣶⣿⣿⡄⠂⢀⢹⣾⣼⣧⣾⣴⣧⣧⣽⣦⣧⣽⣷⣵⣾⣼⣾⣬⣷⣮
⡇⢋⡞⢤⢋⢦⢝⡲⣍⠆⢮⡐⢆⡐⢆⢆⣹⡇⣩⢉⠬⢩⠍⣭⠩⣍⢍⠫⡭⢍⢏⡹⢩⡍⣽⠩⡏⡽⢩⡍⡭⠭⣍⢯⡍⢯⣙⢯⡹⣏⡿⣹⣯⢷⡈⠄⠠⣘⢧⡒⣜⠰⡰⢆⠦⡐⡆⠖⡄⡆⣲⢰⡒⣖⠲⣬
⠾⡳⢾⠳⣯⠾⢾⠶⣭⣮⣧⣭⢶⣼⣬⣶⣼⢧⣦⣧⣮⣴⣧⣼⣱⣮⣌⣳⣼⣑⣮⣜⣥⣒⣽⣲⣍⣣⣳⣸⣑⣫⣜⣶⣍⣳⣎⣷⣹⣞⣽⣳⣿⣯⠖⡈⠐⡈⣳⣝⣬⣓⣱⣋⣼⣡⣋⣹⣐⣇⣱⣣⣙⣎⣓⣶
⣏⢵⣋⠷⣌⢳⠪⡔⣿⠐⣦⡑⢮⢰⢣⠞⣆⠯⡒⢆⢦⡱⢰⠆⣇⢸⣍⠲⡌⡝⡼⣉⢎⠭⣜⣣⢸⢉⠧⣉⢏⠭⡍⣿⡙⢯⡹⣏⡿⣹⣛⡯⣿⠽⣏⠐⠠⡀⠉⢿⢩⢏⣭⢹⡩⢵⢫⡙⢶⡘⢧⡩⢍⣏⠹⣐
⣞⣲⣭⣻⡴⣋⡵⣂⣿⣘⢦⡹⣜⣬⢻⣭⢳⣯⢱⢏⡶⣭⣛⡼⣡⢺⢔⠣⡙⣜⢲⠡⣎⠳⣌⡓⢮⡙⡞⣤⢏⡞⡔⣿⢸⢧⣳⠽⣖⢯⣷⣫⣽⣛⠦⢃⠡⢀⠁⢮⡑⣎⡖⣣⡝⡦⢧⣹⢲⣍⠳⣜⢲⡌⡳⢌
⢹⡭⢯⢽⡹⣏⢿⣫⢝⣯⢻⣹⢋⡟⣿⡻⣿⣻⣛⢿⣾⡛⣿⢶⣟⣞⠺⣛⢳⡛⣞⠳⡞⠿⡾⢿⢞⡷⡿⢾⠿⢾⢷⡟⡿⣿⢾⡿⡾⣿⢾⢷⡿⢿⡃⣌⠲⢤⣉⢶⣻⣼⢻⣳⢻⠝⣷⠻⡞⡞⡿⣞⢿⣚⢿⡾
⣟⣿⢯⣞⡵⢯⡞⣵⢺⢮⣳⡽⢮⣿⣽⡿⣿⣽⣿⣟⣾⣽⣞⡷⣞⢦⡳⢥⡳⡱⢎⡽⣘⡇⣿⣳⢞⣣⡟⣬⢏⡽⢮⣹⠜⣯⣻⡽⣟⣧⣟⢾⡟⣽⡵⣏⣻⡼⣾⢭⡷⣞⢿⡜⣯⢻⡼⡹⢆⣏⢷⣽⣫⣏⣷⣟""")
time.sleep(2)
pause("\n\n\ninternally:DTRDTFYGUCXDJTSDTFESIRDFAAAAAAAAAAAAAAHHHHHHHHHHH")
pause("But externally, you slowly back out of your room into the hallway.")
print("What on earth do you do?")
if cricket_bat == 'yes':
    choice = check_valid_input("a) There's a cricket bat...\nb) Hide ofcourse!","choose [a] or [b]",['a', 'b'])
    if choice == 'a':
        stats['safety'] += 10
        time.sleep(1)
        print("*You crawl into your room and make a grab for the bat*")
        time.sleep(1.5)
        print("Just as the monster turns to see you!")
        time.sleep(1)
        print('You grab the bat just as the monster jumps at you and...')
        time.sleep(1.5)
        print("You wack him on the head just as his slimy hand touches your face!")
        time.sleep(3)
        print("The monster sqeals in pain and runs away, climbing back out through your window")
        time.sleep(3)
        slow_typing(". . .", 0.15)
        print("You cautiously walk to the window and lock it")
        time.sleep(2)
        print("You also hurry to the bathroom to wash whatever gunk is on your face off.")
        time.sleep(5)
        pause("\n*Would it be wrong to suggest at this very moment that you should go back to sleep, because you kind of like have your semester exams tomorrow and you need to be rested. Just a suggestion.*")        
    else:
        stats['safety'] -= 10
        time.sleep(1)
        pause("*You tiptoe into the kitchen and hide in the pantry*")
        slow_typing("HshHSHshHSHHShhshSsSss......", 0.08)
        time.sleep(2)
        pause("*You hold your breath and pray whatever that thing is goes away.*")
        time.sleep(1)
        print("[Monster thing]: . . .??")
        time.sleep(1)
        slow_typing(". . .", 0.15)
        time.sleep(2)
        slow_typing("*The monster has left*", 0.06)
        time.sleep(1)
        slow_typing("*You wonder what it wanted*", 0.06)
        time.sleep(2)
        pause("\n*Would it be wrong to suggest at this very moment that you should go back to sleep, because you kind of like have your semester exams tomorrow and you need to be rested. Just a suggestion.*")        
else:
    choice = check_valid_input("a) I could get my math book...\nb) Hide ofcourse!","choose [a] or [b]",['a', 'b'])
    if choice == 'a':
        stats['safety'] += 7
        time.sleep(1)
        print("*You crawl into your room and make a grab for your math book that's resting on the table (fyi, its a brick!)*")
        time.sleep(3.5)
        print("Just as the monster turns to see you!")
        time.sleep(1)
        print('You grab the bat just as the monster jumps at you and...')
        time.sleep(1.5)
        print("You wack him on the head just as his slimy hand touches your face!")
        time.sleep(3)
        print("The monster sqeals in pain and runs away, climbing back out through your window")
        time.sleep(3)
        slow_typing(". . .", 0.15)
        print("You cautiously walk to the window and lock it")
        time.sleep(2)
        print("You also hurry to the bathroom to wash whatever gunk is on your face off.")
        time.sleep(5)
        pause("\n*Would it be wrong to suggest at this very moment that you should go back to sleep, because you kind of like have your semester exams tomorrow and you need to be rested. Just a suggestion.*")
        
    else:
        stats['safety'] -= 10
        time.sleep(1)
        pause("*You tiptoe into the kitchen and hide in the pantry*")
        slow_typing("HshHSHshHSHHShhshSsSss......", 0.08)
        time.sleep(2)
        pause("*You hold your breath and pray whatever that thing is goes away.*")
        time.sleep(1)
        print("[Monster thing]: . . .??")
        time.sleep(1)
        slow_typing(". . .", 0.15)
        time.sleep(2)
        slow_typing("*The monster has left*", 0.06)
        time.sleep(1)
        slow_typing("*You wonder what it wanted*", 0.06)
        time.sleep(2)
        pause("\n*Would it be wrong to suggest at this very moment that you should go back to sleep, because you kind of like have your semester exams tomorrow and you need to be rested. Just a suggestion.*")
        
score = ''
def exam2(stats, teacher1, name):
    time.sleep(2)
    print("\n\n----------------------------------------------------------------------------")
    slow_typing("               *It's time for your semester exams (>_<)*", 0.06)
    time.sleep(2)
    slow_typing("*You walk into the exam hall*", 0.06)
    if 52 < stats['academics'] < 55:
        time.sleep(1)
        pause("You feel confident knowing you've done all your work.")
        slow_typing("*Your eyes droop a bit*", 0.08)
        time.sleep(1)
        pause("But you also feel tired. You couldn't sleep after what happened last night.")
        time.sleep(1)
        print("---------------------------------------------------------------")
        time.sleep(1)
        slow_typing("180 minutes later...", 0.18)
        time.sleep(1)
        slow_typing("z z zzzz...", 0.1)
        time.sleep(2)
        print(f"{teacher1}: {name}, wake up!")
        time.sleep(2)
        slow_typing("*You ended up falling asleep during your test because you were so tired!*", 0.08)
        time.sleep(2)
        pause("Did you finish atleast??")
        score = random.randint(70,79)
    elif 47 < stats['academics'] <= 52:
        time.sleep(1)
        pause("You feel confident, trusting yourself because you studied.")
        pause("Good thing you managed to get some sleep last night, otherwise you would've been too tired to do the test today.")
        print("---------------------------------------------------------------")
        time.sleep(1)
        slow_typing("180 minutes later...", 0.18)
        time.sleep(3)
        pause("You completed your test and triple checked it.")
        pause("You have a good feeling about this.")
        score = random.randint(80,100)
    elif 36 <= stats['academics'] <= 47:
        time.sleep(1)
        pause("you sit down and stare at your paper.")
        pause("It'll be fine right?")
        pause("*You haven't really studied much, you didnt get enough sleep last night either...*")
        print("---------------------------------------------------------------")
        time.sleep(1)
        slow_typing("180 minutes later...", 0.18)
        time.sleep(3)
        print("*sigh*")
        time.sleep(2)
        pause("it wasn't good, but atleast you finished the test :/ ")
        score = random.randint(50,69)
    elif 18 <= stats['academics'] < 36:
        time.sleep(1)
        pause("Its dawning on you now just how much trouble you're in.")
        pause("You sit down and flick through the paper as the timer starts.")
        pause("You honestly wonder if you're even sitting in the correct exam hall.")
        print("---------------------------------------------------------------")
        time.sleep(1)
        slow_typing("180 minutes later...", 0.18)
        time.sleep(3)
        pause("Welp, you definitely failed that.")
        score = random.randint(1,49)
    else:
        time.sleep(1)
        slow_typing("You sit down and as you begin your test, your teacher walks up and writes 100% on your paper just like that. You smile :)*", 0.08)
        time.sleep(1)
        pause("Beside your bed, your mum frowns as she tries to wake you up.")
        time.sleep(1)
        slow_typing("*You were so tired you slept in and didnt show up to the test*", 0.06)
        print("---------------------------------------------------------------")
        time.sleep(1)
        slow_typing("180 minutes later...", 0.1)
        time.sleep(2)
        print("*THUD*")
        time.sleep(1)
        slow_typing("*You fell off your bed!*", 0.06)
        time.sleep(1)
        pause("Atleast you're up now -__-' ")
        score = 0
    return score

score = exam2(stats, teacher1, name)

time.sleep(3)
print("\n\n*It is now the end of the term*")
time.sleep(1)
slow_typing("You have recieved your report...", 0.1)
time.sleep(2)
print('''
--------------------------------------------------------------------
                         [End card]
                  ..........................''')
slow_typing(f"Exam results: Your average is {score}%", 0.05)
time.sleep(2)
print(f"Your stats currently are:")
time.sleep(2)
print(f"Health: {stats['health']}")
time.sleep(0.8)
print(f"Academics: {stats['academics']}")
time.sleep(0.8)
print(f"Social: {stats['social']}")
time.sleep(0.8)
print(f"Safety: {stats['safety']}")
time.sleep(3)
check_stats()
print(f"*End of term 2*")


#term three lol
time.sleep(3)
pause("\n\nYou and your family haven't been overseas in 4 years.")
pause("Your parents haven't met their parents in that long either.")
pause("So your parents have decided to wisk you all off back to your home country. ")
pause("Except they plan on going for 3 months,")
slow_typing(". . .", 0.15)
pause("meaning you'll miss all of term 3.")
pause("You try to talk them out of it, because you don't want to fail school, but they wont have it.")
pause("They refuse to shorten the holiday or leave you behind.")
pause("You have no choice but to go.")
time.sleep(1)
choice = check_valid_input("\nDo you:\na)Pack all your study material with you, so you don't fall too far behind\nb)Pack normally and plan to enjoy your time there\nc)Bring soft copies of all your materials","choose from [a], [b] or [c]",['a', 'b', 'c'])
if choice == 'a':
    stats['academics'] += 20
    stats['health'] += 5
    stats['social'] +=5
    slow_typing("*You pack your books with you*", 0.06)
    time.sleep(2)
    print("--------------------------------------------------------------------")
    slow_typing("                         Holiday time!", 0.06)
    time.sleep(1)
    slow_typing("Back home, you meet your cousins and grandparents and aunties and uncles and great aunties and second cousins..... The list goes on.", 0.04)
    time.sleep(1)
    slow_typing("But you also spend alot of time studying, making sure to stay in contact with your teachers and peers to help keep up with the class", 0.04)
    time.sleep(2)
    print("\n*end of holiday*")
elif choice == 'b':
    stats['academics'] += 5
    stats['health'] += 10
    stats['social'] +=20
    slow_typing("*You pack your clothes and whatnot*", 0.06)
    time.sleep(2)
    print("--------------------------------------------------------------------")
    slow_typing("                         Holiday time!", 0.06)
    time.sleep(1)
    slow_typing("Back home, you meet your cousins and grandparents and aunties and uncles and great aunties and second cousins..... The list goes on.", 0.04)
    time.sleep(1)
    slow_typing("You spend barely any time studying overseas.",0.04)
    time.sleep(1)
    pause("Instead, you spend alot of time with your family and have alot of fun.")
    time.sleep(2)
    print("\n*end of holiday*")
else:
    stats['academics'] += 10
    stats['health'] += 5
    stats['social'] +=10
    time.sleep(1)
    print("--------------------------------------------------------------------")
    slow_typing("                         Holiday time!", 0.06)
    time.sleep(1)
    slow_typing("Back home, you meet your cousins and grandparents and aunties and uncles and great aunties and second cousins..... The list goes on.", 0.04)
    time.sleep(1)
    slow_typing("The internet absoluely sucked though, and you couldn't always access your studying materials.", 0.04)
    time.sleep(1)
    slow_typing("As a result, you didn't study as much as you should have.", 0.04)
    time.sleep(2)
    print("\n*end of holiday*")
    

time.sleep(3)
print("--------------------------------------------------------------------")
pause("You arriveback to Australia during the term break.")
pause("Next term is going to be absolutely hectic, with all your tests, assignment and . . . semester exams >-<")
pause("You have to make the most of these two weeks.")
choice = check_valid_input("\nDo you:\na) Meet up with your friends and catch up\nb) Study like crazy","choose [a] or [b]",['a', 'b'])
if choice == 'b':
    stats['health'] -= 30
    stats['academics'] += 15
    time.sleep(1)
    slow_typing("*You chose to study*", 0.06)
    time.sleep(1)
    slow_typing("You study and you study and you study,", 0.06)
    time.sleep(1)
    pause("You loose sleep and you even end up skipping meals.")
    if stats['health'] < 31:
        time.sleep(1)
        slow_typing(". . .", 0.5)
        time.sleep(1)
        print("*THUD*")
        time.sleep(1)
        slow_typing("*You fainted!*", 0.06)
        time.sleep(1)
        pause("An ambulance is called and you're rushed to the hospital")
    else:
        pause("What a great way to spend your break.")
else:
    slow_typing("You call your friends and agree to meet up at the park.", 0.06)
    time.sleep(1)
    print("--------------------------------------------------------------------")
    slow_typing("                         At the park:", 0.06)
    time.sleep(1)
    pause(f"{name}: Hey guys! It's been too long,")
    pause(f"{madlibs[2]} and {madlibs[3]}: Hi {name}!")
    print(f"{madlibs[3]}: How was your-")
    time.sleep(1)
    slow_typing("Suddenly the wind picks up and you hear-", 0.08)
    print(f"{name}: A CROW!!")
    time.sleep(1)
    choice = check_valid_input("[run] or [stay]","[run] or [stay]",['run', 'stay'])
    if choice == 'run':
        stats['health'] -= 5
        stats['safety'] -= 10
        time.sleep(1)
        print(f"*You grab {madlibs[2]}'s and {madlibs[3]}'s hand and start running*")
        time.sleep(2)
        print(f"{madlibs[3]}: What are you doing!")
        time.sleep(1)
        print(f"{name}: I don't have time to explain, im sorry. But we have to get away from here!")
        time.sleep(3)
        print(f"{madlibs[2]}: What? Are you afraid of crows?")
        time.sleep(2)
        slow_typing("*You ignore their questions and lead them back to your house*", 0.06)
        time.sleep(1)
        slow_typing(". . .", 0.15)
        pause("How are you going to explain this one to them?")
    else:
        stats['safety'] += 10        
        stats['health'] -= 30
        if cricket_bat == 'yes':
            time.sleep(1)
            print("*Instinctively, you grab your cricket bat (that you just happened to have with you),*")
        else:
            print("*Instinctively, you grab your math book aka The Brick (that you just happened to have with you),*")
        time.sleep(3)
        print(f"{name}: Everyone!! Keep your guard up! Something's going to jump out at us!")
        time.sleep(4)
        print(f"{madlibs[3]} and {madlibs[2]}: ...?")
        time.sleep(2)
        print("\nrustle rustle...")
        time.sleep(2)
        print("\nSNAP*")
        time.sleep(1)
        print("""
                      meow??
               /\ _ /\  
             =( • ༝ • )=
               /      \    
""")
        time.sleep(2)
        slow_typing(". . .", 0.06)
        time.sleep(2)
        slow_typing(f"{madlibs[3]}: A cat-", 0.06)
        time.sleep(0.5)
        print("""
     _.._      𓌹  𓌺    EEUUUGGHHHHH.....
    {¬ºཀ°}¬    (꒪ཀ꒪)
      ||       {-}-,
     / \       | |   
""")
        time.sleep(1)
        print(f"{name}: AARRGGHHH!!!")
        pause("You fight off the monsters with your 'weapon'")
        pause(f"Your friends quickly join the fray, brandishing anything they can find. ({madlibs[2]} found a big stick and {madlibs[3]} is just swinging around a bag)")
        slow_typing("These monsters are more bark than bite, and together with your friends, you fight them off", 0.07)
        time.sleep(1)
        if stats['health'] < 31:
            time.sleep(1)
            slow_typing(". . .", 0.5)
            time.sleep(1)
            print("*THUD*")
            time.sleep(1)
            print(f"{madlibs[2]} and {madlibs[3]}: {name}!!")
            time.sleep(1)
            slow_typing("*Your health dropped below 30 and you fainted!*", 0.06)
            time.sleep(1)
            pause("*Your friends call an ambulance and you're rushed to the hospital*")


teacher3 = random.choice(teachers)
time.sleep(3)
pause("\n\nThe term goes by in a blur of tests and assignments.")
pause("You get swept up in the fray...")
print("--------------------------------------------------------------------")
slow_typing("                     One day in class:", 0.06)
time.sleep(1)
pause("*You're all preparing for your semester 2 exams*")
slow_typing(". . .", 0.1)
pause("Or atleast, you're all supposed to be")
pause("It's a study period, what can you expect honestly?")
choice = check_valid_input("\nWhat are you doing?\na) Studying\nb)Studying duh... :)","choose [a] or [b]",['a', 'b'])
if choice == 'a':
    stats['academics'] += 10
    time.sleep(1)
    slow_typing("*You're actually studying...*", 0.06)
    slow_typing("But you can hear some giggling behind you.", 0.06)
    pause("You ignore it and get on with your work.")
    time.sleep(2)
    print("*SPLAT*")
    time.sleep(0.7)
    print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠶⡄⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣤⠤⣤⡀⢀⡗⠒⣧⠴⠋⠚⠉⠙⠳⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡞⢁⣠⡟⠻⣎⠃⢰⠏⠀⠀⠀⠀⠀⠀⢘⣧⣤⣄⡀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⠞⠓⡶⢦⣻⡄⣨⠷⠚⠒⠶⡤⠀⠀⢀⡴⠋⠁⢠⣇⠙⢳⣄⠀
⠀⠀⠀⢠⣞⠁⣠⠶⢧⣄⠈⣿⠳⠶⢤⣀⠀⠈⢩⠴⠟⠛⣯⠙⢳⡌⠻⣯⡘⡆
⠀⠀⢠⠏⢈⡟⠁⢀⣠⣤⠖⣿⡤⣄⣀⠙⢧⣀⣸⡀⠘⣦⡛⢳⡴⠻⣄⠈⠉⠁
⢀⣴⠟⢳⡞⢀⡴⠋⠀⣼⠗⡿⢠⡏⢹⣇⣤⡽⢫⡉⢻⡁⢹⡄⠻⣄⣸⠧⣄⡀
⠘⠶⠖⠋⣠⠟⢙⡶⢺⠷⣴⠛⠺⢦⡾⠐⣾⣇⣼⡇⠀⣟⠋⢷⠀⠈⠳⢤⡤⠇
⠀⠀⠀⣴⠛⣦⠏⠀⣼⣀⡏⠀⠀⣼⠦⣾⠉⡇⠸⠇⠀⢹⣀⣸⡆⠀⠀⠀⠀⠀
⠀⠀⡼⢧⣴⠃⠀⢸⣃⡼⠁⠀⠀⣿⣤⣿⠀⡟⠉⣇⠀⠀⢿⡀⢻⡀⠀⠀⠀⠀
⠀⠸⣇⡼⠃⠀⠀⠀⠉⠀⠀⠀⠀⠹⣤⡿⠀⢿⣠⣿⠀⠀⠀⠙⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
''')
    time.sleep(1)
    print(f"{name}: AAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHDRTYUIKJHGFDSRFYLDTROERPD (ᗒᗣᗕ)՞")
    time.sleep(1)
    slow_typing("*Laughter erupts from the class*", 0.06)
    time.sleep(1)
    slow_typing("*You slowly turn around and glare at all the students*", 0.06)
    time.sleep(1)
    pause("*It's super effective!!")
    pause("The students all look away...")
else:
    stats['health'] += 2
    stats['academics'] -= 5
    time.sleep(1)
    slow_typing(". . .", 0.1)
    time.sleep(1)
    pause("Well if you fail your semesters, you'll know you had it coming ^-^")
    time.sleep(2)
    print("\nclassmate: psst.")
    time.sleep(2)
    print("\nclassmate: PSSTT")
    time.sleep(1)
    pause("You turn to look at him.")
    pause('''He passes you a fake spider and dares you to throw it on the teachers desk.
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠶⡄⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣤⠤⣤⡀⢀⡗⠒⣧⠴⠋⠚⠉⠙⠳⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡞⢁⣠⡟⠻⣎⠃⢰⠏⠀⠀⠀⠀⠀⠀⢘⣧⣤⣄⡀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⠞⠓⡶⢦⣻⡄⣨⠷⠚⠒⠶⡤⠀⠀⢀⡴⠋⠁⢠⣇⠙⢳⣄⠀
⠀⠀⠀⢠⣞⠁⣠⠶⢧⣄⠈⣿⠳⠶⢤⣀⠀⠈⢩⠴⠟⠛⣯⠙⢳⡌⠻⣯⡘⡆
⠀⠀⢠⠏⢈⡟⠁⢀⣠⣤⠖⣿⡤⣄⣀⠙⢧⣀⣸⡀⠘⣦⡛⢳⡴⠻⣄⠈⠉⠁
⢀⣴⠟⢳⡞⢀⡴⠋⠀⣼⠗⡿⢠⡏⢹⣇⣤⡽⢫⡉⢻⡁⢹⡄⠻⣄⣸⠧⣄⡀
⠘⠶⠖⠋⣠⠟⢙⡶⢺⠷⣴⠛⠺⢦⡾⠐⣾⣇⣼⡇⠀⣟⠋⢷⠀⠈⠳⢤⡤⠇
⠀⠀⠀⣴⠛⣦⠏⠀⣼⣀⡏⠀⠀⣼⠦⣾⠉⡇⠸⠇⠀⢹⣀⣸⡆⠀⠀⠀⠀⠀
⠀⠀⡼⢧⣴⠃⠀⢸⣃⡼⠁⠀⠀⣿⣤⣿⠀⡟⠉⣇⠀⠀⢿⡀⢻⡀⠀⠀⠀⠀
⠀⠸⣇⡼⠃⠀⠀⠀⠉⠀⠀⠀⠀⠹⣤⡿⠀⢿⣠⣿⠀⠀⠀⠙⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠴⠃⠀
''')
    choice = check_valid_input("Do you do it?\na) No!\nb) yeah ¬‿¬","choose [a] or [b]",['a', 'b'])
    if choice == 'a':
        stats['social'] -= 3
        stats['safety'] += 2
        time.sleep(1)
        pause("The guy turns away dissapointed")
    else:
        stats['social'] += 3
        time.sleep(1)
        pause("You grab the spider and throw it onto the teachers desk, immediately covering your face with a book afterwards.")
        time.sleep(2)
        print(f"{teacher3}: OOOOOAAAAAHHHHHHHH!!!!")
        time.sleep(1)
        print("class: *laughter*")
        time.sleep(1)
        print(f"{teacher3}: THAT'S IT, YOU'RE ALL STAYING BACK FOR DETENTION!!")
        time.sleep(3)
        print(f"{name}: (ㆆ_ㆆ)")
        time.sleep(1)
        slow_typing(". . .", 0.1)
        time.sleep(1)
        pause("Good one dude")
        
            


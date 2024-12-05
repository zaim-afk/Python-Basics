import time
import random
import os

attributes = {'grades':65, 'energy':65, 'fun':65, 'social':50, 'trouble':0}
teachers = {'english':'', 'maths':'', 'science':'', 'sports':'', 'compsci':''}
suspensions = 0
term = 1

def cl_s():
    cls = input("Press enter, or type cls to clear the screen ")
    if cls == 'cls':
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print()


def slow_text(line, second):
    for letter in line:
        print(letter, end='', flush=True)
        time.sleep(second)


def gender_check():
    global gender
    gender = input("Are you male or female? ").strip().lower()
    while gender != 'male' and gender != 'female':
        gender = input("I said male or female.\n ")
    return gender

def choose_name():
    global name
    name = input("What's your name? ").strip().title()

    no_asked = 0
    name_sure = input(f"Are you sure you want to be named {name}?(y/n) ").strip().lower()
    while name_sure != 'y' and name_sure != 'n':
        name_sure = input(f"I said y/n only.\nI will ask again. Are you sure you want to be named {name}?(y/n) ").strip().lower()
        no_asked += 1
    if no_asked <= 1:
        if name_sure == 'n':
            name = input("What is your corrected name? ").strip().title()
            name_sure = input(f"Do you choose {name}?(y/n) ")
            if name_sure == 'y':
                pass
            elif name_sure == 'n':
                print("🙄🙄🙄")
                name = input("Well then what do you wish to be called? ").strip().title()
                name_sure = input(f"{name}?(y/n) ").strip().lower()
                if name_sure == 'y':
                    print(f"Finally. Hello {name}")
                    print()
                elif name_sure == 'n':
                    time.sleep(1.3)
                    slow_text('...', 0.5)
                    print()
                    time.sleep(0.5)
                    slow_text("You think you're so funny, don't you?", 0.2)
                    print()
                    slow_text("I will ask", 0.3)
                    print()
                    for line in ["One", "More", "Time."]:
                        slow_text(line, 0.4)
                        print()
                        time.sleep(1)
                    print()
                    for line in ["What", "is", "your", "name?"]:
                        slow_text(line, 0.5)
                        print()
                        time.sleep(1.5)
                    name = input("").strip().title()
                    print()
                    print()
                    print()
                    time.sleep(1)
                else:
                    if gender == 'male':
                        print("That's it I'm naming you Abdullah")
                    elif gender == 'female':
                        print("That's it, I'm naming you Fatima")
            else:
                for line in ['...', 'I will ask one more time.', 'What is your name?']:
                    slow_text(line, 0.5)
                    print()
                print()
                name = input('')
    elif no_asked > 1:
        if name_sure == 'y':
            print(f"Thank you.")
        elif name_sure == 'n':
            name = input("I will give you one more chance to choose your name. This will be your final name. \nWhat do you wish to be called? ").strip().title()
    return name

def attributes_change():
    slow_text("Some of your attributes changed!", 0.05)
    print()
    attributes_display

def attributes_display():
    print(f"Your attributes are now:\nGrades: {attributes['grades']}\nEnergy: {attributes['energy']}\nFun: {attributes['fun']}\nSocial: {attributes['social']}\nTrouble: {attributes['trouble']}")

def select_teachers():
    english_teachers = ['Br Michael', 'Sr Jamila', 'Ms Conti', 'Sr Genevieve']
    maths_teachers = ['Br Ateeq', 'Sr Meenu', 'Br Afzal', 'Br Minhaj', 'Br Rizwan']
    science_teachers = ['Br Kareem', 'Br James', 'Br Blake', 'Sr Suzanne', 'Br Frank', 'Br Hadi']
    sports_teachers = ['Br Milan', 'Br Farish', 'Br MK', 'Br Haythem', 'Sr Crystal', 'Ms Fee']
    compsci_teachers = ['Br Nahian', 'Sr Bushra', 'Br Khaled', 'Sr Gulnaz']
    teachers['english'] = random.choice(english_teachers)
    teachers['maths'] = random.choice(maths_teachers)
    teachers['science'] = random.choice(science_teachers)
    teachers['sports'] = random.choice(sports_teachers)
    teachers['compsci'] = random.choice(compsci_teachers)
    return teachers



def first_morning_feelings():
    global nervous
    nervous = ''
    global excite
    excite = ''
    # Nervousness
    nervous = input("It is your first day of school. Are you nervous?(y/n) ").strip().lower()
    while nervous != 'y' and nervous != 'n':
        nervous = input("I said y or n. \nAre you nervous? ").strip().lower()
    if nervous == 'y':
        time.sleep(0.2)
        print("That's alright. Everyone is nervous the first time they do something.")
        attributes['fun'] -= 15
        print(f"Your fun decreased by 15. It is now at {attributes['fun']}.")
    elif nervous == 'n':
        time.sleep(0.2)
        print("Ooh. Confident. Nice.")
    # Excitement
    time.sleep(0.3)
    excite = input("How about excitement. Are you excited?(y/n) ").strip().lower()    
    while excite != 'y' and excite != 'n':
        excite = input("I said y or n.\nAre you excited? ")
    if excite == 'y':
        time.sleep(0.2)
        print("Nice! Time to get ready and leave")
        attributes['fun'] += 15
        time.sleep(0.4)
        print(f"Your fun increased by 15. It is now at {attributes['fun']}.")
    elif excite == 'n':
        print("Nobody likes school on their first day, but it's compulsory, so what can you do? Off to school you go!")
        attributes['fun'] -= 15
        time.sleep(0.4)
        print(f"Your fun decreased by 15. It is now at {attributes['fun']}.")
    if nervous == 'n' and excite == 'n':
        time.sleep(0.5)
        print("Neither nervous nor excited? Well you're going to be *lovely* this year 🙄")
        attributes['energy'] -= 15
        time.sleep(0.4)
        print(f"Your energy decreased by 15. It is now at {attributes['energy']}.")



def breakfast_choice():
    print("It is now breakfast time.")
    time.sleep(0.4)
    options = ['eggs', 'cereal', 'pancakes']
    food = input(f"What do you choose to have for breakfast? Your options are: \n{options} \n ")
    while food not in options:
        food = input(f"I said these are your only options \n{options}\n")
    if food == 'eggs':
        if nervous == 'y':
            slow_text("You go to make scrambled eggs. However, in your nervousness, you end up dropping half the eggs on the floor and they all crack open. Your mother walks in and shouts at you for being careless, then kicks you out the door and tells you to go to school, muttering that she'll have to clean up the mess herself otherwise you'll be late. You complain that you didn't eat yet, so she hands you a protein bar and shuts the door. You head off to school.", 0.1)
            print()
        elif nervous == 'n':
            if excite == 'y':
                print("You decide to make scrambled eggs for breakfast. Due to your excitement, you accidentally end up making the best eggs you've ever tasted. You finish and head off to school.")
            elif excite == 'n':
                print("You go to make scrambled eggs. However, since you are neither nervous nor excited, your blank expression causes you to make the blandest eggs to ever exist. You eat them and then head off to school.")
    elif food == 'cereal':
        if nervous == 'y':
            slow_text("You go to make cereal. However, in your nervousness, you end up spilling half the milk all over the kitchen bench. Your mother walks in and shouts at you for being careless, then kicks you out the door and tells you to go to school, muttering that she'll have to clean up the mess herself otherwise you'll be late. You complain that you didn't eat yet, so she hands you a protein bar and shuts the door. You head off to school.", 0.1)
            print()
        elif nervous == 'n':
            if excite == 'y':
                print("You decide to make cereal for breakfast. Due to your excitement, you accidentally end up making the best cereal you've ever tasted, with gourmet milk and all sorts of exotic fruits. You finish it and head off to school.")
            elif excite == 'n':
                print("You go to make cereal. However, since you are neither nervous nor excited, your blank expression causes you to make the blandest cereal to ever exist. You eat it and then head off to school.")
    elif food == 'pancakes':
        if nervous == 'y':
            slow_text("You go to make pancakes. However, in your nervousness, you end up spilling half the flour all over the kitchen bench. Your mother walks in and shouts at you for being careless, then kicks you out the door and tells you to go to school, muttering that she'll have to clean up the mess herself otherwise you'll be late. You complain that you didn't eat yet, so she hands you a protein bar and shuts the door. You head off to school.", 0.1)
            print()
        elif nervous == 'n':
            if excite == 'y':
                print("You decide to make pancakes for breakfast. Due to your excitement, you accidentally end up making the best pancakes you've ever tasted, with all sorts of berries and delicious syrups. You finish them and head off to school.")
            elif excite == 'n':
                print("You go to make pancakes. However, since you are neither nervous nor excited, your blank expression causes you to make the blandest pancakes to ever exist. You eat them and then head off to school.")


def first_person():
    global person
    global person_choice
    global suspensions
    global principal
    principal = False
    if gender == 'male':
        for line in ['A boy comes up to you and greets you.', '"Hi! My name is Adam."']:
            print(line, end='', flush=True)
            time.sleep(0.2)
            print()
        print()
        time.sleep(0.5)
        for line in ["You look at Adam, and feel like you can do 1 of 3 things:", "(1) Greet him back", "(2) Ignore him", "(3) Punch him"]:
            slow_text(line, 0.07)
            print()
        adam_choice = input('Do you choose 1, 2, or 3? ')
        while adam_choice != '1' and adam_choice != '2' and adam_choice != '3':
            adam_choice = input("I said 1, 2 or 3 ")
        if adam_choice == '1':
            print(f'''You greet Adam back. 
                "Hi Adam!" you say. "I'm {name}".''')
            time.sleep(0.7)
            print(f'Adam says, "Hi {name}! It\'s so nice to meet you!"')
            person = "Adam"
            person_choice = "friend"
            attributes['social'] += 10
            time.sleep(0.2)
            print(f"Your social factor increased! It is now at {attributes['social']}.")
        elif adam_choice == '2':
            print("You look over Adam and scoff.")
            time.sleep(0.2)
            print("You then turn on your heel and walk away.")
            time.sleep(0.5)
            person = "Adam"
            person_choice = "ignore"
            attributes['social'] -= 10
            print(f"Your social factor decreased! It is now at {attributes['social']}")
        elif adam_choice == '3':
            time.sleep(0.5)
            for line in ['You look at Adam, and smile :)', 'You raise your hand as if to high-five him', "He doesn't notice your hand clench into a fist"]:
                slow_text(line, 0.1)
                print()
                time.sleep(0.2)
            print()
            time.sleep(0.5)
            slow_text("With a smile still on your face, you draw back your hand, and Adam thinks you're going to give a big high-five", 0.3)
            print()
            print()
            time.sleep(0.5)
            print("Suddenly,")
            time.sleep(2)
            slow_text("You right hook Adam in the jaw, sending him flying.", 0.05)
            print()
            witness = random.randint(1,100)
            if witness in range(1,11):
                slow_text("You then look around. Surprisingly, and to your relief, no one saw you. You continue on with your day.", 0.075)
                print()
                attributes['fun'] += 10
                print(f"Your fun factor increased! It is now {attributes['fun']}")
            elif witness in range(11,41):
                slow_text("Oh, that felt good.", 0.06)
                print()
                for line in ['You hear cheering, and turn around to see a crowd of students had gathered around you.', "Then the students realise the fight won't continue, so they scatter away"]:
                    slow_text(line, 0.04)
                    print()
                print()
                attributes['social'] += 20
                time.sleep(0.2)
                print(f"Your social factor increased! It is now at {attributes['social']}.")
            elif witness in range(41,61):
                for line in ["You hear cheering, and turn around to see a crowd of students had gathered around you.", "A nearby teacher hears the shouts, and she comes to see what's going on.", "She shoos away all the other kids and looks at you."]:
                    slow_text(line, 0.04)
                    print()
                print()
                time.sleep(2)
                slow_text("The teacher looks at Adam, sprawled out on the floor. Then, she turns to look at you. She looks extremely mad.", 0.7)
                print()
                time.sleep(2)
                for line in ["WHAT IS WRONG WITH YOU??!!", "PUNCHING POOR ADAM IN THE FACE LIKE THAT!!"]:
                    slow_text(line, 0.03)
                    print()
                print()
                time.sleep(3)
                slow_text("I will have to take you to see the principal.", 0.8)
                print()
                attributes['social'] += 20
                attributes['trouble'] += 50
                time.sleep(0.2)
                print(f"Your social factor increased! It is now at {attributes['social']}.")
                time.sleep(0.1)
                print(f"Your trouble factor increased! It is now at {attributes['trouble']}.")
                principal = True
            elif witness in range(61,100):
                for line in [f'"{name.upper()}! WHAT DO YOU THINK YOU\'RE DOING??"', "You turn and see a teacher walking towards you with a mad look on his face.", "Come with me, NOW! We are going straight to the principal."]:
                    slow_text(line, 0.2)
                    print()
                print()
                attributes['trouble'] += 50
                time.sleep(0.2)
                print(f"Your trouble factor increased! It is now at {attributes['trouble']}.")
                principal = True
            person = "Adam"
            person_choice = "punch"
    elif gender == 'female':
        for line in ['A girl comes up to you and greets you.', '"Hi! I\'m Khadijah."']:
            slow_text(line, 0.2)
            print()
        print()
        for line in ["You look at Khadijah, and feel like you can do 1 of 3 things:", "(1) Greet her back", "(2) Make a joke", "(3) Laugh at her"]:
            slow_text(line, 0.03)
            print()
        print()
        khadijah_choice = input("Do you choose 1, 2, or 3? ")
        while khadijah_choice != '1' and khadijah_choice != '2' and khadijah_choice != '3':
            khadijah_choice = input("I said 1, 2, or 3 ")
        if khadijah_choice == '1':
            print(f'''You greet Khadijah back. 
                "Hi Khadijah!" you say. "I'm {name}".''')
            time.sleep(0.7)
            print(f'Khadijah says, "Hi {name}! It\'s so nice to meet you!"')
            person = "Khadijah"
            person_choice = "friend"
            attributes['social'] += 10
            time.sleep(0.2)
            print(f"Your social factor increased! It is now at {attributes['social']}")
        elif khadijah_choice == '2':
            print('"Hi Khadijah! What\'s your name?"')
            for line in ['"Uh, did you just hear yourself?" Khadijah says.', f'"Haha, I\'m just joking. I\'m {name}. It\'s nice to meet you Khadijah."']:
                slow_text(line, 0.05)
                print()
            print()
            person = "Khadijah"
            person_choice = "friend"
            attributes['social'] += 10
            time.sleep(0.2)
            print(f"Your social factor increased! It is now at {attributes['social']}")
        elif khadijah_choice == '3':
            slow_text('You look at Khadijah, point and laugh at her, then turn around and walk away.', 0.05)
            print()
            person = "Khadijah"
            person_choice = "laugh"
            attributes['social'] -= 10
            time.sleep(0.2)
            print(f"Your social factor decreased! It is now at {attributes['social']}")
    if principal == True:
        time.sleep(3)
    else:
        time.sleep(1)
    return person, person_choice, principal

def attributes_check():
    global suspensions
    if suspensions > 0 and suspensions < 3:
        print(f"You have {suspensions} suspensions. {3 - suspensions} more and you will get expelled.")
    if suspensions >= 3:
        attributes['trouble'] += 100
    if attributes['energy'] <= 20:
        print(f"Your energy is extremely low. It is at {attributes['energy']}.")
    if attributes['energy'] <= 0:
        for line in ["Oh no! Your energy reached 0.", "You collapse, and you get taken away to hospital.", "It seems like your journey has ended..."]:
            slow_text(line, 0.3)
            print()
        raise SystemExit
    if attributes['energy'] > 100:
        for line in ["Your energy", "rose", "above 100..."]:
            slow_text(line, 0.3)
            print()
        slow_text("That's biologically impossible, therefore I'm lowering your energy.", 0.2)
        attributes['energy'] = 100
        print()
        print(f"Your energy is now at {attributes['energy']}")
    if attributes ['fun'] <= 20:
        print(f"Your fun value is extremely low. It is at {attributes['energy']}.")
    if attributes['fun'] <= 0:
        for line in ["Oh no! Your fun reached 0.", "You collapse, unwilling to continue with your journey.", "It seems like you must end here..."]:
            slow_text(line, 0.3)
            print()
        raise SystemExit
    if attributes['fun'] > 100:
        for line in ["Your fun", "rose", "above 100..."]:
            slow_text(line, 0.3)
            print()
        slow_text("That's psychologically impossible, therefore I'm lowering your fun.", 0.2)
        attributes['fun'] = 100
        print()
        print(f"Your fun is now at {attributes['fun']}")
    if attributes['grades'] < 50:
        print(f"Your grades dropped below 50. It is at {attributes['grades']}.")
    if attributes['grades'] <= 0:
        for line in ["Your grades", "dropped", "to 0."]:
            slow_text(line, 0.3)
            print()
        time.sleep(2)
        slow_text("You had to drop school due to your trash grades.", 0.3)
        print()
        slow_text("It seems like you must end your journey here...", 0.3)
        raise SystemExit
    if attributes['grades'] > 100:
        for line in ["Your grades", "they rose", "above 100..."]:
            slow_text(line, 0.3)
            print()
        slow_text("That's psychologically impossible, therefore I'm lowering your grades.", 0.2)
        attributes['grades'] = 100
        print()
        print(f"Your grades are now at {attributes['grades']}")
    if attributes['social'] <= 20:
        print(f"Your social factor is extremely low. It is at {attributes['social']}.")
    if attributes['social'] <= 0:
        for line in ["Oh no! Your social factor reached 0.", "You feel alone, unwilling to continue with your journey..."]:
            slow_text(line, 0.6)
            print()
        raise SystemExit
    if attributes['social'] > 100:
        for line in ["Your social factor", "rose", "above 100..."]:
            slow_text(line, 0.3)
            print()
        slow_text("That's emotionally impossible, therefore I'm lowering your social factor.", 0.2)
        attributes['social'] = 100
        print(f"Your social factor is now at {attributes['social']}")
        print()
    if attributes['trouble'] >= 75:
        print(f"You are in a lot of trouble. Your trouble is now at {attributes['trouble']}.")
    if attributes['trouble'] >= 100:
        for line in ["Your trouble has reached the max.", "The teachers have had enough.", "The principal has had enough.", "The students have had enough.", "The principal has no choice but to expel you."]:
            slow_text(line, 0.6)
            print()
        time.sleep(3)
        for line in ["You get expelled from school.", "You come home, and tell your parents.", "They are extremely mad and disappointed in you.", "Your parents ground you for life.", "Your journey has ended..."]:
            slow_text(line, 0.6)
            print()
        raise SystemExit
    if attributes['trouble'] < 0:
        for line in ["Your trouble", "fell", "below 0..."]:
            slow_text(line, 0.3)
            print()
        slow_text("That's spiritually impossible, therefore I'm raising your trouble.", 0.2)
        attributes['trouble'] = 0
        print()
        print(f"Your trouble is now at {attributes['trouble']}")

def principal_office():
    global suspensions
    for line in ["You have 2 options:", "(1) Apologise", "(2) Talk back to the principal"]:
        slow_text(line, 0.2)
        print()
    print()
    choice = input("1 or 2? ")
    while choice != '1' and choice != '2':
        choice = input("I said 1 or 2 ")
    if choice == '1':
        for line in ["You apologise to the principal.", "He accepts your apology, but says you must serve a 5-day suspension."]:
            slow_text(line, 0.15)
            print()
        print()
        attributes['trouble'] -= 25
        time.sleep(0.5)
        print(f"Your trouble decreased! It is now at {attributes['trouble']}.")
        suspensions += 1
    elif choice == '2':
        for line in ["You talk back to the principal.", "He tells you you are being extremely disrespectful. However, you do not care."]:
            slow_text(line, 0.7)
            print()
        print()
        attributes['trouble'] += 50
        time.sleep(0.5)
        print(f"Your trouble increased! It is now at {attributes['trouble']}.")


def skip_class():
    global suspensions
    teacher_catch = random.randint(1,100)
    if teacher_catch in range(1,51):
        print()
        time.sleep(2)
        slow_text('You go to hang out around the lockers.', 0.1)
        print()
        for line in ['You hear your voice being called, so you turn and see.', 'Oh no! A teacher caught you!']:
            slow_text(line, 0.3)
            print()
        print()
        run = input("Do you stay and see what she says, or run away?(stay/run) ").strip().lower()
        while run != 'stay' and run != 'run':
            run = input("I said stay or run.\n").strip().lower()
        if run == 'stay':
            for line in ['You stay, and the teacher comes and grabs you.', 'She demands to know what you were doing.']:
                slow_text(line, 0.3)
                print()
            print()
            lie = input("Do you tell the truth, or lie?(truth/lie) ")
            while lie != 'truth' and lie != 'lie':
                lie = input("I said truth or lie\n")
            if lie == 'truth':
                for line in ["You tell her that you were wagging.", "She is surprised that you actually told her the truth, and for that she just gives you a detention."]:
                    slow_text(line, 0.3)
                    print()
                print()
            elif lie == 'lie':
                for line in ["You tell her that you were just getting something from your locker.", "The teachers looks at you funnily, obviously not believing you.", "She then decides to test you.", 'She tells you, "Ok, take me to your locker and open it for me, if you are telling the truth.', 'Fearful of getting caught, you go to a random locker, and try to guess the code.']:
                    slow_text(line, 0.15)
                    print()
                print()
                locker_code = random.randint(100000,999999)
                locker_guess = int(input("Guess a locker code. It is 6 digits and the first digit is not 0. "))
                if locker_guess == locker_code:
                    time.sleep(5)
                    for line in ['H-How?', 'How did you guess it?', 'There was approximately a 0.0001% chance of figuring out the code.']:
                        slow_text(line, 0.6)
                        print()
                    print()
                    for line in ['The teacher looks surprised and confused. She was so sure you were wagging.', 'She shrugs, defeated, and lets you go.']:
                        slow_text(0.2)
                        print()
                    print()
                else:
                    time.sleep(1)
                    slow_text("You input the code, and ", 0.4)
                    slow_text("...", 0.7)
                    print()
                    slow_text("It obviously fails. How in the world did you think you were going to guess the code? There's approximately a 0.0001% chance of guessing the right code.", 0.1)
                    print()
                    slow_text("The teachers smiles in glee, then straightaway puts on a straight face. She hands you a suspension for wagging and lying to her.", 0.075)
                    print()
                    suspensions += 1
        if run == 'run':
            run_pass = random.randint(1,100)
            if run_pass in range(1,51):
                slow_text("You turn and run. The teacher chases you, but you are too fast for her.", 0.1)
                print()
                slow_text("Phew, that was close.", 0.4)
                print()
                attributes['trouble'] += 25
                time.sleep(1)
                print(f"Your trouble increased! It is now at {attributes['trouble']}")
            elif run_pass in range(51,101):
                slow_text("You turn and run. Then, you trip on a rock. The teacher catches up to you easily and hands you a suspension for wagging and running from her.", 0.075)
                print()
                suspensions += 1


def weekend():
    slow_text("The weekend comes, and you have several options:", 0.05)
    time.sleep(1)
    print()
    weekend_options = slow_text("(1) Study for school\n(2) Go out with friends\n(3) Stay home and play games\n(4) Stay home and rest", 0.06)
    print()
    weekend_choice = input("Do you choose 1, 2, 3 or 4? ").strip()
    while weekend_choice != '1' and weekend_choice != '2' and weekend_choice != '3' and weekend_choice != '4':
        weekend_choice = input("I said 1, 2, 3 or 4 ")
    print()
    if weekend_choice == '1':
        slow_text("You decide to study for school.", 0.05)
        print()
        attributes['grades'] += 20
        attributes['energy'] -= 20
        attributes['fun'] -= 20
        attributes['social'] -= 20
    elif weekend_choice == '2':
        if person_choice == 'friend':
            slow_text(f"You call up {person}, and ask {'him' if person == 'Adam' else 'her' if person == 'Khadijah' else 'them'} to go to the {'park to play soccer.' if person == 'Adam' else 'shops' if person == 'Khadijah' else 'out'}", 0.05)
            print()
            slow_text("He says sure.", 0.05)
            print()
            attributes['grades'] -= 15
            attributes['energy'] -= 10
            attributes['fun'] += 25
            attributes['social'] += 20
        else:
            slow_text(f"You wanted to call a friend to ask to go out. However, the only person you've met at school so far was {person}.", 0.05)
            print()
            time.sleep(2)
            slow_text(f"And of course, you {'ignored him' if person_choice == 'ignore' else 'punched him' if person_choice == 'punch' else 'laughed at her' if person_choice == 'laugh' else 'befriended '}, so you have no friends to go out with 💀💀.", 0.3)
            attributes['grades'] -= 15
            attributes['fun'] -= 20
            attributes['social'] -= 15
    elif weekend_choice == '3':
        slow_text("You stay home to play games. What a sad guy/girl.", 0.1)
        attributes['grades'] -= 25
        attributes['fun'] += 20
        attributes['social'] -= 25
    elif weekend_choice == '4':
        slow_text("You stay home and...do nothing. That's it. You just don't do anything.", 0.1)
        attributes['fun'] -= 10
        attributes['energy'] += 20
    print()
    attributes_change()
    print()
    attributes_check()


def test():
    global suspensions
    global ask_cheat
    ask_cheat = 0
    global help_cheat
    help_cheat = 0
    global caught_cheating
    caught_cheating = 0
    slow_text("Test day comes, and you're feeling you might be ready (or not, I don't know).", 0.05)
    print()
    if attributes['energy'] <= 30:
        slow_text(f"However, your energy is at {attributes['energy']}, so you're feeling quite tired and not up to it.", 0.1)
        print()
        slow_text("Someone looks at you, sees you're tired, then looks away. You don't know why they looked at you...", 0.07)
        print()
        slow_text(f"(After the test): You didn't do so well since you were really tired. You ended up getting {random.randint(20, 55)}% 💀😂😂.", 0.3)
        print()
        attributes['grades'] -= 20
        print(f"Your grades decreased! It is now at {attributes['grades']}")
    else:
        time.sleep(2)
        for line in ["You're in the middle of the test, when you hear a whisper.", f'"{name}...{name}"', "You turn to the source of the whisper."]:
            slow_text(line, 0.07)
            print()
        time.sleep(2)
        slow_text(f"You see a {'boy' if gender == 'male' else 'girl' if gender == 'female' else 'person'} making facial expressions and miming, and you can tell {'he' if gender == 'male' else 'she' if gender == 'female' else 'they'} is asking for the answer to a question ", 0.2)
        time.sleep(2)
        slow_text("(i.e. CHEATING!).", 0.3)
        print()
        if ask_cheat > 0:
            slow_text("You feel a sense of déjà vu.", 0.05)
            print()
            if caught_cheating > 0:
                slow_text(f"However, you've already been caught cheating {caught_cheating} time(s) before. Do you still want to help this time?", 0.07)
        ask_cheat += 1
        cheat = input(f"Do you help {'him' if gender == 'male' else 'her' if gender == 'female' else 'they'}?(y/n) ").strip().lower()
        while cheat != 'y' and cheat != 'n':
            cheat = input("I said y or n only\n")
        if cheat == 'y':
            help_cheat += 1
            catch = random.randint(1,100)
            if catch in range(1,51):
                slow_text(f"You start helping the other student. However, a teacher catches you. (Honestly get better at cheating bro 💀)\nShe suspends you and the other student for cheating and gives you each a 0 on the test.", 0.1)
                caught_cheating += 1
                suspensions += 1
                attributes['grades'] -= 25
                attributes['social'] += 5
            elif catch in range (51,101):
                slow_text("You start helping the other student. Luckily, no one catches you. \nHmm, why are you so good at this 🤨🤨?", 0.1)
                attributes['grades'] += 5
                attributes['social'] += 10
        elif cheat == 'n':
            slow_text(f"You look at the other student, look around and see some teachers, then look back at the other student with an annoyed expression. You choose not to help {'him' if gender == 'male' else 'her' if gender == 'female' else 'them'}.")
            attributes['grades'] += 15
            attributes['social'] -= 5
    attributes_change()
    attributes_check()

def excursion():
    global excursion_destination
    global excursion_go
    excursion_choice = random.randint(1,99)
    if excursion_choice in range(1,34):
        excursion_destination = 'Scitech'
    elif excursion_choice in range(34,67):
        excursion_destination = 'Laser Blaze'
    elif excursion_choice in range(67,100):
        excursion_destination = 'Hoyts'
    slow_text(f"The excursion is going to be at {excursion_destination}.", 0.05)
    print()
    slow_text("Do you wish to go?(y/n)", 0.05)
    excursion_go = input().strip().lower()
    while excursion_go != 'y' and excursion_go != 'n':
        excursion_go = input("I said y/n only ").strip().lower()
    if excursion_go == 'y':
        slow_text(f"You decide to go to {excursion_destination}.", 0.1)
        print()
        attributes['fun'] += 20
        attributes['energy'] -= 20
        attributes['social'] += 20
    elif excursion_go == 'n':
        time.sleep(2)
        slow_text("Okay then 🙄", 0.2)
        print()
        attributes['fun'] -= 20
        attributes['social'] -= 20
    attributes_change()
    attributes_check()

def term_report():
    print('-------------------------------------------')
    print(f'               Term {term} Report               ')
    print('-------------------------------------------')
    print(f'                  {name}                  ')
    print('-------------------------------------------')
    print(f'Grades: {attributes['grades']}')
    print(f'Energy: {attributes['energy']}')
    print(f'Fun: {attributes['fun']}')
    print(f'Social: {attributes['social']}')
    print(f'Trouble: {attributes['trouble']}')
    print('-------------------------------------------')

def new_term():
    global term
    term += 1
    attributes['energy'] = 65
    attributes['fun'] = 65
    attributes['trouble'] = 0
    slow_text(f"It is now Term {term}\nSome of your attributes have changed.", 0.1)
    print()
    attributes_display()
    print()


import os
import time
import random
import threading 
import operator

"""
PROGRESSION SO FAR:
TERM 1 COMPLETE
TEMPORARY ENDING

TO USE FOR THONNY PLEASE TOGGLE COMMENT FOR THE OS.SYSTEM('CLS')
AND TOGGLE COMMENT PRINT("\n\n\n\n\n\n\n\n\n\n")
BELOW
"""

def clear_terminal():
    os.system('cls') #FOR VSC
    # print("\n\n\n\n\n\n\n\n\n\n") #FOR THONNY

def add_random_symbols(s, num_symbols):
    symbols = "!@#$%^&*()-_=+[]{}|;:',.<>?/\~`"
    
    s_list = list(s)
    
    for _ in range(num_symbols):
        symbol = random.choice(symbols)
        position = random.randint(0, len(s_list))
        s_list.insert(position, symbol)
    
    return ''.join(s_list)

def check_stats_inv_input(choice):
    match choice:
        case choice if choice == "stats":
            ourPlayer.show_stats()
        case choice if choice == "inventory":
            ourPlayer.show_inv()
        case _:
            clear_terminal()
            print("That is not a valid option!")
            input("Press [Enter] to continue")

class Player:
    def __init__(self, name):
        self.name = name
        self.stats = {
            "Social": random.randint(40,70),
            "Energy": random.randint(50,75),
            "Grades": random.randint(40,60),
            "Stress": random.randint(0,50),

        }
        self.inventory = {}
        self.term = 1

    def show_stats(self):
        clear_terminal()

        print("STATS:")
        for i in self.stats:
            print(f"{i}: {self.stats[i]}")
        
        input("\nPress [Enter] to continue")
        clear_terminal()

    def show_inv(self):
        clear_terminal()

        if self.inventory:
            print("INVENTORY:")
            for i in self.inventory:
                print(f"{i}: {self.inventory[i]}")
        else:
            print("You have nothing!")
        
        input("\nPress [Enter] to continue")
        clear_terminal()

    def edit_stat(self, stat, amount):
        self.stats[stat] += amount
        if self.stats[stat] > 100:
            self.stats[stat] = 100
        elif self.stats[stat] < 0:
            self.stats[stat] = 0

    def display_term_summary(self):
        clear_terminal()

        print(f"SUMMARY OF TERM {self.term}\n")

        print("STATS:")
        for i in self.stats:
            print(f"{i}: {self.stats[i]}")

        input("\nPress [Enter] to continue")

        self.term += 1

        if self.term > 4:
            self.deter_ending()

    def deter_ending(self):
        clear_terminal()
        print("You're...")
        time.sleep(2)

        social = self.stats["Social"]
        energy = self.stats["Energy"]
        grades = self.stats["Grades"]
        stress = self.stats["Stress"]

        if grades >= 90:
            print("a Top Student!")
            print("Wow! All that hard work paid off huh?")
        elif social >= 90:
            print("a Social Butterfly!")
            print("Popular eh? Enjoyable to chat with are you? Nice work!")
        elif 70 <= grades < 90 and 70 <= social < 90 and stress < 50 and energy > 50:
            print("Well-Rounded!")
            print("Must have been hard managing all of that!")
        elif grades < 40 and social < 40:
            print("a Failure!")
            print("Boo! Were you even trying?")
        elif stress >= 80:
            print("a Stressed Guy!")
            print("Man how do you even become that stressed out??")
        elif energy <= 20:
            print("an Exhausted Guy!")
            print("Didn't get enough sleep? Welcome to Year 11!")
        else:
            print("a Normal Guy.")
            print("Yknow you're a normal guy and that but nothing wrong with that.")
            print("Hey atleast you didn't get the other ending!")

        input("Press [Enter] to continue to the main menu")
        main_menu()

def intro(): #START
    clear_terminal()
    input("Valid options will be enclosed in []\nType [stats] or [inventory] to view them during the game\nPress [Enter] to continue")

    name = ""
    while len(name) == 0 or len(name) > 20:
        clear_terminal()

        print("Welcome to life in Year 11 of AIC!")
        name = input("What is your name?\n>").title().strip()

        if len(name) == 0:
            clear_terminal()
            print("Names cannot be empty!")
            input("Press [Enter] to continue")
        elif len(name) > 20:
            clear_terminal()
            print("Names cannot exceed 20 characters!")
            input("Press [Enter] to continue")
    
    global ourPlayer
    ourPlayer = Player(name=name)

    options = ["visit", 'talk']
    choice = ""

    while choice not in options:
        clear_terminal()

        print(f"Hi {name}! You just returned from the transition break to Year 11 in AIC.")
        print("Known and unknown surrounds you. You feel the dread of school coming back to haunt you.")
        choice = input(f"You look past it, will you [{options[0]}] classes or [{options[1]}] to friends?\n>").strip().lower()

        match choice:
            case choice if choice == options[0]:
                visit_classes()
            case choice if choice == options[1]:
                talk_to_friends()
        check_stats_inv_input(choice)

def visit_classes(): #day 1
    clear_terminal()

    ourPlayer.edit_stat("Social", -10)
    ourPlayer.edit_stat("Energy", -10)
    ourPlayer.edit_stat("Grades", 20)
    ourPlayer.edit_stat("Stress", 10)

    decider = random.randint(1,2)
    
    match decider:
        case 1: #'bad' teacher
            options = ['mess', 'work']
            choice = ""

            while choice not in options:
                clear_terminal()

                print("You are on time for your first class! The teacher starts teaching right away, a misery!")
                choice = input(f"You are unsure of what to do. Will you [{options[0]}] around or [{options[1]}]?\n>").strip().lower()

                match choice:
                    case choice if choice == options[0]:
                        clear_terminal()
                        print("You talked the entire period with your friends.")
                        print("How unproductive!")
                        input("Press [Enter] to continue")
                        end_of_day1(1) #messed around
                    case choice if choice == options[1]:
                        clear_terminal()
                        print("You managed to get a decent amount of work done!")
                        print("How productive!")
                        input("Press [Enter] to continue")
                        end_of_day1(2) #worked in class
                check_stats_inv_input(choice)
        case 2: #'cool' teacher
            print("You are on time for your first class! The teacher seems to be just be a chill guy that doesn't care.")
            print("You are enjoying this class so far and didn't really do any work.")
            input("Press [Enter] to continue")

            end_of_day1(3) #nothing

def talk_to_friends(): #day 1
    clear_terminal()

    ourPlayer.edit_stat("Social", 20)
    ourPlayer.edit_stat("Energy", -5)
    ourPlayer.edit_stat("Grades", -10)
    ourPlayer.edit_stat("Stress", -10)

    options = ['go', 'skip']
    choice = ""

    while choice not in options:
        clear_terminal()

        print("You had a good laugh with your friends. The bell just rang but you are having such a good time with your mates.")
        choice = input(f"Are you going to [{options[0]}] to class or [{options[1]}] class?\n>").strip().lower()

        match choice:
            case choice if choice == options[0]:
                visit_classes()
            case choice if choice == options[1]:
                skipped_class()
        check_stats_inv_input(choice)

def skipped_class(): #day 1
    clear_terminal()

    ourPlayer.edit_stat("Grades", -20)
    decider = random.randint(1,2)

    match decider:
        case 1: #caught skipping class
            
            print("Oh no! You were caught! You were sent home and a meeting with the principal was called.")
            print("Your parents are furious about the incident.")
            input("Press [Enter] to continue")
            end_of_day1(4)
        
        case 2: #got away with skipping class

            print("You successfully skipped class! Have you done this before?")
            print("You head to your next class as the bell rings.")
            input("Press [Enter] to continue")
            end_of_day1(5)

def end_of_day1(case): #day 1
    clear_terminal()

    match case:
        case 1: #messed around in class day 1
            ourPlayer.edit_stat("Social", 10)
            ourPlayer.edit_stat("Energy", 5)
            ourPlayer.edit_stat("Grades", -15)
            ourPlayer.edit_stat("Stress", -10)
        case 2: #worked in class day 1
            ourPlayer.edit_stat("Social", -10)
            ourPlayer.edit_stat("Energy", -5)
            ourPlayer.edit_stat("Grades", +15)
            ourPlayer.edit_stat("Stress", 5)
        case 3: #teacher was cool
            ourPlayer.edit_stat("Social", 10)
            ourPlayer.edit_stat("Energy", 5)
            ourPlayer.edit_stat("Grades", -5)
            ourPlayer.edit_stat("Stress", -10)
        case 4: #caught skipping class
            ourPlayer.edit_stat("Stress", 20)
        case 5: #got away with skipping class
            ourPlayer.edit_stat("Stress", -5)

    options = ['finish']
    choice = ""

    while choice not in options:
        clear_terminal()

        print("After an excruiating amount of time, it's the end of the day.")
        print(f"Finally, its time to end the day and go home.")
        choice = input(f"[{options[0].title()}] the day.\n>").strip().lower()

        match choice:
            case choice if choice == options[0]:
                before_test1()
        check_stats_inv_input(choice)

def before_test1(): #day 2
    clear_terminal()

    options = ['study', 'nah']
    choice = ""

    while choice not in options:
        clear_terminal()

        print("3 weeks later...")
        time.sleep(1)
        print(f"It's the week before the test week! How exciting!")
        choice = input(f"Are you going to [{options[0]}]? Or [{options[1]}]!\n>").strip().lower()

        match choice:
            case choice if choice == options[0]:
                studied_test1()
            case choice if choice == options[1]:

                clear_terminal()

                print("You had a few laughs with your friends over the computer.")
                print("Surely the test will be easy since it's the first one!")
                input("Press [Enter] to continue")

                end_of_day2(1)

        check_stats_inv_input(choice)

def studied_test1(): #day 2
    clear_terminal()

    def studying():
        choice = int()
        correct = False

        while correct == False:
            clear_terminal()

            op = operator.add
            op_str = "+"
            decider = random.randint(1,2)
            match decider:
                case 1:
                    op = operator.add
                    op_str = "+"
                case 2:
                    op = operator.mul
                    op_str = "*"

            number1 = random.randint(1,20)
            number2 = random.randint(1,20)

            print("You decide to do a new practice question.")
            choice = input(f"What's {number1} {op_str} {number2}?\n>").strip().lower()

            match choice:
                case choice if choice.isdigit():
                    if int(choice) == op(number1, number2):
                        correct = True
                        ourPlayer.edit_stat("Social", -2)
                        ourPlayer.edit_stat("Grades", 4)
                        ourPlayer.edit_stat("Stress", -4)

                        clear_terminal()
                        print("Correct!")
                        print("(Social stats have been negatively affected)")
                        input("Press [Enter] to continue")

                    else:
                        clear_terminal()

                        ourPlayer.edit_stat("Social", -2)
                        ourPlayer.edit_stat("Stress", 2)
                        
                        print("Wrong!")
                        print("(Social and Stress stats have been negatively affected)")
                        input("Press [Enter] to try a different question")

                case choice if choice == "stats":
                    ourPlayer.show_stats()
                case choice if choice == "inventory":
                    ourPlayer.show_inv()
                case _:
                    clear_terminal()
                    print("That is not a valid option!")
                    input("Press [Enter] to try a different question")

    studying()

    stopped = False
    options = ['more', 'stop']
    choice = ''

    while stopped == False:
        clear_terminal()

        choice = input(f"Do you want to study [{options[0]}] or [{options[1]}]?\n>").lower().strip()

        match choice:
            case choice if choice == options[0]:
                if ourPlayer.stats["Energy"] >= 10:
                    ourPlayer.stats["Energy"] -= 10
                    studying()
                else:
                    clear_terminal()
                    print("You are too tired to continue studying.")
                    input("Press [Enter] to continue")

                    stopped = True
                    end_of_day2(2)

            case choice if choice == options[1]:
                stopped = True
                end_of_day2(2)
            case choice if choice == "stats":
                ourPlayer.show_stats()
            case choice if choice == "inventory":
                ourPlayer.show_inv()
            case _:
                clear_terminal()
                print("That is not a valid option!")
                input("Press [Enter] to continue")

def end_of_day2(case):

    match case:
        case 1: #didnt study
            ourPlayer.edit_stat("Social", 20)
            ourPlayer.edit_stat("Energy", -5)
            ourPlayer.edit_stat("Grades", -5)
            ourPlayer.edit_stat("Stress", 10)
        case 2: #studied
            ourPlayer.edit_stat("Grades", 5)
            ourPlayer.edit_stat("Stress", -5)

    options = ["sleep", "stay"]
    choice = ""
    
    while choice not in options:
        clear_terminal()
        print("It's night time, time to go sleep!")
        choice = input(f"Are you going to [{options[0]}] or [{options[1]}] up?\n>").lower().strip()

        match choice:
            case choice if choice == options[0]:
                decider = random.randint(1,2)
                match decider:
                    case 1:
                        clear_terminal()
                        ourPlayer.edit_stat("Energy", 50)

                        print("You had an extremely refreshing sleep!")
                        input("Press [Enter] to continue")

                    case 2:
                        clear_terminal()
                        ourPlayer.edit_stat("Energy", 20)

                        print("You got woken up in the middle of the night by your mum!")
                        print("You only got a few hours of sleep in unfortunately")
                        input("Press [Enter] to continue")

                test_term1()

            case choice if choice == options[1]:
                clear_terminal()
                ourPlayer.edit_stat("Energy", -20)

                print("Horrible idea!")
                print("You're literally starting to hallucinate!")
                input("Press [Enter] to continue")

                test_term1()

        check_stats_inv_input(choice)

def test_term1(): #day 3 END OF TERM 1 EVENT
    clear_terminal()

    maxtime = 0
    jumbleness = 0
    number1 = random.randint(1,20)
    number2 = random.randint(1,20)
    number3 = random.randint(1,15)
    number4 = random.randint(1,15)
    number5 = random.randint(1,15)
    number6 = random.randint(1,15)

    questions = {
        1: f"Quick! What is {number1} + {number2}?",
        2: f"Find the area of a rectangle with side lengths {number3} and {number4}.",
        3: f"Find the area of a triangle with a base length of {number5} and height of {number6}"
    }
    
    global score, maxscore
    score = 0
    maxscore = len(questions)

    answers = {
        1: number1 + number2,
        2: number3 * number4,
        3: (1/2) * number5 * number6
    }

    clear_terminal()

    print("After some time, it is week 4, you were having a blast at school but then you realise there is a math test today!")
    print("Your heart sank as you entered the exam hall.")

    grades = ourPlayer.stats["Grades"]

    if grades >= 70:
        print("You feel as you are well prepared though.")
        maxtime = 20
    elif grades >= 50:
        print("You feel like you are not prepared enough.")
        maxtime = 6
    elif grades >= 30:
        print("You feel hopeless inside. You should've studied.")
        maxtime = 3
    elif grades < 30:
        print("You feel dead inside. You're going to fail your first test in Year 11.")
        maxtime = 1.5

    energy = ourPlayer.stats["Energy"]

    if energy <= 20:
        jumbleness += 10
        maxtime *= 0.5
    elif energy <= 40:
        jumbleness += 5
        maxtime *= 0.65
    elif energy <= 60:
        jumbleness += 2
        maxtime *= 0.8

    stress = ourPlayer.stats["Stress"]

    if stress >= 20:
        jumbleness = 4
    elif stress >= 40:
        jumbleness = 8
    elif stress >= 60:
        jumbleness = 16
    elif stress >= 80:
        jumbleness = 32

    input("Press [Enter] to continue.")

    clear_terminal()
    print(f"(You have {maxtime} seconds for each question because of your energy and grades stats)")

    if jumbleness > 0:
        print("(Some questions may appear to be jumbled because of your stress and energy stats)")

    print("The teacher calls to start the test!")
    time.sleep(3)
    print("You open the paper...")
    time.sleep(2)
    print("Get ready...")
    time.sleep(2)

    def get_input():
        nonlocal user_answer
        user_answer = input(">").lower().strip()

    for q in questions:
        clear_terminal()
        print(add_random_symbols(questions[q], jumbleness))
        user_answer = float()

        thread = threading.Thread(target=get_input)
        thread.start()

        starttime = time.time()
        while thread.is_alive() and time.time() - starttime < maxtime:
            time.sleep(0.05)
        
        if thread.is_alive():
            print(f"\nToo slow! The correct answer is {answers[q]}\nPress [Enter] to continue")
            thread.join()
        elif user_answer.replace('.', '', 1).isdigit():
            if abs(float(user_answer) - answers[q]) < 1e-6:
                score += 1
                print("\nCorrect!")
                input("Press [Enter] to continue")
            else:
                print(f"\nWrong! The correct answer is {answers[q]}")
                input("Press [Enter] to continue")
        else:
            print(f"\nWrong! The correct answer is {answers[q]}")
            input("Press [Enter] to continue")
        
    clear_terminal()

    for i in range(score):
        ourPlayer.edit_stat("Stress", -5)

    print("Whew! That's all done for this term")
    print("No more tests!")
    input("Press [Enter] to continue")

    ourPlayer.display_term_summary()

def start_term2(): #day 1 term 2
    clear_terminal()

    print("After a very short break of 2 weeks, you are back to school! Yayy!")
    time.sleep(2)
    print("Oh no. The tests, the results are coming back today!")
    input("Press [Enter] to continue")

    clear_terminal()

    status = "" #failed, passed, aced

    print("You got...")
    time.sleep(1)
    print(f"{score}/{maxscore}")

    if (score/maxscore) == 1:
        print("You passed with flying colours!")
        print("You are relieved to find that you aced the test")
        status = "aced"
        ourPlayer.edit_stat("Stress", -20)

    elif (score/maxscore) >= 0.5:
        print("You passed!")
        print("You felt relieved that you didn't fail")
        status = "passed"
        ourPlayer.edit_stat("Stress", -10)
    else:
        print("You failed.")
        status = "failed"
        ourPlayer.edit_stat("Stress", 20)

    input("Press [Enter] to continue")

    options = ["tell", "hide"]
    choice = ""

    while choice not in options:
        clear_terminal()

        choice = input(f"Are you going to [{options[0]}] your parents or [{options[1]}] it?\n>").lower().strip()

        # match choice:
        #     case choice if choice == options[0]:

        #         match status:
        #             case "aced":
        #                 clear_terminal()

        #                 print("Your parents are ecstatic!")
        #                 print("They reward you with an energy drink! (That's a bit odd)")


        #             case "passed":

        #             case "failed":


        #     case choice if choice == options[1]:

        #         match status:
        #             case "aced":

        #             case "passed":

        #             case "failed":
                        

        # check_stats_inv_input(choice)

def main_menu():

    options = ["play", "quit"]
    choice = ""

    while choice not in options:
        clear_terminal()

        print("  YEAR 11 AIC ")
        print("   By Shafye  ")
        print("-----------------")
        print("     [Play]   ")
        print("     [Quit]   ")

        choice = input("\n>").strip().lower()

        match choice:
            case choice if choice == options[0]:
                intro()
            case choice if choice == options[1]:
                clear_terminal()
                quit()
            case _:
                clear_terminal()
                print(f"That was not a valid option\nValid options include: [{options[0]}] and [{options[1]}]")
                input("Press [Enter] to contiue")

main_menu()
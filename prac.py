import time

def slow_type(text, speed=0.005):
    """Simulates slow typing with a customizable speed (default is 0.2)."""
    for c in text:
        print(c, end='', flush=True)
        time.sleep(speed)


slow_type("Welcome to ✨ Survive Year 11 ✨ a text-based adventure game where you will play as a student and survive 4 treachorous terms of your second-last year!")

grades = 0
aura_points = 0
energy = 0
social_life = 0 



choice = input("Press X for explanation of the game: ").strip().upper()
if choice == "X":
        slow_type("Great! Here's how to play the game:")
        print("- Every term you will have events like tests; you will make decisions in each one & every choice will affect ur attributes")
        slow_type("These attributes are Grades, Energy, Social Life and Aura Points 😎")
        print("You wil get a different ending based on your points~ fun, right?")
        slow_type("A note: In this game, you will be playing a girl. This is non-negotiable 😊")

else: 
      print("You pressed the wrong button... Press X (in capital) to start!")


start_choice = input("\nPress Y to begin your adventure: ").strip().upper()
if start_choice == "Y":
        slow_type("\n🌅 It's a beautiful morning in your neighborhood. The sun is rising, casting a golden glow over the rooftops.")
        time.sleep(3)
        slow_type("The clock shows 6:30 AM. You make some cereal—it's the most important meal of the day.")
        time.sleep(3)
        print("You eat yo breakfast. Once finished, you grab your bag and go out the door.")
        

else:
        print("You pressed the wrong button... Press Y to begin your adventure!")


choice = input("It's time to go to school. Bus, Bike or Walk?").lower()

if choice == "bike":
        print("You put your helmet on (safety first!) and hop on your bike.")
        time.sleep(2)
        print("You can feel the wind blasting on your face.")
        time.sleep(2)
        print("You pedal fast to school and come 10 minutes early.")
        time.sleep(2)
        aura_points+=30
        time.sleep(3)
        print("You gained 50 aura points!")
        print(f"Current Aura Points: {aura_points}")


elif choice == "walk":
        slow_type("You walk to school, taking in the fresh morning atmosphere. You think to yourself what activites will occur today.")
        time.sleep(3)
        print("It's your first day, so you'll have to introduce yourself and make a good impression.")
        time.sleep(3)
        print("You check the time and notice that you might come late..Uhoh..")
        time.sleep(2)
        print("...But you end up arriving to school on time, Thank God!")
        time.sleep(2)
        aura_points+=30
        time.sleep(2)
        print("You gained 30 aura points!")
        print(f"Current Aura Points: {aura_points}")


elif choice == "bus":
        slow_type("The bus arrives outside your house and you hop on.")
        time.sleep(5)
        slow_type("It's crowded inside..")
        time.sleep(3)
        print("But you manage to find a spot at the back.")
        time.sleep(4)
        print("You think about the impression you'll make at your first day of school...")
        time.sleep(5)
        slow_type("New classes..New teachers...everything will change..")
        time.sleep(5)
        slow_type("*CRASHHH* The bus breaks down....great....")
        time.sleep(5)
        print("You run as fast as you can when you reach your destination..")
        time.sleep(6)
        print("You end up slipping accidentally and tripping over..")
        time.sleep(7)
        slow_type("You're not hurt from the fall but you are late.")
        aura_points-=40
        time.sleep(1)
        print(f"You lost 40 aura points ! Yikes-")
        print(f"Current Aura Points: {aura_points}")



else:
    print("Invalid choice! Please select either Bus, Bike, or Walk.")
    


print("You're in class now. You have English first period.") 
player_name = input("Teacher: YEAR 11 STUDENTS! Welcome to your first day 😊 What's your name? ")
print(f"Teacher: Nice to meet you, {player_name}")
time.sleep(3)

choice = input("Teacher: Did you bring your books today? (yes/no):")

if choice == "yes":
        print("Teacher: Excellent! On the right track, I see.")
        grades+=50
        print(f"Current Grade Points: {grades}")
        time.sleep(5)
        print("Teacher: Alright...let's start the lesson")


elif choice == "no":
        print(f"Teacher: *sighs* {player_name}...")
        time.sleep(4)
        print("Get out of my sight 😡")
        grades-=50
        print(f"Current Grade points: {grades}")
        print("Okay so today we'll be learning about-")

else:
        print("Teacher: I'll let it slide today.. Okay so today class..") 


        
print("The class ends. That wasn't so bad. You have Computer Science now.")
time.sleep(5)

print("Teacher: Salam everyone. I'm Brother Zain and I'm gonna be your teacher.")

print("\nBr. Zain: Let's play a quick game to get to know each other! Two Truths and a Lie!")
time.sleep(2)
print("You have to guess which statement is the lie for each person.")


statements = {
    "Fajar": ["My favorite color is yellow", "I'm from India", "I'm learning to code."],
    "Zaki": ["I play soccer", "I can't swim.", "I speak three languages."],
    "Br. Zain": ["I love Python.", "I hate teaching.", "I run a blog for tech lovers"]
}

for person, facts in statements.items():
    print(f"\n{person}'s statements:")
    for i, fact in enumerate(facts, 1):
        print(f"{i}. {fact}")

    while True:  
        try:
            choice = int(input("Which one is the lie? (1/2/3): "))
            if choice < 1 or choice > 3:
                print("Please choose a valid option (1/2/3).")
                continue

            if person == "Fajar" and choice == 2:
                print("Correct! Fajar is actually Pakistani.")
                social_life+=15
                print("You gained 15 social points!")
                print(f"Current Social points: {social_life}")
                break 
            elif person == "Zaki" and choice == 2:
                print("Correct! Zaki is pretty good at swimming.")
                social_life+=15
                print("You gained 15 social points!")
                time.sleep(2)
                print(f"Current Social points: {social_life}")
                break  
            elif person == "Br. Zain" and choice == 2:
                print("Correct! Br. Zain loves teaching.")
                social_life+=15
                print("You gained 15 social points!")
                print(f"Current Social points: {social_life}")
                break  
            else:
                print("Incorrect! Try again.")
        except ValueError:
            print("Invalid. Please enter a number (1/2/3).")
            break



choice3 = input("It's recess time! Will you eat snacks? yes/no: ")

if choice3.lower() == "no":
    print("Wrong choice there, buddy-")
    time.sleep(2)
    print(f"You won't have energy for the rest of the day, {player_name}...")
    energy -= 50
    time.sleep(2)
    print(f"Current Energy Points: {energy}")

elif choice3.lower() == "yes":
    print("As you should be! You need all the nutrition you can get.")
    time.sleep(2)
    print("You gained 50 energy points!")
    energy += 50
    time.sleep(2)
    print(f"Current Energy Points: {energy}")

else:
    print("Invalid choice! Please type 'yes' or 'no' next time.")

            



print("It's math!!")
time.sleep(4)
print("Teacher: Welcome, students. I'm your math teacher.")
time.sleep(5)
print("...today's content is gonna be rough, so be ready!") 
choice4 = input("Did you bring your calculator? yes/no")

if choice4 == "yes":
        print(f"Just as I expect for an ATAR student {player_name}!")
        grades += 50
        print(f"Current Grade points: {grades}")
        

elif choice4 == "no":
        print(f"NO CALCULATOR? YOU ARE IN YEAR 11 NOW, {player_name} I EXPECTED BETTER 🤬 🤬")
        time.sleep(1)
        grades-=5
        print("you lost 5 grade points 💔")
        
        


slow_type("You practice some questions. It's pretty hard...")
time.sleep(6)
choice5 = input("Do you a- Give up, you suck anyways or b- Keep going, it's always hard til it's done. (A/B)").lower()

if choice5 == "A" or "a":
        print("You give up. You feel dumb and cooked for your test already.")
        time.sleep(5)
        print(f"You lost 40 aura points for having a negative mindset! Remember: It's only the first day ")
        time.sleep(3)
        aura_points-=40
        print("Teacher: Class is over. Remember to do the homework tonight.")

elif choice5 == "B" or "b":
        aura_points+=35
        print("You gained 35 aura points for being optimistic!")
        time.sleep(4)
        choice6 = input("Quick quiz! What's 1 + 1?")
        if choice6 == "2":
                print("Correct!")
                grades+= 15
                print(f"Good job {player_name}! You gained 15 points.")
        
        choice = input("What's 4 + 4 x 7 + 3?")
        if choice == "35":
                print("Wow! You are pretty clever.")
                time.sleep(5)
                grades+=20
                print("You gained 20 points!")
                time.sleep(5)
                print(f"Current Grade points: {grades}")
                print("Teacher: Class is over now. Have a good day, and remember to do your hw!")


print("It's our favorite time of the term...")
time.sleep(5)
print("TEXT WEEK!!")
time.sleep(5)
print("English, Math, and Computer Science are coming up!")

print("1. Study and take breaks")
time.sleep(2)
print("2. Skip studying and PARTY >:)")
time.sleep(2)
print("3. Pull an all-nighter")
time.sleep(2)
choice_101 = input("Enter 1, 2, or 3: ")

if choice_101 == "1":
    print("\nYou chose to study, but also take breaks! You gained some grade and social life points >=<")
    grades += 100
    social_life += 70

    print("\nMini-game: Math quiz!")
    time.sleep(3)
    questions = [
        {"question": "What is 3 x 3", "answer": "9"},
        {"question": "What is 5 x 5?", "answer": "25"},
        {"question": "What's 2 x 2?", "answer": "4"}
    ]
    points = 0
    for q in questions:
        user_answer = input(q["question"] + " ")
        if user_answer == q["answer"]:
            print("Correct!")
            points += 10
        else:
            print(f"Wrong {player_name}!")
            points -= 5

    print("\nYour score:", points)
    time.sleep(4)
    print("Day of test: You got A+ for all your tests!")


if choice_101 == "2":
        print("You choose to go to a party.")
        time.sleep(2)
        print("You deserve some fun and studying is useless anyways..")
        time.sleep(2)
        print("...right?")
        social_life+=70
        print("You gained 70 social life points! Woohoo 🎉")
        time.sleep(2)
        print(f"Current Social points: {social_life}")
        time.sleep(1)
        print("Day of the test: You didnt study...")
        time.sleep(1)
        print("You have two options-")
        time.sleep(1)
        choice = input("A- Accept your fate B- Cheat (A/B)")
        if choice0 == "A":
                print("You failed, but you did the right thing by not cheating")
                aura_points+=20
                print("You gained 20 aura points for not cheating!")


        elif choice0 == "B":
                print(".....")
                print("You failed-")
                time.sleep(6)
                print("Womp Womp")
                aura_points-=80
                print(f"You got caught cheating- & lost 80 aura points {player_name}.. (╥﹏╥)")
                time.sleep(3)
                print(f"Current Aura Points: {aura_points}")


elif choice_101 == "3":
    print("\nYou chose to pull an all-nighter!")
    grades += 80
    energy -= 100
    time.sleep(3)
    print("You gained 80 grade points and lost 100 energy")

    print("\nMini-game: Quick Math Quiz!")
    math_questions = [
        {"question": "3 x 4 x 5", "answer": "60"},
        {"question": "100 - x = 21", "answer": "79"},
        {"question": "2y x 3y = 24 ", "answer": "2"}
    ]
    for mq in math_questions:
        user_answer = input(f"What is {mq['question']}? ")
        if user_answer == mq["answer"]:
            print("Correct!")
        else:
            print("Wrong!")

    slow_type("Day of test: You got a good score but started hallucinating during the test...")
    time.sleep(2)
    slow_type("Have you considered therapy?")
    time.sleep(3)
    

print(f"Current Stats:")
time.sleep(3)
print(f"Aura points: {aura_points}")
print(f"Social: {social_life}")
print(f"Grades: {grades}")
print(f"Energy: {energy}")


print("Term 2 has commenced!")


if choice_101 == "1":
        print("Great job last term partner!")



if choice_101 == "2":
        slow_type("You had alot of fun last term jumping on tables at parties and singing...")
        time.sleep(2)
        print("but we need to lock in for Year 11")



if choice_101 == "3":
        print("You worked hard but a little too hard.")
        time.sleep(3)
        print("You need to give yourself some rest with studying.")



slow_type("New term, better you. Last term was just the beginning anyways.")

slow_type("Year 11 is hectic...wouldn't it be fun if you had an extracurricular to look forward to?")

print("1:A sports team") 
print("2: Debate team") 
print("3: Gardening club")

choice_300 = input("Enter the number of your choice: ")

if choice_300 == "1":
    sport_choice = input("Which sport? a) Badminton b) Soccer c) Volleyball: ").lower()
    
    if sport_choice == "a":
        slow_type("An excellent choice! You joined the badminton team.")
        energy -= 5
        aura_points += 5
        slow_type("You enter the gym for badminton. You see your team members talking to each other.")
        print("Someone comes up to you. Do you 1) run away or 2) say hi?")
        choice = input("Press 1 or 2: ")

        if choice == "2":
            print("Person: Hiii! I'm Zoha. Welcome to the Badminton team.")
            slow_type("She hands you a racket and then asks you to play.")
            print('"Sure," you say very nonchalantly.')
            slow_type("You start the match. Zoha is serving.")
            rally_choice = input("Press X or Y to respond: ").lower()

            if rally_choice == "x":
                print("Ouch! You missed.")
            elif rally_choice == "y":
                slow_type("You guys hit the racket back and forth, doing a legendary rally.")
                print("Zoha: Who's gonna win? 🙀")
                slow_type("You scored the first 5 points. Better luck next time, Zoha.")
                slow_type("You serve.")

            choice = input("Press 1 or 2: ")

if choice == "2":
    print("You scored another 5 points!")
    slow_type(f"Zoha: Woah, {player_name}, you're good at this.")
    slow_type("*You two continue another rally. You both end up with 20 points and need only 1 point left.*")
elif choice == "1":
    slow_type("You missed!! You continue the match and she ends up with 20 points while you end up with 15.")
    slow_type(f"Zoha: I think I'm about to win, {player_name}, mwehehehehe")
    print("*Zoha serves*")
    slow_type("You....You....")
    slow_type("You missed!")
    slow_type("Zoha: YIPEE I WON!! :D")
    
    choice = input("Shake her hand (yes/no): ")
    if choice.lower() == "yes":
        slow_type("*You shake her hand and thank her for the fun game.*")
        slow_type(f"Zoha: I loved playing with you today, {player_name}")
        aura_points += 10
        social_life += 20
        slow_type("Zoha: You're gonna have fun in our team <3")
    elif choice.lower() == "no":
        print("Zoha: Oh okay")
        social -= 5
        print("You lost 5 social points-")
        

    elif sport_choice == "b":
        slow_type("Soccer it is! You joined the soccer team.")
        social_life += 15
        energy -= 10
        slow_type("Someone approaches you")
        slow_type("Naimo: Hii I'm Naimo, Captain of the team! So you into soccer?")
        slow_type("*You nod*")
        slow_type("Awesome 😎")
        slow_type("She throws a ball at you and you grab it.")
        slow_type("We're gonna do drills now.")
        print("You kick the ball.")
        slow_type("You scored!")
        print("The two of you play together and you meet the rest of the team.")
        slow_type("Naimo: Good game everyone!") 
        
        
        

    elif sport_choice == "c":
        slow_type("Volleyball sounds fun! You joined the volleyball team.")
        slow_type("You  first do some warm-ups and then practice spiking!") 
        social_life += 10
        energy -= 5
        aura_points += 10
        

    else:
        slow_type("That's not a valid sport option. You missed out on joining a team.")
        aura_points -= 5

elif choice_300 == "2": 
    slow_type("You joined the Debate Team. You gained some aura and social points for doing so.")
    social_life += 15
    aura_points += 20
    slow_type("*You enter the classroom for the debate team. Someone approaches you.*")
    slow_type("HIII I'm Arooj! AKA President of the debate team ^^")
    choice = input("Shake her hand (yes/no)")
    
    if choice == "yes":
                slow_type("*You shake her hand* Arooj: Sooo..your name is?")
                slow_type(f"'I'm {player_name}'")
                slow_type(f"{player_name}? That's a rlly cool name")
                slow_type("Anyways Let's begin!")

    elif choice == "no":
        slow_type("Arooj: Oh okay I guess..")
        aura_points-=5
        print("Let's begin-")
        slow_type("There are two teams and you have an intense debate on climate change")
        slow_type("Arooj: That was fun! It was nice meeting you.")
        print("You gained some social and aura points!")
        social += 15
        aura_points+=20
        
                





        
        



elif choice_300 == "3":
    slow_type("You chose to do the Gardening Club.")
    energy += 20
    aura_points += 20
    slow_type("You gained 20 energy and aura points!")
    slow_type("You enter the schoool garden.")
    slow_type("There is a big glasshouse filled with a beautiful vegetable patch and gorgeous flora.")
    slow_type("There is a tomato plant, where a girl is watering it.")
    slow_type("You come up to her and tell her you're interested in joining the gardening club.")
    slow_type("She turns behind and looks at you. When you mention the gardening club, she gets super excited.")
    print("Person: OMYGOSH U WANNA DO THE GARDENING CLUB!!! YESSSSS! U came to the right place >:)")
    print("Person: Your name?")
    slow_type(f"My name is {player_name}") 

else:
    slow_type("That's not a valid choice. You missed an opportunity to join a team.")


        

print("You had a good time at your chosen extracurricular.")
time.sleep(1)
print("You spend the next few days working on your extracurricular and trying to focus in class")

slow_type("You have your Semester Exams coming up for")
slow_type("English, Math, Politics, CompSci and Chemistry")


print("You come home and enter your room, getting into your pjs")



choice_13 = input("Press 1 if you want to study now, or press 2 if you want to study later: ")
if choice_13 == "1":
    slow_type("You chose to study now. You bring out your English book and practice writing essays.")
    slow_type("After that, you practice some questions for politics and then work on coding for compsci.")
    
    choice = input("Do you want to take a break now? (yes/no): ")
    if choice.lower() == "yes":
        slow_type("You take a break. You have some snacks.")
        
        choice_12 = input("Fruit or Chips? (fruit/chips): ")
        if choice_12.lower() == "fruit":
            slow_type("A healthy and tasty option! You gained some energy points.")
            energy += 25
            slow_type("You gained 25 energy points!")
        elif choice_12.lower() == "chips":
            slow_type("The chips give you some energy at the beginning but make you a bit sluggish later.")
            energy += 15
            slow_type("You gained 15 energy points!")
        else:
            slow_type("Invalid choice. You missed your snack break.")
    else:
        slow_type("You decide to keep working without a break.")
elif choice_13 == "2":
    slow_type("You chose to study later. Time to relax for now.")
else:
    slow_type("Invalid choice. Please try again.")




slow_type(f"Your current energy level is {energy}.") 



        
        

        






                



    
        

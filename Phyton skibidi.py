import random

Stats = {
  "Marks": 10,
  "Social": 10,
  "Energy": 10
}
name = ""

def intro():
  print("Welcome to this simulator game, where you get to experience the life of a year 11 in 2024, you get to make the right decision which will lead you to different ending, here are your stats")
  name = input("What is your name?").strip().title()

  options = ['study', 'skip school', 'talk with friends']
  ActivityChoice =""

  while ActivityChoice not in options:
    
    print(f"This is your first day of Year 11 {name}, arent you excited?, what would you do in your first day, Skip school(reserver energy) Study(Give you higher marks) or Talk with friends(Social up))")

    ActivityChoice = input("Enter your Choice (Study/SKip school/or talk with friends): ").lower().strip()

    if ActivityChoice == "study":
      
      study()
    elif ActivityChoice == "skip school":
      skipschool()

    elif ActivityChoice == "talk with friends":
      talkwithfriends()
    elif ActivityChoice == "stats":
      print(Stats)
    else:
      print("Invalid choice please choose Study, Skip School, or Talk to your friends")
      input("Press [Enter] to continue")

def study():
    print("You choose to study, thats seem kinda boring but okay")
    Stats["Marks"] += 10

    print(Stats) 
    finish()

def talkwithfriends():
    print("You walk up to your friends and catched up after the holiday")
    finish()

def skipschool():
  options = ['Skip school', 'study', 'chat with friends']
  print("seriously first day and youre already skipping school, well your parents already dropped you off, so you would need to escape school somehow do you wish to still skip school, or study or just talk with friends")
  secondchoice = ""
  
  
  while secondchoice not in options:  
    secondchoice = input("Skip school, study, chat with friends").lower().strip()

    if secondchoice == "study":
      print("uhawfhua")
      study()
      break
    elif secondchoice == "skip school":
      x = random.randint(1,100)
      if x < 50:
        print("you got caught and is now being sent back home")
        yougotcaught()
        break
      else:
        print("You succeeded escaping school, do what you want")
        youescaped()
        break
    elif secondchoice == "chat with friends":
      talkwithfriends()
      break
    else :
      print("Invalid choice, please pick skip school, study, or chat with friends")
      print("Press [Enter] to pick again")

def yougotcaught():
  print("Your parents are informed about this and is now coming to school")
  print("Your cordinator is sending you back home, and your parents' are mad at you, they start lecturing you on your way home, and even more when you are home")

  canteatout()

def finish():
  print("After a long exhausting day, your finally going back home, your parents picked you up, now your on your way home")
  print("You arrived home, your parents ask what food you'd like to eat, as you guys are going out to eat, now you are heading out to eat at your favorite restaurant")



def youescaped():
  print("you are now heading back to school to pretend like nothing happened")

  finish()



def canteatout():
  print("You were going to eat out, but since you got in trouble your parents just gave you some leftovers")


print("You are now heading to sleep press[Enter]")


intro()











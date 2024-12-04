import random

# Introduction
def intro():
    print("🎓 Welcome to the Enhanced School Life Simulator! 🎉")
    print("Manage your Energy, Grades, and Social Life across a school year.")
    print("Make friends, go on adventures, and balance it all for a successful year.")
    print("Your choices matter! Are you ready?\n")

# Player class
class Player:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.energy = 100
        self.grades = 50
        self.social = 50

    def update_attributes(self, energy=0, grades=0, social=0):
        self.energy += energy
        self.grades += grades
        self.social += social
        self.energy = max(0, min(100, self.energy))
        self.grades = max(0, min(100, self.grades))
        self.social = max(0, min(100, self.social))

    def display_status(self):
        print(f"\n--- {self.name}'s Current Status ---")
        print(f"Energy: {self.energy}, Grades: {self.grades}, Social Life: {self.social}")

# Random events
def random_event(player):
    events = [
        ("A teacher gave you surprise extra credit!", {"grades": +10}),
        ("You joined a last-minute basketball game and had fun.", {"energy": -10, "social": +15}),
        ("You forgot to study for a pop quiz.", {"grades": -15}),
        ("You went stargazing with friends over the weekend.", {"energy": -10, "social": +20}),
    ]
    event, effects = random.choice(events)
    print(f"🎲 Random Event: {event}")
    player.update_attributes(**effects)

# Conversation events
def conversation_event(player):
    characters = [
        {
            "names": ["Alex", "Taylor"],
            "dialogue": "We're debating whether to study or go to the movies. What do you think?",
            "responses": {
                "Let's study together.": {"grades": +15, "social": +5, "energy": -10},
                "Movies sound fun!": {"social": +15, "energy": -15},
                "I think I’ll do my own thing.": {"social": -5},
            },
        },
        {
            "names": ["Jordan", "Sam"],
            "dialogue": "We're organizing a charity event. Want to help?",
            "responses": {
                "Of course!": {"social": +20, "energy": -10},
                "Sorry, I’m too busy.": {"grades": +5, "social": -5},
                "Maybe next time.": {"social": -5},
            },
        },
    ]

    event = random.choice(characters)
    print(f"\nYou meet {', '.join(event['names'])}. They say: \"{event['dialogue']}\"")
    print("\nYour response? Type your choice exactly:")
    for choice in event["responses"]:
        print(f"\"{choice}\"")

    response = input("\nType your response: ").strip()
    if response in event["responses"]:
        effects = event["responses"][response]
        player.update_attributes(**effects)
        print(f"\nYou said: \"{response}\"")
    else:
        print("Invalid choice. No changes made.")

# Journey events
def journey_event(player):
    print("\n🚀 A new adventure awaits! Where do you want to go?")
    journeys = {
        "Hiking in the mountains (Energy: -30, Grades: +5, Social: +20)": {"energy": -30, "grades": +5, "social": +20},
        "A relaxing beach vacation (Energy: +20, Social: +10)": {"energy": +20, "social": +10},
        "Attend a coding bootcamp (Energy: -20, Grades: +25)": {"energy": -20, "grades": +25},
    }

    for journey in journeys:
        print(f"\"{journey}\"")

    choice = input("\nType your journey: ").strip()
    if choice in journeys:
        effects = journeys[choice]
        player.update_attributes(**effects)
        print(f"\nYou chose: \"{choice}\"")
    else:
        print("Invalid choice. No changes made.")

# Weekend scenarios
def weekend_scenario(player):
    print("\nWhat will you do this weekend?")
    options = {
        "Study for exams (Energy: -20, Grades: +15)": {"energy": -20, "grades": +15},
        "Go to a party (Energy: -30, Social: +20)": {"energy": -30, "social": +20},
        "Relax at home (Energy: +20)": {"energy": +20},
    }

    for option in options:
        print(f"\"{option}\"")

    choice = input("\nType your choice: ").strip()
    if choice in options:
        effects = options[choice]
        player.update_attributes(**effects)
        print(f"\nYou chose: \"{choice}\"")
    else:
        print("Invalid choice. No changes made.")

# Main game loop
def game():
    intro()
    name = input("Enter your name: ").strip()
    gender = input("Are you Male or Female? ").strip().capitalize()
    while gender not in ["Male", "Female"]:
        gender = input("Please choose Male or Female: ").strip().capitalize()

    player = Player(name=name, gender=gender)

    for term in range(1, 5):  # Four terms
        print(f"\n🌟 Term {term} Begins! 🌟")
        for weekend in range(1, 4):  # Three weekends per term
            print(f"\n--- Weekend {weekend} ---")
            weekend_scenario(player)
            conversation_event(player)
            random_event(player)
            journey_event(player)
            player.display_status()

    # Final results and endings
    print("\n🎉 End of the School Year 🎉")
    player.display_status()
    if player.grades > 80 and player.energy > 50 and player.social > 50:
        print("🏆 You mastered the art of balance and had an amazing school year!")
    elif player.grades > 80:
        print("📚 You achieved academic excellence, but your social life suffered.")
    elif player.social > 80:
        print("🎉 You became super popular but neglected your studies.")
    elif player.energy > 80:
        print("💪 You stayed healthy and energetic but missed out academically and socially.")
    else:
        print("😓 You struggled through the year. Better luck next time!")

if __name__ == "__main__":
    game()


# Mini-project (30 min): Build a "Personality Quiz" — ask the user 3–4 questions 
# (name, favorite animal, favorite color, etc.) and print a silly personalized result, like:


#    Hi Sam! Since you love wolves and the color blue,
#    your spirit animal energy is: Calm Nighttime Explorer 🌙


# Wrap-up (10 min): Save the project. Talk through: what's a variable? What does input() do?




quiz = input("Do you want to take the quiz? (yes/no): ").lower()
list = []
list.append(quiz)
print(list)
if quiz == "yes":
    name = input("What's your name? ")
    animal = input("What's your favorite animal? ")
    color = input("What's your favorite color? ")
    hobby = input("What's your favorite hobby? ")

    print(f"\nHi {name}! Since you love {animal} and the color {color},")
    print(f"your spirit animal energy is: {hobby} Enthusiast! 🐾")

else:
    print("No worries! Maybe next time.")
import random

def play():
    secret = random.randint(1, 100)
    guesses = 0
    

    print("I'm thinking of a number between 1 and 100!")

    while True:
        guess = int(input("Your guess: "))
        guesses += 1

        if guess < secret:
            print("Too low! Try again.")
        elif guess > secret:
            print("Too high! Try again.")
        else:
            print(f"You got it in {guesses} guesses! The number was {secret}.")
            break

if __name__ == "__main__":
    play()

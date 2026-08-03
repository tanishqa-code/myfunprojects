import random

CHOICES = ["rock", "paper", "scissors"]

def decide_winner(player, computer):
    if player == computer:
        return "tie"
    beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    return "player" if beats[player] == computer else "computer"

def play():
    player_score = 0
    computer_score = 0

    print("Rock, Paper, Scissors! Type 'quit' to stop.")

    while True:
        player = input("\nrock, paper, or scissors? ").lower()
        if player == "quit":
            break
        if player not in CHOICES:
            print("Please choose rock, paper, or scissors.")
            continue

        computer = random.choice(CHOICES)
        print(f"Computer chose {computer}.")

        result = decide_winner(player, computer)
        if result == "tie":
            print("It's a tie!")
        elif result == "player":
            print("You win!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"Score -> You: {player_score}  Computer: {computer_score}")

    print("\nThanks for playing!")

if __name__ == "__main__":
    play()

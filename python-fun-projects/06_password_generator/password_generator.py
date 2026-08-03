import random
import string
from colorama import Fore, Style, init

init(autoreset=True)

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))

def play():
    print(Fore.CYAN + "Password Generator")
    length = int(input("How long should the password be? "))

    password = generate_password(length)
    print(Fore.GREEN + f"Your new password: {password}")

if __name__ == "__main__":
    play()

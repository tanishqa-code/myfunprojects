def play():
    print("Let's make a silly story! Fill in the blanks.\n")

    adjective = input("An adjective: ")
    noun = input("A noun: ")
    verb = input("A verb (ending in -ing): ")
    animal = input("An animal: ")
    place = input("A place: ")
    number = input("A number: ")

    story = f"""
Once upon a time, there was a {adjective} {noun}.
It loved {verb} with a {animal} at the {place}.
This happened exactly {number} times a day, and everyone thought it was amazing!
"""
    print(story)

if __name__ == "__main__":
    play()

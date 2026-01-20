import random

print("Hi! I am going to try to guess your age.")
name = input("What is your name? ")

tries = 0

while True:
    guess = random.randint(15, 30)
    tries += 1
    answer = input(f"Is your age {guess}? (y/n): ")

    if answer == 'y':
        print(f"{name} is {guess} years old.")
        print(f"It took me {tries} tries!")
        break
    else:
        print("Rats.")

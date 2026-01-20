import random 

print("HI! I am going to try and guess your age")
name = input("What is your name?")

while True: 
    guess = random.randint(15,30)
    answer = input(f"Is your age{guess}? (y/n):")

    if answer == 'y':
        print(f"{name} is {guess} years old")
        break 
    else: 
        print("Rats.")

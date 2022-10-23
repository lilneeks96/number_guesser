import random

n = random.randint(0,20)

print("I am thinking of a number between 0 and 20")

while True:
    try:
        guess_str = input("GUESS WHAT NUMBER ")
        guess = int(guess_str)
        if guess == n:
            print("Well done!")
            running = False
        elif guess < n:
            print("Try a bigger number")
        else:
            print("Try a smaller number")
    except ValueError:
        print("ERROR! Input not in range!")

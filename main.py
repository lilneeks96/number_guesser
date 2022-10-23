import random

n = random.randint(1,10)

print("I am thinking of a number between 1 and 10")

while True:
    try:
        guess_str = input("Enter a number ")
        guess = int(guess_str)
        if guess == n:
            print("Well done!")
            running = False
        elif guess < n:
            print("Try a bigger number")
        else:
            print("Try a smaller number")
    except ValueError:
        print("Please enter a number.")

import random

# Number guessing game
"""---Number guessing game---"""
random_number = random.randint(1,100)
guess = 0
attempts = 0

print("---Number guessing game!---")
print("Rules: \n -A number is picked randomly from 1-100 \n -After you take your guess, The system will tell you higher and lower")

while guess != random_number :
    guess = int(input("What is your guess?:"))
    if guess < random_number :
        print("-->Guess Higher!")
    elif guess > random_number:
        print("-->Guess Lower!")
    attempts = attempts + 1
if guess == random_number:
    print("You Got it! The number was " + str(random_number))
    print("It took you " + str(attempts) + " attempts")

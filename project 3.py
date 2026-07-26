import random

"""===Coin guess game==="""

# Coin flip RNG

print("---Coin flip guess game.---")

# Introductions

print("Rules: \n -You have 10 attempts. \n -You have to guess between Heads and Tails")
print("The Coin has been flipped! Take your guess.")

# Variable starting values
attempts = 1
score = 0

# Coin Values have been set to 1 and 2
while attempts <= 10:
    coin_flip = random.choice(["heads","tails"])
    if coin_flip == "heads":
        coin_flip = ("heads")
    elif coin_flip == "tails":
        coin_flip = ("tails")

    # Guess Input section
    guess = input("What is your guess (Heads/Tails)? ").lower().strip()
    if guess == coin_flip:
        print("You guessed correctly!")
        score = score + 1
    elif guess != coin_flip:
        print("Wrong guess!")
    print("The output was " + coin_flip.capitalize() + ".")
    print("You used " + str(attempts) + " attempts!")
    
    attempts = attempts + 1
print("Your score is " + str(score) + "/10")
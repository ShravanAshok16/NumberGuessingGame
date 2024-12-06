import random
from art import logo
def guessing_number(turn,a):
    while turn > 0:
        print(f"You have {turn} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess>a:
            print ("Too high. Guess again")
        elif guess<a:
            print("Too low. Guess again")
        elif guess==a:
            print(f"You got it! The answer was {a}")
            break
        turn-=1
    if turn==0:
        print(f"You've run out of guesses, The answer was {a}, you lose.")



answer=random.randint(1,100)
print(logo)
print("Welcome to the Number Guessing Game!.")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': \n").lower()
if difficulty == "easy":
    turns=10
else:
    turns=5

guessing_number(turns, answer)
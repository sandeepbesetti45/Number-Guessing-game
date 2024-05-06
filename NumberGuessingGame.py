from random import randint
from art import logo
EASY_LEVEL_TURNS=2
HARD_LEVEL_TURNS=1
def set_difficulty():
    level=input("Choose a difficulty .Type 'easy' or 'hard': ")
    if level=="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def make_guess(guess,answer,turns):
    if answer<guess:
        print("too high")
        return turns-1
    elif answer>guess:
        print("too low")
        return turns-1
    else:
        print(f"you got it the answer is {answer} ")

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer=randint(1,100)
    print(f"the correct answer is {answer}")
    turns=set_difficulty()
    guess=0
    while guess!=answer:
        print(f"you have {turns} attempts remaining to guess  the number. ")
        guess=int(input("Make a guess: "))
        turns=make_guess(guess,answer,turns)
        if turns==0:
            print("you have run out of guesses, you lose. ")
            return
        else:
            print("Guess again")

game()




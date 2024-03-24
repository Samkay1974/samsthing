import random
Guess_number = random.randint(1,100)
print("Welcome to the guess game, Try to guess a number from 1-100 as many times as you want")
tries = 0
while True:
    User_guess = int(input("Guess the number: "))
    tries +=1
    if User_guess>Guess_number:
        print("Guess number too high, try lower")
    elif User_guess< Guess_number and User_guess!=Guess_number:
            print("Almost there,go higher")
    if User_guess == Guess_number:
        print(f"Congratulations! you guessed the number after {tries} tries,what a player!")
        break
    
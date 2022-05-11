logo = """  
  ________                                  ___ ___________
 /  _____/  __ __   ____    ______  ______ |   |\__    ___/
/   \  ___ |  |  \_/ __ \  /  ___/ /  ___/ |   |  |    |   
\    \_\  \|  |  /\  ___/  \___ \  \___ \  |   |  |    |   
 \______  /|____/  \___  >/____  >/____  > |___|  |____|   
        \/             \/      \/      \/                  """

import random
print(logo)

number = random.randint(1, 100)
print("Welcome to number guessing game 🤫\nI am guessing a number between 1 to 100.")
difficulty = input("Chose a dificulty 'easy' or 'hard': ").lower()
if difficulty == "easy":
    attempt = 10
else:
    attempt = 5
while attempt != 0:
    print(f"You have {attempt} attempts remaining")
    guess = int(input("Make a guess : "))
    if guess < number:
        print("Guess higher.")
        attempt -= 1
    if guess > number:
        print("Guess lower.")
        attempt -= 1
    if guess == number:
        print("You have guessed it,cograts! 😊")
        break
if attempt == 0:
    print("You loose 😥")

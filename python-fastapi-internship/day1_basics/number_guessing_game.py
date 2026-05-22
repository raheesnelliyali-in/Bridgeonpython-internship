import random
secret_number = random.randint(1, 50)
while True:
    guess = int (input("Guess the number (1-50);"))
    
    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print("Correct! You guessed it 🎉")
        break
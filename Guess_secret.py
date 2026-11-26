secret_number = 7

while True:
    Guess = int(input("Guess the number: "))

    if Guess > secret_number:
        print("Too high!")
        #print(f"attempt:{attempt}left")
        continue

    elif Guess < secret_number:
        print("Too low!")
        continue

    else:
        print("Correct! You guessed the number.")
        exit()
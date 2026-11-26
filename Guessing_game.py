print("========NUMBER GUESSING GAME==========")

number = 100
attempts = 5

while attempts < 5:
    num = int(input("Guess a number: "))
    
    if num < 1 or num > 100:
        print("Invalid number\nTry again")
        attempts -= 5
        
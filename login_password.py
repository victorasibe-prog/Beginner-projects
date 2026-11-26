Correct_username = "Admin"
Correct_password = "admin"
attempts = 4

for i in range(attempts):
    username = input("Enter username: ")
    attempts -= 1

    if username.strip().lower() != Correct_username.strip().lower():
        print("Invalid username\nTry again")
        print(f"You have {attempts} attempt(s) left!")
        continue
    else:
        break
else:
    print("Too many attempts\nTry again")
    exit()

password_attempts = 4

for i in range (password_attempts):
    password = input("Enter password: ")
    password_attempts -=1
    
    if password.strip().lower() != Correct_password.strip().lower():
        print("Incorrect password\nTry again")
        print(f"{username}, You have {password_attempts} attempt(s) left!")
        continue
    
    else:
        print("log in successfully")
        print(f"welcome, {username}!")
        exit()
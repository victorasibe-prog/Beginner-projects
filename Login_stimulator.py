
correct_username = "admin"
correct_password = 1234

attempts = 0

while attempts < 4:
    username = input("Enter username: ")
    
    if username == correct_username:
        break
    else:
        print("Incorrect username. Try again.")
        attempts += 1
else:
    print("Account locked!")
    exit()
                
attempts = 0

while attempts < 4:
    user_password = int(input("Enter password: "))
    
    if user_password == correct_password:
        print("Login successful!")        
        break
    else:
        print("Incorrect password. Try again.")
        attempts += 1
else:
    print("Account locked!")
    exit()
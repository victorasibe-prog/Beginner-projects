# print("Hello world")

user_input = int(input("Enter your birth year: "))


age = 2026 - user_input

if age <= 13:
    print(f"You are {age}years old. You are a kid!")

elif age <= 20:
    print(f"You are {age}years old. You are a teenager!")

elif age <=65:
    print(f"You are {age}years old. You are an adult!")

else:
    print(f"You are a senior citizen!")
user = int(input("Enter the number of iteration= "))
num = int(input("Enter a number= "))

for i in range(1, user + 1):
    total = i * user
    print(f"{user} * {i} = {total}")
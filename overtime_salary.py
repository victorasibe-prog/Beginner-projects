# Question 11 — Overtime Salary Calculator 💰

# Write a Python function called calculate_salary(hours, rate) that calculates a worker's total salary.

# Rules

# If the worker works 40 hours or less, calculate the salary normally:

# salary = hours × rate
# If the worker works more than 40 hours, the extra hours are considered overtime.
# Overtime hours are paid at 1.5 times the normal hourly rate.
# Calculate the normal pay and overtime pay, then add them together.

# def calculate_salary(hours, rate):

#     if hours <= 40:
#         normal_pay = hours * rate
#         return normal_pay

#     else:
#         overtime_hours = hours - 40
#         normal_pay = 40 * rate
#         overtime_rate = 1.5 * rate
#         overtime_pay = overtime_hours * overtime_rate
#         total = normal_pay + overtime_pay
#         return total


# print(calculate_salary(40, 1000))
# print(calculate_salary(45, 1000))
# print(calculate_salary(50, 2000))
# print(calculate_salary(30, 1500))

# def Happy_birthday(name, age):
#     print(f"Happy Birthday to {name}!")
#     print(f"YOu are {age} years old!")
#     print("Happy Birthday to you!")
#     print()

# Happy_birthday("Joe", 20)
# Happy_birthday("Steve", 50)
# Happy_birthday("Marx", 80)

# def create_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last
# full_name = create_name("Victor", "Asibe")

# print(full_name)


# name = "mercy"
# surname = "adimike"
# age = 30

# full_name = name + " " + surname + " " + "=" + " " +str(age)

# print(full_name.upper()
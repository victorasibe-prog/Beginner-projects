total_bill = float(input("What is the Total Bill: "))
bill_splitters = int(input("How many people splitting the bill?: "))
satisfaction_level = int(input("What is the satisfaction level(choose 1,2,3): "))

if satisfaction_level == 1:
    tip_percentage = 0.05
    print("Bad, 5% tip")

elif satisfaction_level== 2:
    tip_percentage = 0.15
    print("Good, 15% tip")

else:
    tip_percentage = 0.20
    print("Excellent, 20% tip")
    
total_tip = total_bill * tip_percentage
final_bill = total_bill + total_tip
individual_debt = final_bill / bill_splitters

print(f"Total Tip: ${total_tip:.2f}")
print(f"Total Bill (with tip): ${final_bill:.2f}")
print(f"Each person owes: ${individual_debt:.2f}")
#if the bill was 150.00, split between 5 people, with 12% tip.
#each person should pay (150.00 / 5) * 1.12 =33.6
#format the result to 2 decimal places 33.60
print("welcome to the tip calculator")
bill = float(input("what was the total bill? "))

tip = int(input("how much tip would you like to give? 10,15, or 20? "))
people = int(input("how many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"each person should pay: {final_amount}")


## Tip calculator

## 1. Add a welcome greeting message
print("Welcome to the tip calculator!")
## 2. Ask how many people will receive the bill
num_people = int(input("How many people are sharing this bill? "))
## 3. Calculate the total amount of money spent by all people combined
total_amount = float(input("What was the total cost of the meal? $: "))
## 4. Determine how much each person will have to pay
each_person_amt = total_amount / num_people
## 5. Add the percentage tip (15% to the order)
tip_percentage = .15 * each_person_amt
with_tip_amt = (total_amount) * 1.15
individual_amt = with_tip_amt/num_people
## 6. Print out the total amount and the amount of tip to two decimal figures
print(f"The total amount spent on the order before individually dividing into {num_people} people was {with_tip_amt:.2f} $.\n"
      f"The amount that each individual person would have to pay with a 15% included tip would be {individual_amt:.2f} $.")

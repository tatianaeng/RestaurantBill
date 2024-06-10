# Write a program that computes the tax and tip on a restaurant bill.
# The program should ask the user to enter the charge for the meal.
# The tax should be 6.75 percent of the meal charge.
# The tip should be 20 percent of the meal after adding the tax.
# Display the meal charge, tax amount, tip amount, and total bill on the screen.

# variables
tax_percentage = 0.0675
tip_percentage = 0.2

# ask the user to enter the cost for the entire meal (subtotal)
meal_subtotal = float(input("What was the cost for the entire meal? $"))

# calculate the tax
tax_amount = meal_subtotal * tax_percentage

# calculate the tip
tip_amount = (meal_subtotal + tax_amount) * tip_percentage

# calculate the grand total
grand_total = meal_subtotal + tax_amount + tip_amount

# display the meal charge, tax amount, tip amount, and total bill
print(f"\nYour total bill is as follows:\nMeal subtotal: ${meal_subtotal:.2f}\nTax: ${tax_amount:.2f}\nTip: ${tip_amount:.2f}\nGrand total: ${grand_total:.2f}")
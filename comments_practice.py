"""
This file calculates the total price after adding sales tax.
""" 
subtotal = 100

sales_tax_rate = 0.0625 # local sales tax rate (6.25%)

#Calculate the total price including tax 
total = subtotal * (1 + sales_tax_rate)

print(total)

# print("Debug: calculation complete")

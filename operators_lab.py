#Part-1 - Arithmetic
course_fee = 12000
discount_percent = 10
tax_percent = 18

discount_amount = course_fee * discount_percent / 100
price_after_discount = course_fee - discount_amount
tax_amount = price_after_discount * tax_percent / 100
final_price = price_after_discount + tax_amount

print("Discount amount:",discount_amount)
print("Price after discount:",price_after_discount)
print("Tax amount:",tax_amount)
print("Final price after tax:",final_price)

print(2 + 3 * 4)
print((2 + 3) * 4)

#Part-2 - Division operators
students = 23
team_size = 5

print(students / team_size)
print(students// team_size)
print(students % team_size)

#Part-3 - Comparison operators
age = 21 
score = 78

print(age == 21)
print(age != 18)
print(age > 18)
print(age >= 75)
print(age < 90)
print(age <= 78)

#Part-4 - Logical operators
has_completed_basics = True
has_submitted_assignment = True
is_banned = False

eligible_for_next_topic = has_completed_basics and has_submitted_assignment 
needs_attention = (not has_submitted_assignment) or (score < 60)
can_access_course = not is_banned

print(eligible_for_next_topic)
print(needs_attention)
print(can_access_course)

#Part 5 - Truth table check 
print(True and True)
print(True and False)
print(False or True)
print(False or False)
print(not True)
print(not False)

#Part-6 - Assignment shortcuts
practice_score = 50
practice_score += 10
practice_score *= 2

print(practice_score)


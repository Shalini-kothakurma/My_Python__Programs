#part-1 
age = 20 

if age >= 18:
     print("Adult user")
     print("Access granted")

#part-2 if-else
temperature = 25

if temperature > 30:
    print("It's hot!")
else:
    print("Nice weather!")

#part-3 if-elif-else grade chain
score = 95
if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Good job!")
elif score >= 70:
    print("C - Keep it up!")
else:
    print("F - Need improvement")

score = 86
if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Good job!")
elif score >= 70:
    print("C - Keep it up!")
else:
    print("F - Need improvement")

score = 74
if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Good job!")
elif score >= 70:
    print("C - Keep it up!")
else:
    print("F - Need improvement")

score = 55
if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Good job!")
elif score >= 70:
    print("C - Keep it up!")
else:
    print("F - Need improvement")

#logical operators
age = 25
has_license = True
weekend = False
holiday = True
raining = False

can_drive = age >= 18 and has_license
print(f"Can drive: {can_drive}")

is_day_off = weekend or holiday
print(f"Is a day off: {is_day_off}")

suitable_outside = not raining 
print(f"Suitable to go outside: {suitable_outside}")


#part-5 Nested if
has_ticket = True
age = 20
if has_ticket:
    if age >= 18:
        print("Enjoy the movie!")
    else:
        print("Need adult supervision")
else:
    print("Buy a ticket first")

has_ticket = True
age = 15
if has_ticket:
    if age >= 18:
        print("Enjoy the movie!")
    else:
        print("Need adult supervision")
else:
    print("Buy a ticket first")

has_ticket = False
age = 20
if has_ticket:
    if age >= 18:
        print("Enjoy the movie!")
    else:
        print("Need adult supervision")
else:
    print("Buy a ticket first")

#part-5 Debug three common mistake
x = 7
if x > 5:
    print("Big")

x = 5
if x == 5:
    print("Five")

if True:
    print("Hello")       
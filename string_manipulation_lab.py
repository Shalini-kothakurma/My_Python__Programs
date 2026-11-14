first_name = "shalini"
last_name = "kothakurma"
full_name = first_name + " " + last_name

greeting = f"Hello, {full_name}!"

separate = "-" * 30

course_name  = "python programming for ai"
print(course_name.lower())
print(course_name.upper())
print(course_name.title())

messy_name = "  Python Learner  "
cleaned_name = messy_name.strip()
price = "$19.99"
cleaned_price = price.strip("$")

message = "I love Python Programming with Python"
print("Python" in message)
print(message.startswith("I"))
print(message.endswith("Python"))
print(message.find("Python"))
print(message.count("Python"))

new_message = message.replace("Python","AI")

name = "Shalini"
message_without_f = "Hello {name}"
corrected_message = f"Hello {name}"

print(message_without_f)
print(corrected_message)

string1 = "It's Python"
string2 = 'It\'s Python'

print(string1)
print(string2)

raw_text = "  welcome to python programming with python  "
step1 = raw_text.strip()
step2 = step1.title()
step3 = step2.replace("Python", "AI")

print(step3)
print(step3.count("AI"))
# student_records.py

# ---------- Part 2: Student record ----------
student = {
    "name": "Shalini",
    "age": 22,
    "city": "Hyderabad",
    "course": "Python for AI Development"
}
print("Student record:", student)

# ---------- Part 3: Safe lookup ----------
print("get('github'):", student.get("github"))
print("get('github', 'Not provided'):", student.get("github", "Not provided"))

# ---------- Part 4: Dictionary changes ----------
student["email"] = "shalini@example.com"      # add a new key
print("Added key (email):", student["email"])

student["age"] = 23                           # update an existing value
print("Updated age:", student["age"])

student.update({"status": "Active", "grade_level": "Beginner"})   # two values at once
print("Updated status:", student["status"])

del student["email"]                          # remove email using del
print("After del:", student)

removed = student.pop("city")                 # remove city using pop()
print("Value removed using pop():", removed)

# ---------- Part 5: Dictionary inspection ----------
print("keys():", student.keys())
print("values():", student.values())
print("items():", student.items())

# ---------- Part 6: Nested students ----------
students = {
    "S101": {"name": "Anitha", "grade": "B"},
    "S102": {"name": "Ravi", "grade": "A"}
}
selected = students["S101"]
print("Student selected:", selected)
print("Original grade:", students["S101"]["grade"])
students["S101"]["grade"] = "A"
print("Updated grade:", students["S101"]["grade"])

# ---------- Part 7: Debugging ----------
person = {"name": "Shalini"}
print("Safe age lookup:", person.get("age", "Age not available"))

locations = {(17.38, 78.48): "Hyderabad"}     # tuple used as a key
print("Tuple key example:", locations[(17.38, 78.48)])
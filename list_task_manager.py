
# list_task_manager.py
# Assignment 26 - List Operations & Safe Modification Lab

# ---------------------------------------------------------
# Part 1 - Create and access the list
# ---------------------------------------------------------
tasks = ["Install Python", "Create venv", "Learn lists", "Practice Python"]

print("=== Part 1: Create and access ===")
print("First task:", tasks[0])                  # index 0 = first item
print("Last task:", tasks[-1])                  # -1 = last item (negative indexing)
print("First two tasks:", tasks[:2])            # slice: index 0 up to (not including) 2
print("From second item onward:", tasks[1:])    # slice: index 1 to the end

# Part 3 - Inspect and search
# ---------------------------------------------------------
print("\n=== Part 3: Inspect and search ===")

print("Number of tasks:", len(tasks))

if "Learn lists" in tasks:
    print('"Learn lists" exists in the list')
    print("Its index is:", tasks.index("Learn lists"))
else:
    print('"Learn lists" is not in the list')

# A second small list with repeated values
fruits = ["apple", "banana", "apple", "mango", "apple"]
print("Fruits list:", fruits)
print('Count of "apple":', fruits.count("apple"))

# Part 4 - Sort, reverse, and copy
# ---------------------------------------------------------
print("\n=== Part 4: Sort, reverse, and copy ===")

scores = [78, 92, 65, 92, 88, 71]

# 1. Count of 92
print("Count of 92:", scores.count(92))

# 2. Sort (smallest to largest) - changes the list itself
scores.sort()
print("After sort:", scores)

# 3. Reverse (so it is now largest to smallest)
scores.reverse()
print("After reverse:", scores)

# 4. Make a real, separate copy
scores_copy = scores.copy()

# 5. Append 100 ONLY to the copy
scores_copy.append(100)

# 6. Print both and confirm the original did not change
print("Original scores:", scores)
print("Copy scores:    ", scores_copy)
print("Original unchanged?", 100 not in scores)

# Part 5 - Debug three list mistakes
# ---------------------------------------------------------
print("\n=== Part 5: Debugging ===")

# A. Index out of range
# Problem: fruits has only 2 items, so the valid indexes are 0 and 1.
# fruits[2] looks for a 3rd item that does not exist, so Python raises
# IndexError: list index out of range.
fruits_a = ["apple", "banana"]
# print(fruits_a[2])   # <-- this line would crash the program

# Safe approach: check the length first
index = 2
if index < len(fruits_a):
    print(fruits_a[index])
else:
    print("A: Index 2 is out of range. List length is", len(fruits_a))

# B. Modifying a list while looping over it
# Problem: when you remove an item during a for loop, the items after it
# shift left by one position, but the loop keeps moving forward. So it
# skips the next item and some 2s can be left behind.
numbers = [1, 2, 3, 2, 4]

# Safe approach: loop over a COPY, and remove from the original
for n in numbers.copy():
    if n == 2:
        numbers.remove(n)
print("B: numbers after removing all 2s:", numbers)

# (Another safe way: build a new list with a list comprehension)
# numbers = [n for n in numbers if n != 2]

# C. Reference vs copy
# Problem: list2 = list1 does NOT make a new list. Both names point to
# the SAME list in memory, so changing list2 also changes list1.
list1 = [1, 2, 3]
list2 = list1          # same list, two names
list2.append(4)
print("C: list1 after list2.append(4):", list1)   # list1 changed too!

# Correct approach: use .copy() to make a separate list
list1 = [1, 2, 3]
list2 = list1.copy()   # new, independent list
list2.append(4)
print("C: list1 with .copy():", list1)   # unchanged
print("C: list2 with .copy():", list2)


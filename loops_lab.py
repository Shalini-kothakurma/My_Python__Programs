#part-1 Replace repetition with a loop
for i in range(5):
    print("Hello!")

#part-2 Understand range()
for i in range(5):
    print(i)

for i in range(1,6):
    print(i)

for i in range(0,10,2):
    print(i)

for i in range(5,30,5):
    print(i)    

#part-3 Loop through text
word = "Python"

position = 1
for letter in word:
    print(position,letter)
    position = position + 1

#part-4 List preview
colors = ["red", "blue", "green"]

for color in colors:
    print(f"I like {color}")

#part-5 Build a safe while loop
count = 0
while count < 5:
    print(f"Count is {count}")
    count = count + 1
    
#part-7  Final Multiples Challenge
for i in range(3,31,3):
    print(f"Multiple of 3: {i}")
    
    
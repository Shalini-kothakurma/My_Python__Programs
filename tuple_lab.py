

# ---------- Part 1: Create fixed data ----------
location = (17.3850, 78.4867)
rgb_color = (52, 152, 219)

print("location:", location, type(location))
print("rgb_color:", rgb_color, type(rgb_color))
# Why a tuple? A coordinate or RGB value is a fixed set of values that
# should not change by accident, so a tuple (which cannot be changed) fits well.

# ---------- Part 2: Single-item tuple experiment ----------
single = (42,)
not_tuple = (42)

print("single:", single, type(single))
print("not_tuple:", not_tuple, type(not_tuple))
# The comma is what makes a tuple; (42) is just 42 inside brackets.

# ---------- Part 3: Indexing and slicing ----------
print("First value:", rgb_color[0])
print("Last value:", rgb_color[-1])
print("First two values:", rgb_color[:2])

# ---------- Part 4: Tuple unpacking ----------
latitude, longitude = location
red, green, blue = rgb_color

print("Latitude:", latitude)
print("Longitude:", longitude)
print("Red:", red)
print("Green:", green)
print("Blue:", blue)

x = 10
y = 20
print("Before swap: x =", x, ", y =", y)
x, y = y, x
print("After swap: x =", x, ", y =", y)

# ---------- Part 5: Prove immutability ----------
point = (3, 5)

# This line would crash the program, so it is tested safely inside try/except:
try:
    point[0] = 4
except TypeError as error:
    print("Error type:", type(error).__name__)
    print("Error message:", error)

# Approach 1: create a new tuple with the changed value
new_point = (4, point[1])
print("Approach 1 (new tuple):", new_point)

# Approach 2: convert to a list, modify it, convert back to a tuple
temp_list = list(point)
temp_list[0] = 4
converted_point = tuple(temp_list)
print("Approach 2 (list then tuple):", converted_point)
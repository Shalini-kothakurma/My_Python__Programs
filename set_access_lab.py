

# ---------- Part 2: Empty set check ----------
print(type(set()))   # <class 'set'>
print(type({}))      # <class 'dict'>

# ---------- Part 3: Duplicate removal ----------
signups = ["alice", "bob", "alice", "charlie", "bob", "diana"]
print("Original count:", len(signups))      # 6

unique_users = set(signups)
print("Unique users:", unique_users)
print("Unique count:", len(unique_users))   # 4

# ---------- Part 4: remove vs discard ----------
unique_users.remove("bob")                  # bob exists, so this works
print("After remove:", unique_users)

unique_users.discard("unknown_user")        # not in set, no error
print("After discard:", unique_users)

# ---------- Part 5: Access check ----------
print("alice:", "alice" in unique_users)    # True
print("diana:", "diana" in unique_users)    # True

# ---------- Part 6: Order experiment ----------
print("Printed Set:", unique_users)
print("Printed List:", signups)

# ---------- Part 7: Tag uniqueness challenge ----------
tags = ["python", "ai", "python", "ml", "ai", "data"]
print("Original tag count:", len(tags))     # 6

unique_tags = set(tags)
print("Unique tags:", unique_tags)
print("Does python exist?", "python" in unique_tags)   # True

unique_tags.add("deep-learning")
unique_tags.discard("data")
print("Final unique tags:", unique_tags)
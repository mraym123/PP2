age = 17
has_id = True

can_enter = age >= 18 or has_id
print("Can enter:", can_enter)

# AND + NOT
score = 45
min_score = 50

failed = not (score >= min_score)
print("Failed:", failed)

# Boolean в if
if age >= 18 and has_id:
    print("Adult with ID")
elif age >= 18 and not has_id:
    print("Adult without ID")
else:
    print("Minor")
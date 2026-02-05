values = [3, -2, 5, -1, 0, 4]
total = 0

for v in values:
    if v <= 0:
        continue
    total += v
print("Sum of positives:", total)
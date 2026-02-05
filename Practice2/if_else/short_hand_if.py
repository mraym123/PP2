a = 10
b = 5

# Обычный if-else
if a > b:
    max_value = a
else:
    max_value = b

print("Max value:", max_value)

# Short-hand if (одна строка)
max_value = a if a > b else b
print("Max value (short):", max_value)

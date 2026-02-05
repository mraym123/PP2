score = 72
min_score = 60
max_score = 100

# Проверка диапазона
passed = score >= min_score and score <= max_score
print("Passed:", passed)

# Сравнение с порогами
print(score < min_score)
print(score >= min_score)
print(score > max_score)

# Сравнение строк (логин)
username = "admin"
input_username = "Admin"

print(username == input_username)
print(username.lower() == input_username.lower())
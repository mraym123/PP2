with open("example.txt", "r") as file:
    content = file.read()
    print(content)

with open("example.txt", "a") as file:
    file.write("New line append\n")

with open("example.txt", "r") as file:
    print(file.read())
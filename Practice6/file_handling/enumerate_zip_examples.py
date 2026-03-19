# List of student names
names = ["Mustafa", "Usuf", "Asis", "Malik"]

# Corresponding exam scores
scores = [85, 70, 90, 50]

# Corresponding attendance percentages
attendance = [80, 60, 95, 40]

# Loop through all students using enumerate and zip
# enumerate → adds a counter (i), starting from 1
# zip → combines multiple lists into tuples for paired iteration
for i, (name, score, attend) in enumerate(zip(names, scores, attendance), start=1):
    
    # Determine student status based on score and attendance
    if score >= 80 and attend >= 75:
        status = "Excellent"
    elif score >= 60:
        status = "Good"
    else:
        status = "Fail"

    # Print the student's number, name, score, attendance, and status
    print(f"{i}. {name} - {score}, {attend}% → {status}")
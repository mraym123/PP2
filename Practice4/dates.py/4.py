from datetime import datetime

# Ask user for two dates
date1 = input("Enter the first date (YYYY-MM-DD): ")
date2 = input("Enter the second date (YYYY-MM-DD): ")

# Convert strings to datetime objects
d1 = datetime.strptime(date1, "%Y-%m-%d")
d2 = datetime.strptime(date2, "%Y-%m-%d")

# Calculate difference in seconds
diff_seconds = (d2 - d1).total_seconds()

print("Difference in seconds:", diff_seconds)
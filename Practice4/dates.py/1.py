from datetime import date, timedelta
# Get today's date
today = date.today()
# Subtract 5 days
five_days_ago = today - timedelta(days=5)
print("Today's date:", today)
print("Date 5 days ago:", five_days_ago)
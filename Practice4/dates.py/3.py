from datetime import datetime
now = datetime.now()
no_micro = now.replace(microsecond=0)
print("Original time:",now)
print("Time without microseconds:",no_micro)
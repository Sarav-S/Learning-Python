from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

# Creating timedelta
print(timedelta(days=365, hours=10, minutes=0))

# Print today's date
print(date.today())
print(datetime.now())


# Print one year from now
today = date.today()
print("Current date is", today)
print("One year from now will be", str(today + timedelta(days=365)))

# 2 weeks 3 days from now
print("Current date is", today)
print("2 weeks 3 days from now will be", str(today + timedelta(days=3, weeks=2)))

# One year ago
print("Current date is", today)
print("One year ago will be", str(today - timedelta(days=1)))


# Calculate how many days are there for christmas
today       = date.today()
christmas   = date(today.year, 12, 25)

today       = date(today.year, 12, 28)

if today > christmas :
    print("Christmas has already gone past by %d days ago" % ((today - christmas).days))
    christmas = date(today.year + 1, 12, 25)

days_remaining = christmas - today
print("It's just", days_remaining.days, " for christmas")

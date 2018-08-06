

from datetime import date
from datetime import time
from datetime import datetime

def main():
    today = datetime.today()
    print("Today's date is", today)
    
    print("Today's date by date, month, year", today.day, today.month, today.year)

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print("Today is", days[today.weekday()])

    now = datetime.now()
    print("Current time is ", now)


if __name__ == '__main__':
    main()

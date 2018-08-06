from datetime import datetime

def main():
    now = datetime.now()
    
    # Date Formatting
    # %y/%Y - Year
    # %m/%M - Month in integer
    # %b/%B - Month in string
    # %d    - Day of the month
    # %a/%A - Day of the week
    print(now.strftime("Current date is %b %a, %d %m %y"))

    
    # Time Formatting
    # %I/%H - Hours 12/24 format
    # %M    - Minutes
    # %S    - Seconds
    # %p    - AM/PM
    print(now.strftime("Current time is %I:%M:%S %p"))


    # Locale Settings
    # %c    - Locale's date and time
    # %x    - Locale's date
    # %X    - Locale's time
    print(now.strftime("Current date time is %c"))
    print(now.strftime("Current date is %x"))
    print(now.strftime("Current time is %X"))

if __name__ == '__main__':
    main()

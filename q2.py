Year = int(input("Enter Year: "))

if Year%100 == 0:
    if Year%400 == 0:
        print(Year, "is a leap year.")
    else:
        print(Year, "is not a leap year.")
else:
    if Year%4 == 0:
       print(Year, "is a leap year.") 
    else:
        print(Year, "is not a leap year.")
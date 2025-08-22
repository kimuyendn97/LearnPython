#%% determine the day of week of January 1st of a year.
import math
while True:
    year=input("please input the year").strip()
    value_date={
        0:"Sun", 1:"Mon", 2:"Tue", 3:"Wed",
        4:"Thu", 5:"Fri", 6:"Sat"
    }
    try:
        n=int(year) #fomula int() để lấy số nguyên
        value=int((n+math.floor((n-1)/4)-math.floor((n-1)/100)+math.floor((n-1)/400))%7)
        if value in value_date:
            print(f"The day of week of the 1st January of {int(n)} is {value_date[value]}")
        else:
            print(f"can not calcutale, pls re-check the year")
    except ValueError:
        print(f"You entered year is in valid")


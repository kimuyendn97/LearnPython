import math
while True:
    year=input("please input the year").strip()
    value_date={
        0:"Sun", 1:"Mon", 2:"Tue", 3:"Wed",
        4:"Thur", 5:"Fri", 6:"Sat"
    }
    n=float(year)
    value=math.floor((n+math.floor((n-1)/4)-math.floor((n-1)/100)+math.floor((n-1)/400))%7)
    print(f"{value}")
        

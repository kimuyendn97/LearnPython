#%% Advanced: Get the week day of Jan 1st of a give year.
import math

#%% dictionary for weekday
weekday_name={0:"Sun", 1:"Mon", 2:"Tue", 3:"Web", 4:"Thu", 5:"Fri", 6:"Sat"}

#%% Formula to return to the weekday of a given year
def get_weekday_of_jan1(year:int) -> str:
    value= (year+
           math.floor((year-1)/4)
           -math.floor((year-1)/100)
           +math.floor((year-1)/400)) % 7
    return weekday_name[int(value)]

#%% lệnh main
while True: 
    year=input("Please input the year, or enter 'q' to exit").strip()
    if year.lower() == "q":
        print("再见")
        break
    try:
        year_value=int(year)
        weekday=get_weekday_of_jan1(int(year))
        print(f" The 1st Jan of {year} is {weekday}")
    except ValueError:
        print("Invalid input! Please enter a valid year (integer).")


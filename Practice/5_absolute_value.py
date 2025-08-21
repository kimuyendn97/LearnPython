#%% absolute value calculation
import math
while True:
    try:
        value1=float(input("Pls enter the first nummber").strip())
        value2=float(input("Pls enter the second number").strip())
        value3=float(input("Pls enter the third number").strip())
        if abs(value1)<10:
            print(f"{value1} has absolute value less than 10")
        if abs(value2)<10:
            print(f"{value2} has abs less than 10")
        if abs(value3)<10:
            print(f"{value3} has abs less than 10")
        else:
            print("No value has abs less than 10")
            continue
    except ValueError:
        print("invalid number")

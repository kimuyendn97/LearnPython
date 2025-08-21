#%% Quadratic equation
import math
while True:
    try:
        a=float(input("Pls enter a number"))
        b=float(input("Pls enter b number"))
        c=float(input("Pls enter c number"))
        if a == 0:
            print("invalid")
            continue
        else:
            delta=b**2-4*a*c
            if delta>0:
                x1=(-b+math.sqrt(delta))/(2*a)
                x2=(-b-math.sqrt(delta))/(2*a)
                print(f"Two distinct roots: x1 ={x1}, x2={x2}")
            elif delta == 0:
                x=-b/(2*a)
                print(f"One double roots: x={x}")
            else:
                print("No real roots")
    except ValueError:
        print("not valid")

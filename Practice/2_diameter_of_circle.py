#%%
import math
print("Calculation the area of your circle")
while True:
    try:
        diameter=float(input("pls enter the diameter of your circle").strip())
        if diameter<=0:
            print("you entered invalid value")
            continue
        area=(diameter*0.5)**2*math.pi
        print(f"Your area is {area:.2f}")
    except ValueError:
        print("you entered invalid value")
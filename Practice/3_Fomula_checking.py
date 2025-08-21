#%% formula checking
import math
x=[math.pi,math.pi/2,4*math.pi/3] #Dùng dấu [] thay vì {} vì đây là value list, not set list
for x in x: # nếu x nằm trong tập hợp x ở trên
    formula=float(math.cos(x)**2+math.sin(x)**2)
    if formula == 1:
        print(f"{x} formula is true")
    else:
        print(f"{x} formula is false")

#%% tìm max min
import math
while True:
    numbers=input("please enter your numbers, separated by comma")
    number=numbers.split(",")
    set={float(numbers.strip()) for numbers in number}
    print(f"the smallest number is {min(set)}")
    print(f"The highest number is {max(set)}")
    for n in number:
        try:
            float(n)
            continue
        except:
            print(f"The number {n} is invalid")
            continue




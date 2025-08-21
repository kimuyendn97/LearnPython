#%% Enter the numbers you want, separated by commas (,). The program will find the numbers whose absolute values are less than 10.
import math
while True:
    numbers=input("please enter the numbers, separated by comma (,)")
    numbers=numbers.split(",")
    for n in numbers:
        try:# để try-except ngoài vòng lặp for-in để khi bị Value Error thì biết giá trị (n) nào bị error, nếu không sẽ nhảy vào vòng lặp for-in lại và không xác định được giá trị nào bị error.
            value=float(n.strip())
            if abs(value)<10:
                print(f"{value} has abs less than 10")
            else:
                continue
        except ValueError:
            print(f"And there is a letter {n.strip()} in your inputted string") #không để strip() cũng được, có strip để bỏ bớt khoảng trống


    

         
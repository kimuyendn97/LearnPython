#%% tìm max min trong một dãy ký tự. bất kỳ nhập vào. Nếu dãy ký tự chứa chữ thì chỉ check những ký tự là số, ký tự chữ liệt kê ra thành invalid.
import math
while True:
    numbers=input("please enter your numbers, separated by comma").strip().split(",")
    num_set=set()
    notnum_set=set()
    for n in numbers:
        try: 
            float(n)
            num_set.add(float(n))
        except ValueError:
            notnum_set.add(n)
    if num_set:
        print(f"min is {min(num_set)}")
        print(f"max is {max(num_set)}")
    if notnum_set:
        print(f"{notnum_set} is invalid")



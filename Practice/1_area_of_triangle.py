#%%
from colorama import init, Style
init()
#%%
while True:
    try:
       print(Style.BRIGHT + "The area of triangle" + Style.RESET_ALL)
       base=float(input("Pls enter the base").strip())
       height=float(input("Pls enter the height").strip())
       if base<=0 or height <=0:
        print('you entered invalid value')
        continue
       area=0.5*base*height
       print(f"the area of triangle is {area}")
    except ValueError:
       print('you entered invalid value')


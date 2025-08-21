#%% 
rating_meaning={
    0.0:"unacceptable Performance",0.4:"Acceptable Performance",
    0.6:"Meritorious Performance"
}
while True:
    rating = float(input("Pls input the rating").strip())
    if rating == 1:
        print("Bye")
        break

    if rating in rating_meaning:
        print(f"Your performance is {rating_meaning[rating]}")
    elif rating > 0.6:
        print("Your performance is Meritorious Performace")
    else:
        print("Invalid")

# %%

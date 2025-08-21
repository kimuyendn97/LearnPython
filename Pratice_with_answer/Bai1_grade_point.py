# %% Grade point
grade_point={
"A+": 4.0,"A":4.0,
"A-": 3.7,"B+":3.3,
"B":3.0,"B-":2.7,
"C+":2.3,"C":2.0,
"C-":1.7,"D+":1.3,
"D":1.0,"F":0.0
}
#%%
grade = input("Pls input the grade").strip().upper()
#%%
if grade in grade_point:
 print(f"The score of {grade} is {grade_point[grade]}")
else:
 print("not valid, pls write again")
 

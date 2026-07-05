print("PERSONAL POCKET CGPA CALCULATOR")
n=int(input("Number of courses: "))
tp=tu=0
for i in range(n):
    u=int(input(f"Course {i+1} unit: "))
    g=input("Grade(A-F): ").upper()
    if g=="A": p=5
    elif g=="B": p=4
    elif g=="C": p=3
    elif g=="D": p=2
    elif g=="E": p=1
    elif g=="F": p=0
    else:
        print("Invalid"); continue
    tp+=p*u; tu+=u
cgpa=tp/tu
print("CGPA:",round(cgpa,2))
if cgpa>=4.5: print("First Class")
elif cgpa>=3.5: print("Second Class Upper")
elif cgpa>=2.4: print("Second Class Lower")
elif cgpa>=1.5: print("Third Class")
elif cgpa>=1.0: print("Pass")
else: print("Fail")

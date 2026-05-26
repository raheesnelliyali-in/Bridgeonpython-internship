marks=[]
print("\n STUDENT MARKS ANALYSER ")
print("Enter Mark Of 10 Students:")
for i in range(10):
    marks.append(int(input(f"students {i+1}:")))
print(f"All Marks    : {marks}")
highest=max(marks)
print(f"The Highest Mark is    :",highest)
lowest=min(marks)
print(f"The Lowest Mark is    :",lowest)
average=sum(marks)/len(marks)
print("The Average Mark Is    :",average)
unique_marks=[]
[unique_marks.append(m) for m in marks if m not in unique_marks]
print(f"Unique Marks     : {unique_marks}")
above_average=[m for m in unique_marks if m > average]
print(f"Above Average    : {above_average}")
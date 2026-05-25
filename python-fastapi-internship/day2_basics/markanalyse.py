marks=[]
for i in range(5):
    num=int(input(f"Enter Marks of Students {i+1} :"))
    marks.append(num)
largest=max(marks)
print("The Highest Mark Is:",largest)
lowest=min(marks)
print("The Lowest Mark is:",lowest)
average=sum(marks)/len(marks)
print("The Average Mark is:",average)
passed=0
for num in marks:
    if num >= 40:
        passed += 1
print("Students Passed:",passed)

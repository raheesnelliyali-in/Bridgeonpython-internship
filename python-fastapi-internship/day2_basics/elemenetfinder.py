List1=[]
n1=int(input("How Many Elements in First List?:"))
for i in range(n1):
    List1.append(int(input(f"Enter Elements {i+1}:")))
List2=[]
n2=int(input("\nHow Many Elements in Second List?:"))
for i in range(n2):
    List2.append(int(input(f"Enter Elements{i+1}:")))
print("List1:",List1)
print("List2:",List2)
set1=set(List1)
set2=set(List2)
print("set1:",set1)
print("set2:",set2)
common=set1&set2
print("Common Elements:",common)
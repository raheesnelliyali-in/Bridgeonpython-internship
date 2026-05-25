numbers = []
print("Enter 5 numbers one by one:")
for i in range(5):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)
largest = max(numbers)
print("The biggest number is:", largest)
smallest = min(numbers)
print("The smallest number is:",smallest)
total=sum(numbers)
print("total sum of the number is:",total)
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
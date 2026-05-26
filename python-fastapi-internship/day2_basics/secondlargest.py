numbers=[10,20,30,40,50]
largest = numbers[0]
second_largest = numbers[0]
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num != largest and num > second_largest:
        second_largest = num
print("First largest number is:", largest)
print("Second largest number is:", second_largest)
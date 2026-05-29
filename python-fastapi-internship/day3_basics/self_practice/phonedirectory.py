phone_directory = {}
n = int(input("How many contacts? "))
for i in range(n):
    print(f"\n   Contact {i+1} ")
    name = input("Name: ")
    phone = input("Phone: ")
    city = input("City: ")
    phone_directory[name] = { "phone": phone, "city": city}
print("\nPhone Directory:")
for name, details in phone_directory.items():
    print(name, "-> Phone:", details["phone"], ", City:", details["city"])
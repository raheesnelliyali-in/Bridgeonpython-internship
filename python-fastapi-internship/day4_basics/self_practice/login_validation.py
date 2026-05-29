users = {
    "admin": "admin123",
    "sahad": "python123",
    "ravi": "pass123"
}

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print("Invalid username or password")
        print("Attempts left:", attempts)

if attempts == 0:
    print("Account locked. Too many failed attempts.")
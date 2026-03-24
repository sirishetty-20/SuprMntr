 ## 1) Print Password Authentication System

password = input("Create your password:")

if len(password) < 6:
    print("Password is too short, it must have at least 6 characters")

elif password == "":
    print("Password cannot be empty")

else:
    print("Password created successfully")

login = input("Enter your password to login:")

if login == password:
    print("Access granted")
else:
    print("Access denied")
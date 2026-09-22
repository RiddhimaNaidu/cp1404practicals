""" Check Password length and prints the same number of asterisks """
MINIMUM_CHARACTERS = 8
Password = input("Enter your password:")
while len(Password) < 8:
    print("Password should be at least 8 characters long.")
    Password = input("Enter your password:")
print("*" * len(Password))

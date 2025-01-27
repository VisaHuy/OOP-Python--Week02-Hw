password = input("Enter the password to check the strength: ")
if len(password) < 8:
    print("The password weak!!")
elif any(char.isupper() for char in password):
    print("The password is strong!!")
elif any(char.isdigit() for char in password):
    print("The password is strong!!")
elif any(not char.isalnum() for char in password):
    print("The password is strong!!")
else:
    print("The password is Moderate.")
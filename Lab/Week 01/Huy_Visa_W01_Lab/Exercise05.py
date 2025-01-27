string = input("Enter a string: ")
reverse_string = string[::-1]
if reverse_string == string:
    print(string, "is palindrome")
else:
    print(string, "is not palindrome")
print("Reversed string:", reverse_string)

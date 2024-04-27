name = input("write your name: ")
password = input("write your pass: ")
repeat_password = input("repeat your pass: ")
if password == repeat_password:
    print("registered")
else:
    print("repeat your password")
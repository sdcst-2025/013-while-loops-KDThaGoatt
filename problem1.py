##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied

example:
example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 1234
Access denied
Too many failed attempts. Access denied.
"""

username = ""
password = ""
correctUser = False
count = 0

while not correctUser:
    if count > 3:
        print("Too many failed attempts. Access denied")
        break
    username = str(input("Enter your username"))
    password = str(input("Enter your password"))
    if username != "admin" or password != "12345":
        print("Access Denied")
        count = count + 1
    else:
        correctUser = True
        print("Access granted")


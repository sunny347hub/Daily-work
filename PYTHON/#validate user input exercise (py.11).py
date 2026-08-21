#validate user input exercise
#1. username is no more than 12 characters
#2. username must not contain spaces
#3. username must not contain digits
username = input("enter your username: ")
if len(username) > 12:
    print ("user name is more than required length")
elif not username.find(" ") == -1:
    print("username must not contain spaces")
elif not username.isalpha():
    print("username must not contain digits")
else:
    print(f"welcome {username} to our website")

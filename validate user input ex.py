# rules
# useranme is not empty
# username is less than 12 characters
# username must not cantain spaces
# username must not contain special characters
#username must not contain digits
username = input("Enter your username: ")
if len(username) == 0:
    print("Username cannot be empty.")
elif len(username) > 12:
    print("Username must be less than 12 characters.")
elif not  username.find(" ", username)== -1:
    print("Username must not contain spaces.")
elif not username.alpha():
    print("Username must not contain special characters or digits.")


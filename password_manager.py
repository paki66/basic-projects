# function for viewing all passwords
def view():
    f = open('passwords.txt', 'r') 
    for line in f.readlines():
        user, password = line.split(" ")
        print("Username: " + user + " | " + "password: " + password)
    f.close()

# function for adding a password
def add():
    acc_name = input("Enter your account name: ")
    new_password = input("Enter new password: ")
    with open('passwords.txt', 'a') as f:
        f.write(acc_name + " " + new_password + "\n")


while True:
    option = input("Do you want to view passwords or add a new password or quit(v/a/q)?").lower()
    
    if option == "q":
        print("You exited the program!")
        break
    elif option == "v":
        view()
        continue
    elif option == "a":
        add()
        continue
    else:
        print("Invalid option!")
        continue
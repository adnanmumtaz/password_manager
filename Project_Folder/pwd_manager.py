master_pwd = input("Enter your Master Password: ")


def view():
    with open("password.txt", "r") as f:
        for lines in f.readlines():
            data = lines.rstrip()
            user, passw = data.split("|")
            print("User: ", user + " | " + "Password: ", passw)


def add():
    name = input("Enter name: ")
    pwd = input("Enter password: ")

    with open("password.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")


while True:

    choice = input(
        "Enter view to view password, add to add new password or q for quit: "
    ).lower()
    if choice == "q":
        print("Program is quitting!")
        quit()

    if choice == "view":
        view()
    elif choice == "add":
        add()
    else:
        print("Invalid choice!")
        continue

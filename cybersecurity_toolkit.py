import re

while True:
    print("\n=== Cybersecurity Toolkit ===")
    print("1. Password Strength Checker")
    print("2. URL Safety Checker")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        password = input("Enter Password: ")

        score = 0

        if len(password) >= 8:
            score += 1
        if re.search("[A-Z]", password):
            score += 1
        if re.search("[a-z]", password):
            score += 1
        if re.search("[0-9]", password):
            score += 1
        if re.search("[!@#$%^&*()_+=<>?/]", password):
            score += 1

        if score <= 2:
            print("Weak Password")
        elif score <= 4:
            print("Medium Password")
        else:
            print("Strong Password")

    elif choice == "2":
        url = input("Enter Website URL: ")

        if url.startswith("https://"):
            print("Safe Website")
        elif url.startswith("http://"):
            print("Warning: Website is not secure")
        else:
            print("Invalid URL")

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")

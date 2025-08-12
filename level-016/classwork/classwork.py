age = int(input("Enter your age: "))

# შემოწმება ასაკის
if age < 18:
    print("You are kid")
    print("You are adult")

    # მომხმარებლისგან პაროლის შეყვანა
password = input("Enter your password: ")

# პაროლის შემოწმება
if password == "1234":
    print("Password is correct")
    print("Password is incorrect")
    number = float(input("Enter a number: "))

# შემოწმება, არის თუ არა რიცხვი დადებითი
if number > 0:
    print("The number is positive")
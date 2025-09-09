# in ამოწმებს, არის თუ არა კონკრეტული ცხილში
fruits = ["apple", "banana", "cherry", "orange", "grape"]
for fruit in fruits:
     print(fruit)
     
name = ["tato" , "gio","DAVITI"]
user_name = input ("შეიყვანე სახელი: ")

if user_name in name:
    print("შენი სახელი მოხვდა სიაში")
else:
    print("შენი სახელი ვერ მოხვდა სიაში")


nums = [5, 10, 15, 20, 25]
jami = sum(nums)
print("რიცხვების ჯამი არის: ", jami)

user_number = int(input("შეიყვანე რიცხვი: "))
list_numbers = [1, 2, 3, 4, 5]

if user_number in list_numbers:
    print("რიცხვი არის სიაში")
else:
    print("რიცხვი არარის სიაში")
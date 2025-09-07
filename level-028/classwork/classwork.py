# in ამოწმებს, არის თუ არა კონკრეტული ცხილში
fruits = ["apple", "banana", "cherry", "orange", "grape"]
for fruit in fruits:
     print(fruit)
     
name_list = ["ნიკა," "ტატო","გიორგი"]
user_name = input("შეიყვანე შენი სახელი: ")
if user_name in name_list:
    print("მოგესალმები,", user_name + "!")
else:
    print("შენი სახელი სიაში არ მოიძებნა.")

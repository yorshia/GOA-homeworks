for i in range(5):
    print(i)


name=["gio", "giorgi", "yorshia"]
for name in name:
      print(name)

geo=0
for i in range(1, 10):
    geo += i
print("ჯამი:", geo)


i = 1
while i <= 10:
    print(i)
    i += 1


vici= 0
num = 1
while vici< 100:
    vici += num
    num += 1
print("ჯამი : ", vici)



password = "tatooo"
user_input =input("შეიყვანეთ პაროლი: ")

while password != user_input:
    print("wrong password")
    user_input =input("შეიყვანეთ პაროლი: ")

print ("you win")



numbers = []

for i in range(5):
    num = int(input("შეიყვანე რიცხვი: ")) 
    numbers.append(num)

print("შეყვანილი რიცხვებია:", numbers)



extra = int(input("შეიყვანე რიცხვი: "))
numbers.insert(0, extra ** 3)

print("ახალი სია :", numbers)

i = 1
while i < len(numbers):
    numbers.pop(i)
    i += 1 

print("ყოველი მეორე წაშლილის შედეგი:", numbers)

nums = []

while True:
    num = int(input("შეიყვანე რიცხვი (0 რომ შეწყვიტო): "))
    if num == 0:
        break
    nums.append(num)

print("შეყვანილი")
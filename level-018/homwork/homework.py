# for ციკლი გამოიყენება პროგრამირებაში რათა კოდი განმეორებით შესრულდეს რამდენჯერმე# 
for i in range(5):
     print(i)

for I in range(10):
    print(I)
    


for x in range(1,15):
     if x== 13:
         break
     else:
          print(x)

for i in range(3):
    name = input("შეიყვანეთ სახელი: ")
    print("შეყვანილი სახელია:")

    for i in range(10):
     print("თემო")




for i in range(5):
     print("yorshia")
     

ჯამი = 0

for _ in range(5):
    რიცხვი = int(input("შეიყვანე რიცხვი: "))
    ჯამი += რიცხვი  

საშუალო = ჯამი / 5
print("საშუალო არითმეტიკულია:", საშუალო)


number = int(input("შეიყვანე რიცხვი: "))

if number > 0:
    print("რიცხვი დადებითია")
elif number < 0:
    print("რიცხვი უარყოფითია")
else:
    print("რიცხვი ნულია")



     

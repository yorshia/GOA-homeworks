#Boolean არის ლოგიკური მონაცემთა ტიპი რომელსაც მხოლოდ ორი მნიშვნელობა აქვს true-fals

#Binary Code - არის როგორც ბულიონ კოდი ოღონ 1-და 0 ით
print(7 > 2)
print(1 < 9)
print(5 >= 5)
print(3 <= 4)
print(5 == 5)
print(4 != 3)
print(True and False)
print(True and True)
print(False or True)
print(True or False)
print(False and False)


number = int(input("შეიყვანე რიცხვი: "))
if number % 2 == 0 or number % 5 == 0:
    print(True)
else:
    print(False)
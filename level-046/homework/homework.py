
N = int(input("შეიყვანეთ რიცხვი N: "))
for num in range(2, N + 1):
    giogio = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            giogio = False
            break
    if giogio:
        print(num)
import random
print("mogesalmebi gaqvs sami sicocxle warmatebebi")
lives= 3 
level= 2
score= 0
print("mogesalmebi gavs sami sicocle warmatebebr")

lives = 3
level = 2
score = 0

while lives > 0:
    print("sheni done:", level)

    number = random.randint(1, level * 10)
    guess = int(input(f"gamotani ricxvi 1-dan {level * 10}-mde: "))

    if guess == number:
        print("sworia :)")
        score += 10 * level
        level += 1
    else:
        lives -= 1
        print(f"araswori pasuxia {number}")
        print("darchenili sicocleebi:", lives)

print("tamashi dasrulda")
print("sheni qula iyo:", score)
# არგუმენტი არის მნიშვნელობა, რომელსაც ვაწვდით ფუნქციას, როცა მას ვიძახებთ.
# ეს მნიშვნელობა ფუნქციას სჭირდება მუშაობისთვის

# raing- ქმნის როიცხვების მიმდევრობას



for i in range(50, 101):
 print(i)



for i in range(100, 201):

     print(i)
 

#  for -მუშაობს განმეორებით  რამდენს რაოდენობასაც მივუთითებთ
#ხოლო while იქამდე მუშაობს სანამ სწორია პორპბა


i = 1  # ვიწყებთ 1-დან

while i <= 10:  
    print(i)    
    i += 1      

    # password="2009"
    # user_input=input("გთხოვთ შეიყვანე პასვორდი")
    # while password !=user_input:
    #    print("პაროლი არასწორია ცადე თავიდან")
    #    user_input=input("გთხოვ შეიყვანე პაროლი სწორად")
    #    print("პაროლი არის სწორი")


       
secret_number = 5  

while True:
    user_input = int(input("შეიყვანე რიცხვი 1-დან 10-ის ჩათვლით: "))
    
    if user_input == secret_number:
        print("You Win!")
        break  
    else:
        print("Wrong number")

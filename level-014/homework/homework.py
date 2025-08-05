#ალგორითმი ნიშნავს ნაბიჯნაბიჯ ინსტრუქციას რაც გვეხმარება ამოცანის ან პრობლემის გადაჭრაში
#შეგიძლია იფიქრო ალგორითმზე როგორც რეცეპტზე  მაგალითად როგორ უნდა გავაკეთო სენდვიჩი
#Sequencing- ეს თანმივდერობით ასრულებს კოდს
# Iteration- ნიშნავს ერთი ან მეტი ნაბიჯის გამეორებას, სანამ რაიმე პირობა შესრულდება ან განსაზღვრული რაოდენობით
# Selection-ნიშნავს გადაწყვეტილების მიღებას  არჩევას სხვადასხვა გზას შორის რაიმე პირობის მიხედვით
# Flowchart – სურათი, რომელიც აჩვენებს ნაბიჯებს
#ფლოჩარტი (flowchart) არის ნაბიჯების ნახატი.
# Pseudocode-ეს არის პროგრამინების ენით დაწერილი პროგრამის ენასთან მიახლოვებული
#Natural Language-ჩვეულებრივი ინგლისურით




#The program asks how old you are.
#If you are younger than 18, it says: "You are a child."
#If you are 18 or older, it says: "You are an adult."
# Ask the user to enter their age
age = int(input("Enter your age: "))

# Check if the age is less than 18
if age < 18:
    print("You are a child")
else:
    print("You are an adult")

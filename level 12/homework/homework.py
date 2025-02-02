#integer

a = 5       # დადებითი მთელი რიცხვი
b = -10     # უარყოფითი მთელი რიცხვი
c = 0       # ნულოვანი მთელი რიცხვი
d = 123456  # დიდი მთელი რიცხვი
e = -987654 # დიდი უარყოფითი მთელი რიცხვი

#string

name = "irakli"            # სტრიქონი, სახელის მაგალითი
greeting = "GAUMARJOS !!!" # სტრიქონი, greeting ტექსტი
age = "18"                 # სტრიქონი, თუმცა ციფრი, მაგრამ ტექსტური სახით
message = "...."           # სტრიქონი, ტექსტი
empty = ""                 # ცარიელი სტრიქონი

#float

pi = 3.14         # გლუვი რიცხვი, ათწილადებით
temperature = -5.5 # უარყოფითი რიცხვი ათწილადებით
height = 175.2     # ადამიანის სიმაღლე (მეტრებში)
price = 199.99     # პროდუქტის ფასი (დოლარები)
weight = 70.5      # წონა (კილოგრამი)

#როდის გვჭირდება მონაცემთა ტიპის კონვერტაცია:
#მიღებული მონაცემების შესაბამისობაში მოყვანისას როცა ვიღებთ მონაცემებს ერთ ტიპში, მაგრამ ოპერაციებისთვის ან გამოყენებისთვის მათ სხვა ტიპში გარდაქმნა გჭირდებათ. მაგალითად:
#თუ მომხმარებელმა შეიყვანა რიცხვი ტექსტად (სტრიქონად), მაგრამ ეს რიცხვი უნდა გამოიყენოთ თუ არა მათემატიკური ოპერაციებისთვის, მაშინ უნდა გარდაქმნათ ის int ან float ტიპში.


# შემოვიტანოთ სამი ადამიანის ასაკები
age1 = int(input("შეიყვანეთ პირველი ადამიანის ასაკი: "))
age2 = int(input("შეიყვანეთ მეორე ადამიანის ასაკი: "))
age3 = int(input("შეიყვანეთ მესამე ადამიანის ასაკი: "))

# გამოთვალოთ ასაკების ჯამი
total_age = age1 + age2 + age3

# გამოთვალოთ საშუალო არითმეტიკული
average_age = total_age / 3

# გამოვიყვანოთ შედეგი
print(f"სამი ადამიანის საშუალო ასაკია: {average_age}")



# მომხმარებლის ასაკის შეყვანა
age = int(input("შეიყვანეთ თქვენი ასაკი: "))

# გამოთვლა, რამდენი წლის იქნება 20 წელში
age_in_20_years = age + 20

# შედეგის დაბეჭდვა
print(f"20 წელში თქვენ იქნებით {age_in_20_years} წლის.")


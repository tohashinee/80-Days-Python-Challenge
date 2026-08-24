# Chall 3 - Build a simple grade evaluator (input percentage → output letter grade) using nested if-else conditionals.
percentage = int(input("Enter percentage: "))
if percentage >=80  and percentage <= 100:
    print("A*")
elif  percentage >= 70 and percentage <=80:
    print("A")
elif percentage >=50 and percentage <=70:
    print("B")
elif percentage >= 40 and percentage <=50:
    print("C")
elif percentage<40:
    print("Fail !")
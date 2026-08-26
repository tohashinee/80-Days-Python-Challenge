#Challenge 4 - Sieve of Erathosnese
n = int(input("Enter integer: "))
Numbers = []
for i in range(n+1):
    if i ==0 or i ==1:
        continue
    else:
        Numbers.append(i)

index = 0
while True:
    for i in Numbers:
        if i % Numbers[index] ==0 and i!=Numbers[index]:
            Numbers.remove(i)
    index +=1
    if (Numbers[index] * Numbers[index]) > n :
        break

print(Numbers)
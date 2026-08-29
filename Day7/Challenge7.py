#Sum of Array Elements (GFG)
#for loop
Numbers = [2,3,4,5,6,7,8,9]
total = 0
for i in Numbers:
    total = total + i
print(total)

#index loop
total = 0
index = 0
while index <= 7:
    total = total + Numbers[index]
    index +=1
print(total)


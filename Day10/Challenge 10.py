#Find Minimum and Maximum Element in an Array (GFG) — Implement manual comparison logic without using min() or max().
numbers = [6,7,2,3,100,4,8,11]
max = numbers[0]
for i in numbers:
    if i > max:
        max = i

print("Maximum Element: ",max)
   
min = numbers[0]
for i in numbers:
    if i < min:
        min = i
print("Minimum Element: ",min)
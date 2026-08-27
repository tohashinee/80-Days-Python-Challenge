#Create a fixed-size array in Java and a list in Python; fill them with random integers and print their values and length.
Numbers = [34,5,100,23,11,67,4,900,89,12]
for i in Numbers:
    print(f"{i} \t", end = "") #Override default ending character with end = "" to print everything on the same line
print()
print(f"Length of list: {len(Numbers)}")
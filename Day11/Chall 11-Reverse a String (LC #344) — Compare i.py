# Reverse a String (LC #344) — Compare in-place string manipulation mechanics across both languages.
s = "stupendous"
reverse = "".join((reversed(s)))
print (reverse)

#Alternative method - using stack
stack = list(s)
rev = ""
while stack: #This takes advantage of Python's built-in "truthiness." In Python, an empty list [] is considered False, while a list with at least one element is considered True.
    rev += stack.pop()

print(rev)
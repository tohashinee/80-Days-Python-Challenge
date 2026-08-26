#Challenge 5 - Write a custom function calculate_bmi(weight, height) that returns a formatted classification string.
def calculate_bmi(weight,height):
    bmi = (weight)/(height*height)
    if bmi < 18.5:
        text = f"Your BMI is {bmi:.2f}. You are underweight"
    elif bmi>= 18.5 and bmi<=24.9:
        text = f"Your BMI is {bmi:.2f}. Your weight is healthy."
    elif bmi > 24.9:
        text = f"Your BMI is {bmi:.2f}. You are overweight."
    return text

w = float(input("Enter Weight: "))
h = float(input("Enter Height: "))
print(calculate_bmi(w,h))




# Challenge 2 - Write a program that converts temperatures between Celsius, Fahrenheit, and Kelvin using typed variables and formatted output.
print("----------------Conversion Menu----------------")
print()
print("1. Celcius to Kelvin")
print("2. Celcius to Farenheit")
print("3. Farenheit to Celcius")
print("4. Farenheit to Kelvin")
print("5. Kelvin to Celcius")
print("6. Kelvin to Farenheit")
print()
choice = int(input("Choose an option: "))
while choice < 1 or choice > 5:
    print("Invalid number")
    choice = int(input("Choose an option: "))

temperature = input("Enter temperature: ")

match choice:
    case 1:
        kelvin = ( float(temperature) + 273.15)
        if kelvin >=0:
            print(f" Temperature: {kelvin:.2f} K")
        else:
            print("Invalid Temperature!1")
    case 2:
        farenheit = (float(temperature)*1.8) + 32
        print(f"Temperature: {farenheit:.2f} F")
    case 3:
        celcius = (float(temperature)-32)*(5/9)
        print(f"Temperature: {celcius:.2f} C")
    case 4:
        kelvin = (float(temperature)-32)*(5/9) + 273.15
        if kelvin >= 0:
            print(f"Temperature: {kelvin:.2f} K")
        else:
            print("Invalid temperature value!")
    case 5:
        celcius = float(temperature) - 273.15
        print(f"Temperature: {celcius:.2f} C")
    case 6:
        farenheit = (float(temperature)-273.15)*(1.8) + 32
        print(f"Temperature: {farenheit:.2f} F")
    
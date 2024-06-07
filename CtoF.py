#!/usr/bin/python3
def convert_temp(temperature, unit):
    if unit.upper() == "C":
        return temperature * 9 / 5 + 32
    elif unit.upper() == "F":
        return (temperature - 32) * 5 / 9
    else:
        return None

while True:
    try:
        temperature = float(input("Enter a temperature: "))
        while True:
            unit = input("Enter the unit 'C' for Celsius or 'F' for Fahrenheit: ").upper()
            converted_temp = convert_temp(temperature, unit)
            if converted_temp is not None:
                break
            else:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        break 
    except ValueError:
        print("Invalid input. Please enter a valid number for temperature.")

if converted_temp is not None:
    print(f"{temperature:.2f} {unit} is equal to {converted_temp:.2f} {'F' if unit == 'C' else 'C'}")

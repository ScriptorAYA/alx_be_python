FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temp_input = input("Enter the temperature to convert: ")

try:
    temperature = float(temp_input)
except:
    raise ValueError("Invalid temperature. Please enter a numeric value.")

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if unit == "C" or unit == "c":
    result = convert_to_fahrenheit(temperature)
    print(str(temperature) + "°C is " + str(result) + "°F")
elif unit == "F" or unit == "f":
    result = convert_to_celsius(temperature)
    print(str(temperature) + "°F is " + str(result) + "°C")
else:
    print("Invalid unit. Please enter C or F.")


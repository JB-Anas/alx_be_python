# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_OFFSET = 32  # The offset used for Fahrenheit to Celsius conversion

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    # Using the global factor FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    # Using the global factor CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET
    return fahrenheit

# User Interaction
def temperature_conversion():
    # Prompt the user to enter temperature
    temperature = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (Celsius/Fahrenheit): ").strip().lower()

    # Check the unit and call the appropriate function
    if unit == "celsius":
        converted_temperature = convert_to_fahrenheit(temperature)
        print(f"{temperature}° Celsius is {converted_temperature}° Fahrenheit")
    elif unit == "fahrenheit":
        converted_temperature = convert_to_celsius(temperature)
        print(f"{temperature}° Fahrenheit is {converted_temperature}° Celsius")
    else:
        print("Invalid unit. Please enter 'Celsius' or 'Fahrenheit'.")

# Call the function to start the conversion process
temperature_conversion()

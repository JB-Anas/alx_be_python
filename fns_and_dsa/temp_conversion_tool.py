# Define Global Conversion Factors (exact format)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_OFFSET = 32  # Offset used in Fahrenheit to Celsius conversion

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR, FAHRENHEIT_OFFSET
    celsius = (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET
    return fahrenheit

# User interaction
def temperature_conversion():
    try:
        # Prompt user for temperature input
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

        # Check the unit and call the appropriate conversion function
        if unit == "c":
            # Convert Celsius to Fahrenheit
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temperature}°F")
        elif unit == "f":
            # Convert Fahrenheit to Celsius
            converted_temperature = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temperature}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        # Handle invalid input for temperature
        print("Invalid temperature. Please enter a numeric value.")

# Start the conversion process
temperature_conversion()

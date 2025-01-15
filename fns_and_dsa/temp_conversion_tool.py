# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Correct global conversion factor
FAHRENHEIT_OFFSET = 32  # The offset used for Fahrenheit to Celsius conversion

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR, FAHRENHEIT_OFFSET
    # Perform the conversion
    celsius = (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    # Perform the conversion
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET
    return fahrenheit

# User Interaction
def temperature_conversion():
    try:
        # Prompt the user to enter temperature
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

        # Check the unit and call the appropriate function
        if unit == "c":
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temperature}°F")
        elif unit == "f":
            converted_temperature = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temperature}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        # Handle invalid temperature input
        print("Invalid temperature. Please enter a numeric value.")

# Call the function to start the conversion process
temperature_conversion()

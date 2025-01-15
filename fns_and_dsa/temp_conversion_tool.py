# Define Global Conversion Factors (exact format)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_OFFSET = 32  # Offset used in Fahrenheit to Celsius conversion

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET
    return fahrenheit

# User interaction
def temperature_conversion():
    # User input
    temperature = input("Enter the temperature to convert: ")
    
    try:
        # Try to convert the input to a float
        temperature = float(temperature)
        
        # Ask for the unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

        # Check if the unit is valid
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
        # If the user enters a non-numeric value for the temperature
        print("Invalid temperature. Please enter a numeric value.")

# Start the conversion process
temperature_conversion()

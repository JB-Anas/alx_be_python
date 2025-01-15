from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)
    return formatted_date

def calculate_future_date():
    try:
        number_of_days = int(input("Enter the number of days to add: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=number_of_days)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print("Future Date:", formatted_future_date)
        return formatted_future_date
    except ValueError:
        print("Please enter a valid integer for the number of days.")

current_date = display_current_datetime()
future_date = calculate_future_date()

print("Formatted Current Date:", current_date)
print("Formatted Future Date:", future_date)

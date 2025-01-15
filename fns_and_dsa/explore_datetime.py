from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    try:
        number_of_days = int(input("Enter the number of days to add: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=number_of_days)
        print("Future Date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Please enter a valid integer for the number of days.")
        
display_current_datetime()
calculate_future_date()

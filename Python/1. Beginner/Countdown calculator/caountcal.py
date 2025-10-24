from datetime import datetime

# Define the date format
date_format = "%Y-%m-%d"

# Get user input for the two dates
start_date_input = input("Enter the start date (YYYY-MM-DD): ")
end_date_input = input("Enter the end date (YYYY-MM-DD): ")

# Convert input strings to datetime objects
start_date = datetime.strptime(start_date_input, date_format)
end_date = datetime.strptime(end_date_input, date_format)

# Calculate the difference between the two dates
difference = end_date - start_date

# Display the result
print(f"The time between {start_date_input} and {end_date_input} is {difference.days} days.")
202
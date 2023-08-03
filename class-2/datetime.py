import datetime

current_datetime = datetime.datetime.now()
print("Current Date and Time:", current_datetime)

# Creating a specific date: year, month, day
specific_date = datetime.datetime(2023, 8, 15)
print("Specific Date:", specific_date)

current_datetime = datetime.datetime.now()

year = current_datetime.year
month = current_datetime.month
day = current_datetime.day
hour = current_datetime.hour
minute = current_datetime.minute
second = current_datetime.second

print("Year:", year)
print("Month:", month)
print("Day:", day)
print("Hour:", hour)
print("Minute:", minute)
print("Second:", second)


current_datetime = datetime.datetime.now()

# Format as a string with custom formatting
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted DateTime:", formatted_datetime)

# Parse a string into a DateTime object
date_string = "2023-08-15 12:30:45"
parsed_datetime = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed DateTime:", parsed_datetime)

current_date = datetime.date.today()

# Add 7 days to the current date
new_date = current_date + datetime.timedelta(days=7)
print("New Date:", new_date)

# Calculate the time difference between two dates
date1 = datetime.datetime(2023, 8, 1)
date2 = datetime.datetime(2023, 8, 15)
time_difference = date2 - date1
print("Time Difference:", time_difference)



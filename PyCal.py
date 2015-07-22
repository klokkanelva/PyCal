import datetime
from termcolor import colored, cprint

week_dict = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

# you have to enter the date in quotes or it'll do division
user_input = input("Enter date for event\n") # right now only works when entering dates in the form of 22/7 or similar
user_input_date = user_input.split("/") # splits user input into a list
user_input_day = int(user_input_date[0])
user_input_month = int(user_input_date[1])
if len(user_input) <= 5:
    user_input_year = 2015           # meaning, if the user doesn't enter a year,
                                        # we assume the event takes place in the current year
else:
    user_input_year = user_input[-4:]   # otherwise, we take the last 4 characters of the entered
                                        # input and assigns it to the year
event = input('Event: ')
day = {user_input_day: {'Weekday': week_dict[datetime.date(user_input_year, user_input_month, user_input_day).weekday()],'Event': event}}
print(day)

# sorry for no comments, just ask questions
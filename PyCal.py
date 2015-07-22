import datetime
from termcolor import colored, cprint

week_dict = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

user_input = input("Enter date for event\n") # right now only works when entering dates in the form of 22/7 or similar
user_input_date = user_input.split("/") # splits user input into a list
user_input_day = user_input[0]
user_input_month = user_input[1]
# user_input_year should be something like:
# if not user_input.endswith("****"):
#   user_input_year = "2015"
# meaning, if the user doesn't enter a year, we assume the event
# takes place in the current year

example_calendar = {"2015":{'Month':'January':{1:{'Day':'monday''Events':None'Etc':None}}}}

# idea for dictionary generation
# {d: {'day': day_dic[datetime.day(year, month, d]}, 'events': ' '} for d in range(1,32)}

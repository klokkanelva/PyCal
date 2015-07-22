import datetime
from termcolor import colored, cprint

week_dict = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

user_input = input("Enter date for event\n") # right now only works when entering dates in the form of 22/7 or similar
user_input_date = user_input.split("/") # splits user input into a list
user_input_day = user_input[0]
user_input_month = user_input[1]
if len(user_input) <= 5:
    user_input_year = "2015"            # meaning, if the user doesn't enter a year,
                                        # we assume the event takes place in the current year
else:
    user_input_year = user_input[-4:]   # otherwise, we take the last 4 characters of the entered
                                        # input and assigns it to the year


example_calendar = {'Year': user_input_year,
                    'month':'January',
                    'day': {
                        1: {
                            'Weekday': 'Monday'
                            'Events': ''
                        }
                        2: {
                            'Weekday': 'Tuesday'
                            'Events': ''
                        }
                    }}
# ^^^ OK so we're getting a syntax error on the above code
# maybe it'd be better to do a list of tuples instead? Example below:
example_calendar = [("Year":user_input_year), ("Month":"user_input_month"), ("Day":user_input_day), ("Events":None), ("Etc":None)]




# idea for dictionary generation
# {d: {'day': day_dic[datetime.day(year, month, d]}, 'events': ' '} for d in range(1,32)}

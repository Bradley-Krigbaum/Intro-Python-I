"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:

 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.

 - If the user specifies one argument, which we will assume they 
   passed in a month, render the calendar for that month of the 
   current year.

 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.

 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime


def displayCalendar(*args):
    date_to_ref = args[0]
    date_to_ref.pop(0)
    # print(date_to_ref)

    if date_to_ref == ['help']:
        print(
            '''
            \n\n\nThis is a calendar program that will give you either the calendar for this month \nor a calender for the given month and year. To use this program please give both \na number for the month and year that you would like to see.
            \nExample: (this program).py [the number of the month] [the number of the year]
            \nYou do NOT have to give a month or a year but doing so will give you this months calendar.\n\n\n
            '''
        )
    elif len(date_to_ref) == 0:
        print(
            "\n\n" +
            "Here is this months calendar:\n\n" +
            calendar.month((datetime.today().year), (datetime.today().month)) +
            "\n"
        )
    elif len(date_to_ref) == 1:
        month_from_ref = date_to_ref[0]

        print(
            "\n\n" +
            "Here is the calendar:\n\n" +
            calendar.month((datetime.today().year), int(month_from_ref)) +
            "\n"
        )
    elif len(date_to_ref) == 2:
        month_from_ref = date_to_ref[0]
        year_from_ref = date_to_ref[1]

        print(
            "\n\n" +
            "Here is the calendar:\n\n" +
            calendar.month(int(year_from_ref), int(month_from_ref)) +
            "\n"
        )
    else:
        print(
            '\n\n\nsomething went wrong!!!\n\n\n' +
            'Please give a number for the month and year you would like to see\n\n\n'
        )


displayCalendar(sys.argv)

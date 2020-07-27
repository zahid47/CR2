import datetime
import openpyxl
from routine_basics import *
from daily_routine import get_daily_routine


# returns csv of the whole routine
def get_full_routine(sheet, semester, section, cs_major=False):
    global day
    start_row_full = 6
    end_row_full = 102

    section = section.upper()
    rows_that_have_sub_names = [2, 5, 8, 11, 14, 17]
    rows_that_have_day_names = [87, 70, 54, 38, 22, 6]  # column is always 1 [6, 22, 38, 54, 70, 87]

    lineTime = ";08:30-10:00;10:00-11:30;11.30-01:00;01:00-2:30;2:30-4:00;4:00-5:30"
    lineSaturday = "Saturday;"
    lineSunday = "Sunday;"
    lineMonday = "Monday;"
    lineTuesday = "Tuesday;"
    lineWednesday = "Wednesday;"
    lineThursday = "Thursday;"
    lineFriday = "Friday;"

    for a_row_that_have_sub_name in rows_that_have_sub_names:  # traversing columns with sub names from left-right

        counter = start_row_full  # setting counter = start_row every time we finish a column & move to next time frame

        while counter < end_row_full:  # scan one time frame to see if there is a class in that time

            sub = sheet.cell(row=counter, column=a_row_that_have_sub_name).value

            row = counter
            while row + 1 not in rows_that_have_day_names:
                if row in rows_that_have_day_names:
                    day = day = sheet.cell(row=row, column=1).value
                    break
                row -= 1

            if sub in get_subjects_with_section(subjects, semester, section):
                if day == "Monday":
                    lineMonday = lineMonday + sub + " "
                elif day == "Tuesday":
                    lineTuesday = lineTuesday + sub + " "
                elif day == "Wednesday":
                    lineWednesday = lineWednesday + sub + " "
                elif day == "Thursday":
                    lineThursday = lineThursday + sub + " "
                elif day == "Friday":
                    lineFriday = lineFriday + sub + " "
                elif day == "Saturday":
                    lineSaturday = lineSaturday + sub + " "
                elif day == "Sunday":
                    lineSunday = lineSunday + sub + " "

            counter += 1

        lineMonday = lineMonday + ";"
        lineTuesday = lineTuesday + ";"
        lineWednesday = lineWednesday + ";"
        lineThursday = lineThursday + ";"
        lineFriday = lineFriday + ";"
        lineSaturday = lineSaturday + ";"
        lineSunday = lineSunday + ";"

    routine = f"""{lineTime}
{lineSaturday}
{lineSunday}
{lineMonday}
{lineTuesday}
{lineWednesday}
{lineThursday}
{lineFriday}"""

    return routine


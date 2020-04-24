import datetime
import openpyxl
from pprint import pprint

# opening an excel file and selecting the first sheet which is named "Sheet1"
workbook = openpyxl.load_workbook("sample_routine.xlsx")
sheet = workbook["Sheet1"]

# dictionary that contains sub codes, key = semester no., value = list of sub codes
subjects = {
    4: ["SE211", "SE212", "SE213", "SE214", "SE215", "CS211"],
    5: ["SE221", "SE223", "SE224", "SE225", "SE226", "SE222"]
}


def get_day(day_number):
    if day_number == 0:
        return "Monday"
    elif day_number == 1:
        return "Tuesday"
    elif day_number == 2:
        return "Wednesday"
    elif day_number == 3:
        return "Thursday"
    elif day_number == 4:
        return "Friday"
    elif day_number == 5:
        return "Saturday"
    elif day_number == 6:
        return "Sunday"


def get_day_number(day):
    if day == "Monday":
        return 0
    elif day == "Tuesday":
        return 1
    elif day == "Wednesday":
        return 2
    elif day == "Thursday":
        return 3
    elif day == "Friday":
        return 4
    elif day == "Saturday":
        return 5
    elif day == "Sunday":
        return 6


def get_subjects_with_section(subjects_list, semester, section):
    section = section.upper()
    subjects_with_section = []
    for subject in subjects_list[semester]:
        subjects_with_section.append(subject + section)
    return subjects_with_section


def get_routine(semester, section, want_tomorrow=False, cs_major=False, day=get_day(datetime.datetime.now().weekday())):

    global start_row, end_row
    section = section.upper()

    routine = {}

    rows_that_have_sub_names = [2, 5, 8, 11, 14, 17]
    # times = ["08:30-10:00", "10:00-11:30", "11.30-01:00", "01:00-2:30", "2:30-4:00", "4:00-5:30"]

    if want_tomorrow:  # == True
        day = get_day(datetime.datetime.now().weekday() + 1)

    day = "Saturday"

    tomorrow = get_day(get_day_number(day) + 1)

    # print(f"Today = {day}")  # debug
    # print(f"Tomorrow = {tomorrow}")  # debug

    row_length = len(sheet["A"])
    # col_length = len(sheet[1])  # // 4

    # print(row_length)  # debug
    # print(col_length)  # debug

    row = 1
    while row != row_length + 1:  # traversing rows from top-down
        if sheet.cell(row=row, column=1).value == day:  # we found the day! also, day name always in first column(col=1)
            start_row = row
        if sheet.cell(row=row, column=1).value == tomorrow:  # we found the next day! This is where we stop
            end_row = row

        row += 1

    # print(start_row)  # debug
    # print(end_row)  # debug

    dict_counter = 1
    for a_row_that_have_sub_name in rows_that_have_sub_names:  # traversing columns that have sub names from left-right

        counter = start_row  # setting counter = start_row every time we finish a column & move to next time frame

        while counter < end_row:  # scan one time frame to see if there is a class in that time

            sub = sheet.cell(row=counter, column=a_row_that_have_sub_name).value

            if sub in get_subjects_with_section(subjects, semester, section):

                routine[dict_counter] = {}

                subject = sub
                time = sheet.cell(row=4, column=a_row_that_have_sub_name - 1).value
                room = sheet.cell(row=counter, column=a_row_that_have_sub_name - 1).value
                teacher = sheet.cell(row=counter, column=a_row_that_have_sub_name + 1).value

                routine[dict_counter]["time"] = time
                routine[dict_counter]["subject"] = subject
                routine[dict_counter]["room"] = room
                routine[dict_counter]["teacher"] = teacher

                dict_counter += 1

            counter += 1

    return routine


result = get_routine(4, "c")
pprint(result)

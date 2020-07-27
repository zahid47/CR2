import datetime
from routine_basics import *


# returns dictionary of today & tomorrows routine
def get_daily_routine(sheet, semester, section, day=get_day(datetime.datetime.now().weekday())):
    try:
        global start_row, end_row
        section = section.upper()
        routine = {}
        rows_with_sub_names = [2, 5, 8, 11, 14, 17]

        # day = "Monday"  # debug

        tomorrow = get_tomorrow(day)  # returns day name

        # print(f"Today = {day}")  # debug
        # print(f"Tomorrow = {tomorrow}")  # debug

        row_length = len(sheet["A"])
        # col_length = len(sheet[1])  # // 4

        # print(row_length)  # debug
        # print(col_length)  # debug

        # finding start and end row of today
        row = 1
        while row != row_length + 1:  # traversing rows from top-down
            if sheet.cell(row=row, column=1).value == day:  # we found the day! day name always in first column(col=1)
                start_row = row
            if sheet.cell(row=row, column=1).value == tomorrow:  # we found the next day! This is where we stop
                end_row = row

            row += 1

        # print(start_row)  # debug
        # print(end_row)  # debug

        dict_counter = 1
        for a_row_with_sub_name in rows_with_sub_names:  # traversing columns with sub names from left-right

            counter = start_row  # setting counter = start_row every time we finish a column & move to next time frame

            while counter < end_row:  # scan one time frame to see if there is a class in that time

                sub = sheet.cell(row=counter, column=a_row_with_sub_name).value

                # if semester == 1 and sub == "AOL101(A,B,D)" and section == "A" or "B" or "C":
                # I forgot what I was doing here rip, but hey! it works...sort of.
                if sub in get_subjects_with_section(subjects, semester, section):
                    routine[dict_counter] = {}

                    subject = sub
                    time = sheet.cell(row=4, column=a_row_with_sub_name - 1).value
                    room = sheet.cell(row=counter, column=a_row_with_sub_name - 1).value
                    teacher = sheet.cell(row=counter, column=a_row_with_sub_name + 1).value

                    routine[dict_counter]["day"] = day
                    routine[dict_counter]["time"] = time
                    routine[dict_counter]["subject"] = subject
                    routine[dict_counter]["room"] = room
                    routine[dict_counter]["teacher"] = teacher

                    dict_counter += 1

                counter += 1

    except:
        routine = {}

    return routine

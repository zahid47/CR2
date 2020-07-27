from routine_basics import *


# returns csv of the whole routine
def get_full_routine(sheet, semester, section):
    day = None
    start_row = 6
    end_row = 102

    section = section.upper()
    rows_with_sub_names = [2, 5, 8, 11, 14, 17]
    rows_with_day_names = [87, 70, 54, 38, 22, 6]  # column is always 1 [6, 22, 38, 54, 70, 87]

    time_row = ";08:30-10:00;10:00-11:30;11.30-01:00;01:00-2:30;2:30-4:00;4:00-5:30"
    saturday_row = "Saturday;"
    sunday_row = "Sunday;"
    monday_row = "Monday;"
    tuesday_row = "Tuesday;"
    wednesday_row = "Wednesday;"
    thursday_row = "Thursday;"
    friday_row = "Friday;"

    for a_row_with_sub_name in rows_with_sub_names:  # traversing columns with sub names from left-right

        counter = start_row  # setting counter = start_row every time we finish a column & move to next time frame

        while counter < end_row:  # scan one time frame to see if there is a class in that time

            sub = sheet.cell(row=counter, column=a_row_with_sub_name).value
            room = sheet.cell(row=counter, column=a_row_with_sub_name - 1).value
            teacher = sheet.cell(row=counter, column=a_row_with_sub_name + 1).value

            result = f"{sub}, {room}, {teacher}"

            row = counter
            while row + 1 not in rows_with_day_names:
                if row in rows_with_day_names:
                    day = sheet.cell(row=row, column=1).value
                    break
                row -= 1

            if sub in get_subjects_with_section(subjects, semester, section):
                if day == "Monday":
                    monday_row = monday_row + result + " "
                elif day == "Tuesday":
                    tuesday_row = tuesday_row + result + " "
                elif day == "Wednesday":
                    wednesday_row = wednesday_row + result + " "
                elif day == "Thursday":
                    thursday_row = thursday_row + result + " "
                elif day == "Friday":
                    friday_row = friday_row + result + " "
                elif day == "Saturday":
                    saturday_row = saturday_row + result + " "
                elif day == "Sunday":
                    sunday_row = sunday_row + result + " "

            counter += 1

        monday_row = monday_row + ";"
        tuesday_row = tuesday_row + ";"
        wednesday_row = wednesday_row + ";"
        thursday_row = thursday_row + ";"
        friday_row = friday_row + ";"
        saturday_row = saturday_row + ";"
        sunday_row = sunday_row + ";"

    routine = f"""
                    {time_row}
                    {saturday_row}
                    {sunday_row}
                    {monday_row}
                    {tuesday_row}
                    {wednesday_row}
                    {thursday_row}
                    {friday_row}
              """

    return routine

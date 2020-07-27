from full_routine import *

# opening an excel file and selecting the first sheet
excel_file_name = "sample_routine.xlsx"
sheet_name = "Sheet1"

workbook = openpyxl.load_workbook(excel_file_name)
# sheet = workbook["Sheet1"]
sheet = workbook[sheet_name]

# getting semester no from user
while True:
    try:
        semester_no = int(input("Enter semester no (1-11): "))
    except ValueError:
        print("Please enter an integer.")
        semester_no = 0
        continue

    if not 0 < semester_no < 12:
        print("Please enter a valid semester number (1-11). Semester 12 isn't supported yet.")
        continue
    if semester_no != 0:
        break

# getting section from user
while True:
    section = input("Enter section: ").lower()
    if section not in ["a", "b", "c", "d"]:
        print("Please enter a valid section (a/ b/ c/ d).")
        continue
    if section in ["a", "b", "c", "d"]:
        break


def main_get_daily_routine():
    result = get_daily_routine(sheet, semester_no, section)
    # pprint(result)
    print(f'You have {len(result)} class(es) today.')
    print("_____________")
    for cls in range(1, len(result) + 1):
        print(f'Time: {result[cls]["time"]}')
        print(f'Subject: {result[cls]["subject"]}')
        print(f'Room: {result[cls]["room"]}')
        print(f'Teacher: {result[cls]["teacher"]}')
        print("_____________")


def main_get_full_routine():
    routine = get_full_routine(sheet, 5, "b")

    with open("routine.csv", "w") as f:
        f.write(routine)


main_get_daily_routine()

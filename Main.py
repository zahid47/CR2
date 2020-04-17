import datetime
import openpyxl
import requests
from pprint import pprint
import discord
from discord.ext import commands

'''
# Discord stuff
TOKEN = ""
client = commands.Bot(command_prefix="cr ")

# send a msg when the bot is ready and set status
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("cr routine"))
    print("Sir, yes sir!")


def day(weekday_in_int):
    if weekday_in_int == 0:
        return "Monday"
    elif weekday_in_int == 1:
        return "Tuesday"
    elif weekday_in_int == 2:
        return "Wednesday"
    elif weekday_in_int == 3:
        return "Thursday"
    elif weekday_in_int == 4:
        return "Friday"
    elif weekday_in_int == 5:
        return "Saturday"
    elif weekday_in_int == 6:
        return "Sunday"


today = day(datetime.datetime.now().weekday())
routine = {
    "Monday": {},

    "Tuesday": {0: {"sub": "Algorithm Design", "start_time": datetime.time(11, 30),
                    "end_time": datetime.time(1, 00), "room": "604 AB", "teacher": "MAH"},

                1: {"sub": "Digital Electronics", "start_time": datetime.time(1, 00),
                    "end_time": datetime.time(2, 30), "room": "601 AB", "teacher": "KS"},

                2: {"sub": "Object Oriented Concepts", "start_time": datetime.time(2, 30),
                    "end_time": datetime.time(4, 00), "room": "404 AB", "teacher": "FAH"}
                },

    "Wednesday": {0: {"sub": "Digital Electronics", "start_time": datetime.time(1, 00),
                      "end_time": datetime.time(2, 30), "room": "601 AB", "teacher": "KS"},

                  1: {"sub": "Algorithm Design", "start_time": datetime.time(2, 30),
                      "end_time": datetime.time(4, 00), "room": "601 AB", "teacher": "MAH"}
                  },

    "Thursday": {},

    "Friday": {},

    "Saturday": {0: {"sub": "Software Requirements", "start_time": datetime.time(11, 00),
                     "end_time": datetime.time(1, 00), "room": "607 AB", "teacher": "MMR"},

                 1: {"sub": "Object Oriented Concepts", "start_time": datetime.time(2, 30),
                     "end_time": datetime.time(4, 00), "room": "404 AB", "teacher": "FAH"}
                 },

    "Sunday": {0: {"sub": "Software Requirements", "start_time": datetime.time(1, 00),
                   "end_time": datetime.time(2, 30), "room": "406 AB", "teacher": "MMR"},

               1: {"sub": "Algorithm Design LAB 1", "start_time": datetime.time(2, 30),
                   "end_time": datetime.time(4, 00), "room": "404 AB", "teacher": "MAH"},

               2: {"sub": "Algorithm Design LAB 2", "start_time": datetime.time(4, 00),
                   "end_time": datetime.time(5, 30), "room": "404 AB", "teacher": "MAH"}
               }
}

no_of_classes = len(routine[today])
subject = []
start_time = []
end_time = []
room = []
teacher = []
for serial in range(no_of_classes):
    subject.append(routine[today][serial]['sub'])
    start_time.append(routine[today][serial]['start_time'])
    end_time.append(routine[today][serial]['end_time'])
    room.append(routine[today][serial]['room'])
    teacher.append(routine[today][serial]['teacher'])

# [MAIN FUNCTIONALITY]
@client.command(aliases=["today"])
async def routine(ctx):
    await ctx.send(f"You have {no_of_classes} class(es) in {today}.")
    for serial in range(no_of_classes):
        await ctx.send(f"`{subject[serial]}`\nFrom {start_time[serial]} to {end_time[serial]} | Room: {room[serial]} | "
                       f"Teacher: {teacher[serial]}")

# TODO add a command "tomorrow routine"

# run the bot
client.run(TOKEN)
'''

# opening an excel file and selecting the first sheet which is named "Sheet1"
workbook = openpyxl.load_workbook("routine_v4.xlsx")
sheet = workbook["Sheet1"]

# dictionary that contains subject codes according to semester number
subjects = {
    4: ["SE211", "SE212", "SE213", "SE214", "SE215"]
}

routine = []  # list for now, will make it a dict later


def get_day_from_day_number(weekday_in_int):
    if weekday_in_int == 0:
        return "Monday"
    elif weekday_in_int == 1:
        return "Tuesday"
    elif weekday_in_int == 2:
        return "Wednesday"
    elif weekday_in_int == 3:
        return "Thursday"
    elif weekday_in_int == 4:
        return "Friday"
    elif weekday_in_int == 5:
        return "Saturday"
    elif weekday_in_int == 6:
        return "Sunday"


def get_subjects_with_section(subjects_list, semester_no, section):
    subjects_with_section = []
    for subject in subjects_list[semester_no]:
        subjects_with_section.append(subject + section)
    return subjects_with_section


def get_routine(semester_no, section, cs_major=False, tomorrow=False,
                day=get_day_from_day_number(datetime.datetime.now().weekday())):

    section = section.upper()

    day = "Sunday"  # temp

    tomorrow = "Monday"  # get_day_from_day_number(datetime.datetime.now().weekday())


    '''
    if tomorrow:  # == True
        day = tomorrow'''

    if day == "Friday":
        return "No classes in Friday!"

    for row_counter in range(1, len(sheet["B"])):
        if sheet.cell(row=row_counter, column=1).value == day:
            while sheet.cell(row=row_counter, column=1).value != tomorrow:
                pprint(sheet.cell(row=row_counter + 1, column=2).value)
                row_counter += 1

    '''for column in range(2, 18, 3):  # TODO need to change this "18" to len(). Find total no. of rows
        for row in range(1, len(sheet["B"])):
            subject = sheet.cell(row=row, column=column).value
            # print(subject)  # debug
            if subject in get_subjects_with_section(subjects, semester_no, section):
                routine.append(subject)
                # routine.append(sheet.cell(row=row, column=column - 1).value) #  room no.
                # routine.append(sheet.cell(row=row, column=column + 1).value) #  teacher name'''
    # return routine


get_routine(4, "c")

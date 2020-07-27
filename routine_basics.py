# dictionary that contains sub codes, key = semester no., value = list of sub codes
subjects = {
    1: ["SE111", "SE112", "SE113", "ENG101", "AOL101"],
    2: ["SE121", "SE122", "SE123", "MAT101", "PHY101"],
    3: ["SE131", "SE132", "SE133", "MAT102", "STA101"],
    4: ["SE211", "SE212", "SE213", "SE214", "SE215", "CS211"],
    5: ["SE 221", "SE 222", "SE 223", "SE 224", "SE 532"],  # "SE 225", "SE 226",
    6: ["SE 231", "SE 232", "SE 233", "SE 234", "SE 235"],
    7: ["SE 225", "SE 226", "SE 311", "SE 312", "SE 313", "CS 312", "GED"],
    8: ["SE 312", "SE 322", "SE 323", "SE 442", "SE 341", "CS 323"],
    9: ["SWE412", "SWE331", "SWE423", "SWE424"],
    10: ["SWE422", "SWE425", "SWE426", "SWE332"],
    11: ["SWE411", "SWE439"],
    12: []
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


def get_tomorrow(day):
    if day == "Sunday":
        return "Monday"
    else:
        return get_day(get_day_number(day) + 1)


def get_subjects_with_section(subjects_list, semester, section):
    section = section.upper()
    subjects_with_section = []
    for subject in subjects_list[semester]:
        if subject == "AOL101":
            if section in ["A", "B", "D"]:
                subjects_with_section.append("AOL101(A,B,D)")
                continue
        subjects_with_section.append(subject + section)
    return subjects_with_section


def get_sub_name(sub_code):
    # TODO: create a function that takes subject code and returns subject name of that code
    pass

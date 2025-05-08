import time

def isblank(var):
    # Function checks if the value passed in var is blank and asks for another input
    while len(var.strip()) == 0:
        print("You can't leave it blank")
        var = input("Enter a value: ")
    return var

def second(f, day, month):
    # Takes object of first() as the parameter and evaluates second value
    id = f + str(day) + str(month)
    return id

def dobvalid_func(year, month, day, cur_year):
    # Checks if the date of birth is valid
    if year <= 0 or month <= 0 or day <= 0:
        return 0
    if cur_year < year:
        return 0
    if month > 12:
        return 0
    if month in (1, 3, 5, 7, 8, 10, 12):
        if day > 31:
            return 0
    elif month in (4, 6, 9, 11):
        if day > 30:
            return 0
    if year % 4 == 0 and month == 2:
        if day > 29:
            return 0
    elif month == 2 and day > 28:
        return 0
    return 1

def age_func(year, month, day, cur_year, cur_month, cur_day):
    # Calculates age based on date of birth
    age = cur_year - year - 1
    if month < cur_month or (month == cur_month and day <= cur_day):
        age += 1
    return str(age)

t = time.localtime(time.time())
# Determines the current time in a list
cur_year = t.tm_year
cur_month = t.tm_mon
cur_day = t.tm_mday

fname = input("Enter your first name: ")
fname = isblank(fname)
# Call isblank function for fname
lname = input("Enter your last name: ")
lname = isblank(lname)
# Call isblank function for lname

while True:
    dob = input("Enter your date of birth, mm-dd-yyyy: ")
    dob = isblank(dob)
    # Call isblank function for dob
    if len(dob) != 10 or dob[2] != '-' or dob[5] != '-':
        print("Enter date in correct format!!")
        continue
    try:
        month = int(dob[:2])
        day = int(dob[3:5])
        year = int(dob[6:10])
    except ValueError:
        print("Enter date in correct format!!")
        continue

    if dobvalid_func(year, month, day, cur_year) == 0:
        print("Invalid date of birth")
        continue
    else:
        break

print('You can choose one of the following login names:')
first = fname + lname[0]
# Evaluates the first value
print("1. ", first)
print("2. ", second(first, day, month))  # Calls second() with first value as the argument
third = lname[0] + fname + str(year)[2:]
print("3. ", third)
# Evaluates the third value
fourth = fname[0] + lname + age_func(year, month, day, cur_year, cur_month, cur_day)
print("4. ", fourth)
# Evaluates the fourth value

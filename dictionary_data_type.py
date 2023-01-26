# This program calculates days to units(minutes)
# How to use try and except for error handling
# Iterating within a list using for...loop
calc_to_hours = 24
calculation_to_minutes = 24 * 60
calc_to_seconds = 24 * 60 * 60


def days_to_units(num_of_days, unit):
    if unit == "hours":
        return f"{num_of_days} days are {num_of_days * calc_to_hours} {unit}"
    elif unit == "minutes":
        return f"{num_of_days} days are {num_of_days * calculation_to_minutes} {unit}"
    elif unit == "seconds":
        return f"{num_of_days} days are {num_of_days * calc_to_seconds} {unit}"
    else:
        print("you have entered unit wrong")


def execute():
    try:
        user_input_no = int(dictionary_conversion["days"])
        if user_input_no >= 1:
            calculated_value = days_to_units(user_input_no, dictionary_conversion["unit"])
            print(calculated_value)
        elif user_input_no == 0:
            print("enter above zero")
        else:
            print("negative numbers not accepted")
    except ValueError:
        print("your input is not valid")


user_input = ""
while user_input != "exit":
    user_input = input("hey user, enter num of days and unit of conversion: ")
    days_and_units = user_input.split(":")
#   print(days_and_units)
    dictionary_conversion = {"days": days_and_units[0], "unit": days_and_units[1]}
    print(dictionary_conversion)
    execute()

print("wow")

# This program calculates days to units(minutes)
# How to use try and except for error handling
# Iterating within a list using for...loop
calculation_to_units = 24 * 60
unit = "minutes"

print(f"40 days are {calculation_to_units} {unit}")


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {unit}"


def execute():
    try:
        user_input_no = int(days)
        if user_input_no >= 1:
            print(days_to_units(user_input_no))
        elif user_input_no == 0:
            print("enter above zero")
        else:
            print("negative numbers not accepted")
    except ValueError:
        print("your input is not valid")


user_input = ""
while user_input != "exit":
    user_input = input("hey user, enter num of days: ")
    for days in user_input.split(","):
        execute()

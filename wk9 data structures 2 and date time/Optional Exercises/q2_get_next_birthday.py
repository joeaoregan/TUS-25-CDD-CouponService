# A00258304

# Write a function get_next_birthday() which
# * takes a single string parameter representing someone’s date of birth in the format dd/mm/YYYY
# * determines their next birthday
# * returns a string representing their next birthday in the format dd/mm/YYYY 

# The function will need to:
# * Convert the date of birth into a date object
# * Get the current year
# * Create a date object for their birthday this year
# * If their birthday this year has passed, then
#   - Create a date object for their birthday next year
# * Return the birthday in the form dd/mm/YYYY 

# For example:

# Test	                                            | Result
# ------------------------------------------------- | -------------------------
# Michael D Higgins, President of Ireland           | Next birthday: 18/04/2023
# birthday_string = get_next_birthday("18/4/1941")  |
# print(f"Next birthday: {birthday_string}")        |
# ------------------------------------------------- | -------------------------
# Mary Robinson, Former President                   | Next birthday: 21/05/2023
# birthday_string = get_next_birthday("21/5/1944")  |
# print(f"Next birthday: {birthday_string}")        |
# ------------------------------------------------- | -------------------------
# Jessie Buckley, Actress and Singer                | Next birthday: 28/12/2022
# birthday_string = get_next_birthday("28/12/1989") |
# print(f"Next birthday: {birthday_string}")        | 
# ------------------------------------------------- | -------------------------
# # Israel Olatunde, Sprinter                       | Next birthday: 29/05/2023
# birthday_string = get_next_birthday("29/5/2002")  |
# print(f"Next birthday: {birthday_string}")        |
# ------------------------------------------------- | -------------------------
# # Rhasidat Adeleke, Sprinter                      | Next birthday: 29/08/2023
# birthday_string = get_next_birthday("29/8/2002")  |
# print(f"Next birthday: {birthday_string}")        |
# ------------------------------------------------- | -------------------------
# # Jasprit Bumrah, Cricketer                       | Next birthday: 06/12/2022
# birthday_string = get_next_birthday("6/12/1993")  |
# print(f"Next birthday: {birthday_string}")        |


import datetime

def get_next_birthday(dob):
    birthday = datetime.datetime.strptime(dob, "%d/%m/%Y").date()
    # print(next_birthday.month) # 4
    # print(type(next_birthday.month)) # int
    # fire_date.replace(month=months_dict.get(month))
    if birthday.month > 8:
        next_birthday = birthday.replace(year=2022)
    else:
        next_birthday = birthday.replace(year=2023)
    return next_birthday.strftime("%d/%m/%Y")

# Michael D Higgins, President of Ireland
birthday_string = get_next_birthday("18/4/1941")
print(f"Next birthday: {birthday_string}")
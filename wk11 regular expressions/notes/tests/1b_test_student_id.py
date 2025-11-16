
import re

def check_student_id(id):
    # compare the regex to the string
    match = re.fullmatch("[A][0-9]{8}", id)

    # check if there's a match
    if match: # match objecgt not None -> the regex and string match
        print("Valid AIT Student ID")
    else:
        print("Not a valid AIT Student ID")

# test cases
# The regular expression is case-sensitive, 
# which means it will match A00123456 but not a00123456.
check_student_id("A00123456")
check_student_id("A123456")
check_student_id("a00123456")
check_student_id("F00123456")
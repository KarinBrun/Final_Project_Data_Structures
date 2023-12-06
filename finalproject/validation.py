# Name: Final Project
# Author: Karin Brun
# Created: 12/03/2023
#
# Course: CIS 152 - Data Structure
# Version: 1.0
# OS: Linux Ubuntu
# IDE: PyCharm EDU
#
# Copyright:  This is my own original work
#             based on specifications issued
#             by our instructor
#
# Description: Validation code for final project
#
# Academic Honesty: I attest that this is my original work.
#                   I have not used unauthorized source code,
#                   either modified or unmodified. I have not
#                   given other fellow student(s) access to my program.

# exception code for invalid character input
class InvalidInputCharacters(Exception):
    pass


# constant variables for validation inputs
VALID_INPUT_CHARACTERS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-")
VALID_PRIORITY_NUMERIC = [1, 2, 3]
VALID_PRIORITY_STRING = ["Mild", "Moderate", "Severe"]


# validation for numeric triage
def validate_numeric_priority(priority):
    if priority not in VALID_PRIORITY_NUMERIC:
        raise InvalidInputCharacters
    return True


# validation for patient name string
def validate_string_input(string):
    if not (VALID_INPUT_CHARACTERS.issuperset(string)):
        raise InvalidInputCharacters
    return True


# validation for string triage
def validate_string_priority(priority):
    if priority not in VALID_PRIORITY_STRING:
        raise InvalidInputCharacters
    return True

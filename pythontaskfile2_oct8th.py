#Title: Create, concatenate, and print a string and access a sub-string from a given string.

FIRST_NAME=input("ENTER FIRST NAME:")
LAST_NAME=input("ENTER LAST NAME:")
NEW_STRING=(FIRST_NAME+" "+LAST_NAME)
print("FULL NAME:",NEW_STRING)
LENGTH=len(FIRST_NAME)
EXTRACTED_FIRSTNAME=(NEW_STRING[0:LENGTH])
print("EXTRACTED FIRST NAME:",EXTRACTED_FIRSTNAME)


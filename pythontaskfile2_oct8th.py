#Title: Create, concatenate, and print a string and access a sub-string from a given string.

FIRST_NAME="RIFAN"
LAST_NAME="MUHAMMED"
NEW_STRING=(FIRST_NAME+" "+LAST_NAME)
print("FULL NAME:",NEW_STRING)
EXTRACTED_FIRSTNAME=(NEW_STRING[0:5])
print("EXTRACTED FIRST NAME:",EXTRACTED_FIRSTNAME)


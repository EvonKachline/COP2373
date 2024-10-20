
import re

#Tge main fuction that holds the results of the other three functions.

def main():
    insert_phone(input("Enter a phone number "))

    insert_ssn(input("Enter a ssn "))

    insert_zipcode(input("Enter a zip code "))


def insert_phone(phone):

#Telling what is the patton of a vaild phone number.

    phone_number = r'\d\d\d[ -]\d\d\d[ -]\d\d\d\d$'

#This will check if your format is correct.
    
    if re.match(phone_number, phone):

        print("This phone number is valid.")

    else:

        print("This phone number is invalid.")


def insert_ssn(ssn):

#Telling what is the patton of a vaild ssn.

    social_security_number = r'\d\d\d[ -]\d\d[ -]\d\d\d\d$'

#This will check if your format is correct.

    if re.match(social_security_number, ssn):

        print("This social security number is valid.")

    else:

        print("This social security number is invalid.")


def insert_zipcode(zipCode):

#Telling what is the patton of a vaild zip code.
    
    zip_code_number = r'\d\d\d\d\d$'

#This will check if your format is correct.
    
    if re.match(zip_code_number, zipCode):

        print("This zip code is valid.")

    else:

        print("This zip code is invalid.")


main()

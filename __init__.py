import random
from datetime import datetime
from random import *
import string
#Generate Security
def generate_security(securtiy_type):
    security = None
    if securtiy_type == "pin":
        pin = randint(111111, 999999)
        security = str(pin)
    elif securtiy_type == "code":
        random_letter_1 = choice(string.ascii_uppercase)
        random_letter_2 = choice(string.ascii_uppercase)
        random_2_digit_1 = randint(11, 99)
        random_2_digit_2 = randint(11, 99)
        security = f"{random_letter_1}{random_2_digit_1}{random_letter_2}{random_2_digit_2}"
    return security

#Special Key Generator
def generate_special_key(list_of_exists):
    datetime_1 = datetime.today().strftime("%y%m%d%H%M%S")
    random_letter_1 = choice(string.ascii_uppercase)
    random_2_digit = randint(11, 99)

    generated_key = f"{datetime_1}{random_letter_1}{random_2_digit}"

    is_key_exists = False
    for n in list_of_exists:
        if n == generated_key:
            is_key_exists = True
            break

    if is_key_exists:
        generate_special_key(list_of_exists=list_of_exists)
    else:
        return generated_key

def generate_special_key_2(list_of_exists):
    random_letter_1 = choice(string.ascii_lowercase)
    random_letter_2 = choice(string.ascii_lowercase)
    random_2_digit_1 = randint(11, 99)
    random_letter_3 = choice(string.ascii_lowercase)
    random_letter_4 = choice(string.ascii_lowercase)
    random_2_digit_2 = randint(11, 99)
    random_letter_5 = choice(string.ascii_lowercase)
    random_letter_6 = choice(string.ascii_lowercase)

    generated_key = f"{random_letter_1}{random_letter_2}{random_2_digit_1}{random_letter_3}{random_letter_4}{random_2_digit_2}{random_letter_5}{random_letter_6}"

    is_key_exists = False
    for n in list_of_exists:
        if n == generated_key:
            is_key_exists = True
            break

    if is_key_exists:
        generate_special_key_2(list_of_exists=list_of_exists)
    else:
        return generated_key

def generate_special_key_3(list_of_exists):
    random_letter_1 = choice(string.ascii_lowercase)
    random_2_digit_1 = randint(11, 99)
    random_letter_2 = choice(string.ascii_lowercase)

    generated_key = f"{random_letter_1}{random_2_digit_1}{random_letter_2}"

    is_key_exists = False
    for n in list_of_exists:
        if n == generated_key:
            is_key_exists = True
            break

    if is_key_exists:
        generate_special_key_3(list_of_exists=list_of_exists)
    else:
        return generated_key


def generate_dev_id(suffix: str, preffix: str, list_of_exists: list, devname: str):

    current_year = datetime.today().strftime("%y")
    name_intial = devname[0]
    random_digit = randint(0, 9)

    generated_id = f"{preffix}{current_year}{name_intial}{random_digit}{suffix}"

    is_id_exists = False
    for n in list_of_exists:
        if n == generated_id:
            is_id_exists = True
            break

    if is_id_exists:
        generate_dev_id(suffix=suffix, preffix=preffix, list_of_exists=list_of_exists, devname=devname)
    else:
        return generated_id

def generate_user_id(suffix: str, list_of_exists: list, username: str, supporter_name: str):
    random_letter_1 = choice(string.ascii_uppercase)
    random_digit = randint(0, 9)
    random_letter_2 = choice(string.ascii_uppercase)
    current_year = datetime.today().strftime("%y")
    name_intial_1 = username[0]
    name_intial_2 = supporter_name[0]

    generated_id = f"{random_letter_1}{random_digit}{random_letter_2}{current_year}{name_intial_1}{name_intial_2}{suffix}"

    is_id_exists = False
    for n in list_of_exists:
        if n == generated_id:
            is_id_exists = True
            break

    if is_id_exists:
        generate_user_id(suffix=suffix, list_of_exists=list_of_exists, username=username, supporter_name=supporter_name)
    else:
        return generated_id

def create_user_password():
    random_letter_1 = choice(string.ascii_uppercase)
    random_2_digit_1 = randint(11, 99)
    random_letter_2 = choice(string.ascii_uppercase)
    random_2_digit_2 = randint(11, 99)
    random_letter_3 = choice(string.ascii_uppercase)
    random_2_digit_3 = randint(0, 9)

    new_user_pass = f"{random_letter_1}{random_2_digit_1}{random_letter_2}{random_2_digit_2}{random_letter_3}{random_2_digit_3}"

    return new_user_pass

def generate_unique_letters_uid(no_of_letters:int, list_of_exists: list):
    generated_id =""
    for n in range(0, no_of_letters):
         generated_id += choice(string.ascii_uppercase)

    is_id_exists = False
    for n in list_of_exists:
        if n == generated_id:
            is_id_exists = True
            break

    if is_id_exists:
        generate_unique_letters_uid(no_of_letters=no_of_letters, list_of_exists=list_of_exists)
    else:
        return generated_id

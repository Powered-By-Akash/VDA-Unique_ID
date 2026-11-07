"""
VDA-Unique_ID (Unique_ID_By_VDA)
================================
Virtual Development Assistant (VDA)
High-Integrity Unique Identifier, Security Token, PIN & Key Generation Engine.
Developed by Powered By Akash (PBA) — Akash Tanna, Gujarat, India.

Functions:
- generate_security: 6-digit numeric PIN or 4-char alphanumeric security code.
- generate_special_key: Timestamp-seeded unique collision-resistant project key.
- generate_special_key_2: 8-character complex alphanumeric composite token.
- generate_special_key_3: 3-character compact composite key.
- generate_dev_id: Structured developer identity key with year stamp and initial.
- generate_user_id: Standardized user identity code with multi-name checksums.
- create_user_password: High-entropy structured alphanumeric password generator.
- generate_unique_letters_uid: N-length uppercase alphabetical UID with collision detection.
"""

from datetime import datetime
import random
import string
from typing import List, Optional


def generate_security(securtiy_type: str = "pin") -> str:
    """
    Generates a security token based on requested type:
    - 'pin': 6-digit integer string (111111 - 999999).
    - 'code': 4-char uppercase alphanumeric string (e.g. 'A45B82').
    """
    s_type = str(securtiy_type).lower()
    if s_type == "pin":
        return str(random.randint(111111, 999999))
    elif s_type == "code":
        letter_1 = random.choice(string.ascii_uppercase)
        letter_2 = random.choice(string.ascii_uppercase)
        digit_1 = random.randint(11, 99)
        digit_2 = random.randint(11, 99)
        return f"{letter_1}{digit_1}{letter_2}{digit_2}"
    else:
        return str(random.randint(100000, 999999))


def generate_special_key(list_of_exists: Optional[List[str]] = None) -> str:
    """
    Generates a timestamp-based unique key: YYMMDDHHMMSS + Random Uppercase + 2 Digits.
    Guarantees uniqueness against `list_of_exists`.
    """
    if list_of_exists is None:
        list_of_exists = []
    
    while True:
        timestamp = datetime.today().strftime("%y%m%d%H%M%S")
        letter = random.choice(string.ascii_uppercase)
        digit = random.randint(11, 99)
        key = f"{timestamp}{letter}{digit}"
        if key not in list_of_exists:
            return key


def generate_special_key_2(list_of_exists: Optional[List[str]] = None) -> str:
    """
    Generates an 8-character lowercase/digit composite key:
    2 letters + 2 digits + 2 letters + 2 digits + 2 letters.
    """
    if list_of_exists is None:
        list_of_exists = []

    while True:
        l1 = random.choice(string.ascii_lowercase)
        l2 = random.choice(string.ascii_lowercase)
        d1 = random.randint(11, 99)
        l3 = random.choice(string.ascii_lowercase)
        l4 = random.choice(string.ascii_lowercase)
        d2 = random.randint(11, 99)
        l5 = random.choice(string.ascii_lowercase)
        l6 = random.choice(string.ascii_lowercase)
        key = f"{l1}{l2}{d1}{l3}{l4}{d2}{l5}{l6}"
        if key not in list_of_exists:
            return key


def generate_special_key_3(list_of_exists: Optional[List[str]] = None) -> str:
    """
    Generates a 3-component compact key: letter + 2 digits + letter.
    """
    if list_of_exists is None:
        list_of_exists = []

    while True:
        l1 = random.choice(string.ascii_lowercase)
        d1 = random.randint(11, 99)
        l2 = random.choice(string.ascii_lowercase)
        key = f"{l1}{d1}{l2}"
        if key not in list_of_exists:
            return key


def generate_dev_id(suffix: str, preffix: str, list_of_exists: Optional[List[str]] = None, devname: str = "Dev") -> str:
    """
    Generates structured developer identity ID: {prefix}{YY}{initial}{digit}{suffix}.
    """
    if list_of_exists is None:
        list_of_exists = []

    current_year = datetime.today().strftime("%y")
    initial = devname[0].upper() if devname else "X"

    while True:
        digit = random.randint(0, 9)
        dev_id = f"{preffix}{current_year}{initial}{digit}{suffix}"
        if dev_id not in list_of_exists:
            return dev_id


def generate_user_id(suffix: str, list_of_exists: Optional[List[str]] = None, username: str = "User", supporter_name: str = "Support") -> str:
    """
    Generates standardized user account identifier.
    Format: {Letter}{Digit}{Letter}{YY}{Initial1}{Initial2}{suffix}.
    """
    if list_of_exists is None:
        list_of_exists = []

    current_year = datetime.today().strftime("%y")
    i1 = username[0].upper() if username else "U"
    i2 = supporter_name[0].upper() if supporter_name else "S"

    while True:
        l1 = random.choice(string.ascii_uppercase)
        d = random.randint(0, 9)
        l2 = random.choice(string.ascii_uppercase)
        uid = f"{l1}{d}{l2}{current_year}{i1}{i2}{suffix}"
        if uid not in list_of_exists:
            return uid


def create_user_password() -> str:
    """
    Generates a secure structured alphanumeric password:
    {UpperLetter}{2Digits}{UpperLetter}{2Digits}{UpperLetter}{1Digit}.
    """
    l1 = random.choice(string.ascii_uppercase)
    d1 = random.randint(11, 99)
    l2 = random.choice(string.ascii_uppercase)
    d2 = random.randint(11, 99)
    l3 = random.choice(string.ascii_uppercase)
    d3 = random.randint(0, 9)
    return f"{l1}{d1}{l2}{d2}{l3}{d3}"


def generate_unique_letters_uid(no_of_letters: int, list_of_exists: Optional[List[str]] = None) -> str:
    """
    Generates an N-length uppercase alphabetical identifier with collision prevention.
    """
    if list_of_exists is None:
        list_of_exists = []

    while True:
        uid = "".join(random.choice(string.ascii_uppercase) for _ in range(no_of_letters))
        if uid not in list_of_exists:
            return uid


__all__ = [
    "generate_security",
    "generate_special_key",
    "generate_special_key_2",
    "generate_special_key_3",
    "generate_dev_id",
    "generate_user_id",
    "create_user_password",
    "generate_unique_letters_uid"
]

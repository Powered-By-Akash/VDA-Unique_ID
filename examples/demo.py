"""
VDA-Unique_ID Showcase Demo
===========================
Demonstrates identifier and security key generation.
Run:
    python examples/demo.py
"""

import sys
import os

# Add parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from vda_unique_id import (
    generate_security,
    generate_special_key,
    generate_special_key_2,
    generate_dev_id,
    generate_user_id,
    create_user_password,
    generate_unique_letters_uid
)


def main():
    print("=== VDA-Unique_ID Generator Suite ===")

    # 1. Security PIN & Code
    pin = generate_security("pin")
    code = generate_security("code")
    print(f"[1] Security 6-Digit PIN:     {pin}")
    print(f"[2] Security Alphanumeric:     {code}")

    # 2. Collision-free Special Keys
    key1 = generate_special_key()
    key2 = generate_special_key_2()
    print(f"[3] Timestamped Special Key:   {key1}")
    print(f"[4] Composite Special Key:     {key2}")

    # 3. Developer & User IDs
    dev_id = generate_dev_id(suffix="-ENG", preffix="PBA-", devname="Akash")
    user_id = generate_user_id(suffix="-PRO", username="Rajesh", supporter_name="Akash")
    print(f"[5] Developer Identifier:      {dev_id}")
    print(f"[6] User Account Identifier:   {user_id}")

    # 4. Password & Letter UID
    pwd = create_user_password()
    uid = generate_unique_letters_uid(8)
    print(f"[7] Generated Secure Password: {pwd}")
    print(f"[8] 8-Letter Unique UID:       {uid}")

    print("\nAll generator engines executed successfully!")


if __name__ == "__main__":
    main()

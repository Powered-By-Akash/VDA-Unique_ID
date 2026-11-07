<div align="center">

# 🔑 VDA-Unique_ID (Unique_ID_By_VDA)
### Virtual Development Assistant (VDA) — High-Integrity Unique Identifier, Security Token & Key Generation Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.7+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Organization](https://img.shields.io/badge/Powered%20By-Akash-00d4ff)](https://github.com/Powered-By-Akash)
[![Founder](https://img.shields.io/badge/Founder-Akash%20Tanna-ff007f)](https://github.com/akashtanna)
[![Security](https://img.shields.io/badge/Security-Collision--Resistant-10b981)](https://github.com/Powered-By-Akash/VDA-Unique_ID)

**The core algorithmic token, credential, and collision-resistant identity generation framework powering Powered By Akash (PBA) software platforms and UDN infrastructure.**

---

</div>

## 📌 Overview

**VDA-Unique_ID** (internally designated `Unique_ID_By_VDA` under the **Virtual Development Assistant** system) provides a suite of deterministic, collision-resistant identifier generators:
- **Zero Third-Party Dependencies**: Pure standard library (`random`, `datetime`, `string`).
- **Collision Immunity**: Built-in verification loop against existing ID collections (`list_of_exists`) ensuring guaranteed uniqueness.
- **Multi-Tier Security Tokens**: Generates 6-digit numeric PINs, alphanumeric OTP challenge codes, and timestamp-based access keys.
- **Enterprise Hierarchy IDs**: Standardized schema for Developer IDs (`{prefix}{YY}{initial}{digit}{suffix}`) and User Accounts (`{letter}{digit}{letter}{YY}{initial1}{initial2}{suffix}`).
- **Drop-in Compatibility**: Full support for both legacy imports (`import Unique_ID_By_VDA`) and modern package workflows (`import vda_unique_id`).

---

## 🧩 Generator Function Reference

| Function | Output Format | Description |
|---|---|---|
| `generate_security(securtiy_type)` | 6-digit integer or 4-char alphanumeric | Creates verification PINs (`111111`-`999999`) or structured security challenge codes (e.g. `A45B82`). |
| `generate_special_key(list_of_exists)` | Timestamped alphanumeric (`YYMMDDHHMMSS` + Letter + 2 Digits) | Collision-free project access key tied to precise moment of creation. |
| `generate_special_key_2(list_of_exists)` | 8-character lowercase/digit composite | Complex composite token (`l1 l2 d1 l3 l4 d2 l5 l6`) for API tokens and session nonces. |
| `generate_special_key_3(list_of_exists)` | 3-component compact key | Short 3-segment key (e.g. `a42b`) for quick index tags and compact references. |
| `generate_dev_id(suffix, preffix, list_of_exists, devname)` | Formatted system identifier | Standardized developer identity tag combining organization prefix, year code, and initials. |
| `generate_user_id(suffix, list_of_exists, username, supporter_name)` | Formatted account ID | Multi-signature user identifier embedding dual entity checksums and timestamp stamps. |
| `create_user_password()` | Structured alphanumeric password | Generates structured high-entropy passwords (e.g. `K45B82M7`). |
| `generate_unique_letters_uid(no_of_letters, list_of_exists)` | Arbitrary-length uppercase UID | Creates collision-checked alphabetical string identifiers of specified length. |

---

## 🚀 Installation

### Option 1: Install via Pip from GitHub
```bash
pip install git+https://github.com/Powered-By-Akash/VDA-Unique_ID.git
```

### Option 2: Clone and Install in Editable Mode
```bash
git clone https://github.com/Powered-By-Akash/VDA-Unique_ID.git
cd VDA-Unique_ID
pip install -e .
```

---

## 💻 Minimal Code Example

```python
from vda_unique_id import (
    generate_security,
    generate_special_key,
    generate_dev_id
)

# 1. Generate 6-digit 2FA verification PIN
pin = generate_security("pin")
print(f"One-Time PIN: {pin}")

# 2. Generate collision-resistant project access key
existing_keys = ["261107120000A11", "261107120000B22"]
project_key = generate_special_key(list_of_exists=existing_keys)
print(f"Project Access Key: {project_key}")

# 3. Create enterprise developer identity tag
dev_id = generate_dev_id(
    suffix="-DEV",
    preffix="PBA-",
    list_of_exists=[],
    devname="Akash"
)
print(f"Developer ID: {dev_id}")
```

---

## 🎮 Running the Verification Demo

```bash
python examples/demo.py
```

---

## 📁 Repository Structure

```
VDA-Unique_ID/
├── __init__.py           # Legacy root entry point for Unique_ID_By_VDA
├── vda_unique_id.py      # Primary module with full generator suite
├── Unique_ID_By_VDA.py   # Backward-compatibility bridge
├── setup.py              # Setuptools distribution config
├── pyproject.toml        # Modern PEP 517/518 build specification
├── LICENSE               # MIT Open Source License
├── .gitignore            # Git exclusions
├── README.md             # Documentation and usage guide
└── examples/
    └── demo.py           # Verification and usage demonstration
```

---

## 🏢 Organization & Founder

- **Organization:** [Powered By Akash (PBA)](https://github.com/Powered-By-Akash)
- **Founder & Lead Architect:** [Akash Tanna](https://github.com/akashtanna)
- **Location:** Gujarat, India
- **Official Website:** [poweredbyakash.in](https://www.poweredbyakash.in/)

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

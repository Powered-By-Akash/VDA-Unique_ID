from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8") if (this_directory / "README.md").exists() else ""

setup(
    name="vda-unique-id",
    version="2025.1.0",
    description="Virtual Development Assistant (VDA) - High-Integrity Unique Identifier, Security Token, PIN & Key Generation Engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Akash Tanna",
    author_email="Poweredbyakash@gmail.com",
    url="https://github.com/Powered-By-Akash/VDA-Unique_ID",
    project_urls={
        "Organization": "https://github.com/Powered-By-Akash",
        "Website": "https://www.poweredbyakash.in/",
        "Source": "https://github.com/Powered-By-Akash/VDA-Unique_ID",
        "Tracker": "https://github.com/Powered-By-Akash/VDA-Unique_ID/issues",
    },
    py_modules=["vda_unique_id", "Unique_ID_By_VDA"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    keywords="unique-id security tokens pin keys vda virtual-development-assistant pba",
    install_requires=[],
)

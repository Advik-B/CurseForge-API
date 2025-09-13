from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

with codecs.open(os.path.join(here, "requirements.txt"), encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

VERSION = '1.6.0'
DESCRIPTION = "A no-compromises wrapper for the CurseForge API"

# Setting up
setup(
    name="curseforge",
    version=VERSION,
    author="Advik",
    author_email="<advik.b@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=requirements,
    keywords=["CMPDL", "Minecraft", "Curseforge", "API", "Wrapper", "Modding", "Mods"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7", 
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Games/Entertainment",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    url="https://github.com/Advik-B/CurseForge-API",
    project_urls={
        "Bug Reports": "https://github.com/Advik-B/CurseForge-API/issues",
        "Source": "https://github.com/Advik-B/CurseForge-API",
        "Documentation": "https://github.com/Advik-B/CurseForge-API#readme",
    },
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "curseforge=curseforge.__main__:main",
        ],
    },
)

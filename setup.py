from setuptools import setup

with open("README.md") as f:
    long_description = f.read()
    
setup(name="grader",
      version="0.1",
      description="tools for grading coding assignments",
      long_description=long_description,
      author="Asher Wasserman",
      author_email="adwasser@ucsc.edu",
      url="https://github.com/adwasser/grader",
      packages=["grader"],
      scripts=["bin/autograde.py"]
)

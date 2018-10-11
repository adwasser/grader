#!/bin/env python3
"""
Automagically run python scripts and diff their outputs.
"""

import sys
import argparse

from grader import check_student
            
parser = argparse.ArgumentParser(description=sys.modules[__name__].__doc__)
parser.add_argument("studentDirectory", type=str,
                    help="directory with student scripts")
parser.add_argument("expectedDirectory", type=str,
                    help="directory with expected outputs")
args = parser.parse_args()
merged_diffs = check_student(args.studentDirectory, args.expectedDirectory)
    

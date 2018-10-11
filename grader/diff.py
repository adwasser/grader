"""
tools for creating diffs of script output and expected output
"""

import sys
import os
import subprocess
import glob

__all__ = ["call_script",
           "check_script",
           "check_student"]


def clean_name(script_name):
    """Catch some common formatting differences"""
    return script_name.replace("-", "_").lower()


def run_cmd(cmd, *args):
    """Run the command in the shell and catch the output"""
    result = subprocess.run([cmd, *args],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    return result.stdout.decode("utf-8")


def call_script(script_name):
    """Run the script and catch the output.

    Parameters
    ----------
    script_name : str
        path to python script

    Returns
    -------
    output : str
        split lines of standard output
    """
    output = run_cmd("python3", script_name)
    with open("{}.out".format(script_name), "w") as f:
        f.write(output)
    return output


def check_script(script_path, expected_path):
    """Run the script diff the output with the expected output.
    
    Parameters
    ----------
    script_path : str
        path to python script
    expected_path : str
        path to expected output

    Returns
    -------
    diff : str
        output of running diff
    """
    script_dir, script_file = os.path.split(script_path)
    output = call_script(script_path)
    output_path = "{}.out".format(script_path)
    expected_dir, expected_file = os.path.split(expected_path)
    expected_root = expected_file.split(".out")[0]
    diff_path = os.path.join(script_dir, expected_root + ".diff")

    diff = run_cmd("diff", "-c", output_path, expected_path)
    with open(diff_path, "w") as f:
        f.write(diff)
        
    return diff


def check_student(student_directory, expected_output_directory):
    """Run all scripts in the student directory and diff with expected outputs.

    Parameters
    ----------
    student_directory : str
         path to directory with student's scripts
    expected_output_directory : str
        path to directory with expected outputs

    Returns
    -------
    merged_diffs : list
        list of diff lines for each script, merged together
    """
    expected_output_files = glob.glob("{}/*.out".format(expected_output_directory))
    merged_diffs = []
    for i, expected_path in enumerate(expected_output_files):
        expected_dir, expected_file = os.path.split(expected_path)
        script_name = expected_file.split(".out")[0]
        merged_diffs.append("#" * 80)
        merged_diffs.append("## {}".format(script_name))
        merged_diffs.append("#" * 80)
        student_files = glob.glob("{}/*.py".format(student_directory))
        for j, raw_path in enumerate(student_files):
            path, raw_name = os.path.split(raw_path)
            cleaned_name = clean_name(raw_name)
            if cleaned_name == script_name:
                diff = check_script(raw_path, expected_path)
                diff = diff.splitlines()
                break
        else:
            diff = ["\n", "!!! missing {} !!!".format(script_name), "\n"]
        merged_diffs.extend(diff)
    with open("{}/summary.diff".format(student_directory), "w") as f:
        f.write("\n".join(merged_diffs))
    return merged_diffs

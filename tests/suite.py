"""
Runs all tests in the tests folder.
"""

import pytest
import sys

if __name__ == '__main__':
    test_path = r"tests"

    pytest_args = ["-v",
                   "--junitxml=./output/junit_xml/junit_xml.log",
                   "--html=./output/html_report/html_report.html",
                   "--self-contained-html",
                   test_path]

    pytest_args.extend(sys.argv)
    pytest.main(pytest_args)

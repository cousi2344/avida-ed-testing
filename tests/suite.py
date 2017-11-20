"""
Runs all basic tests included in the tests folder.

This script creates and runs all tests considered in the "basic" tests groups,
as opposed to "advanced" tests.
"""

import pytest
import sys

if __name__ == '__main__':
    common_path = r"tests/common"
    pop_basic_path = r"tests/population"
    org_basic_path = r"tests/organism"
    analysis_basic_path = r"tests/analysis"

    pytest_args = ["-v",
                   "--junitxml=./output/junit_xml/junit_xml.log",
                   "--html=./output/html_report/html_report.html",
                   "--self-contained-html",
                   common_path,
                   pop_basic_path,
                   org_basic_path,
                   analysis_basic_path]

    pytest_args.extend(sys.argv)
    pytest.main(pytest_args)

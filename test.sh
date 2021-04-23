#!/usr/bin/env bash
#pylint required and unittest required
python3 -m unittest discover -s test | tee report_test
pylint src | tee report_lint
pylint test | tee -a report_lint


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest


def get_all_cases():
    suite = unittest.TestSuite()
    matched_files = unittest.defaultTestLoader.discover(
        os.path.join(os.path.dirname(__file__), '../module'),
        pattern='*__test.py'
    )

    for case in matched_files:
        suite.addTests(case)

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    cases = get_all_cases()

    runner.run(cases)

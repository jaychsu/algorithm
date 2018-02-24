#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest

ROOT_DIR = os.path.join(os.path.dirname(__file__), '../topic')


def get_all_cases():
    suite = unittest.TestSuite()

    for path, _, files in os.walk(ROOT_DIR):
        if ('pycache' in path or
            'python' not in path or
            '__init__.py' not in files):
            continue

        tests = unittest.defaultTestLoader.discover(
            path,
            pattern='*__test.py',
            top_level_dir=ROOT_DIR
        )

        for test in tests:
            suite.addTests(test)

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    cases = get_all_cases()

    runner.run(cases)

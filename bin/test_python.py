#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys
import unittest
import doctest

sys.path.append(os.path.join(
    os.path.dirname(__file__),
    '../topic'
))
from _test.python.test_base import TaskTimer


def get_unittests(dirname):
    ROOT_DIR = os.path.join(
        os.path.dirname(__file__),
        '../{dirname}'.format(dirname=dirname)
    )
    tests = []

    for path, _, files in os.walk(ROOT_DIR):
        if ('pycache' in path or
            'python' not in path or
            '__init__.py' not in files):
            continue

        tests.append(unittest.defaultTestLoader.discover(
            path,
            pattern='*__test.py',
            top_level_dir=ROOT_DIR
        ))

    return tests


def get_doctests(dirname):
    ROOT_DIR = os.path.join(
        os.path.dirname(__file__),
        '../{dirname}'.format(dirname=dirname)
    )
    tests = []
    sys.path.append(ROOT_DIR)

    for path, _, files in os.walk(ROOT_DIR):
        if 'pycache' in path:
            continue

        for file in files:
            if (file.startswith('_') or
                not file.endswith('.py')):
                continue

            timer = TaskTimer()
            tests.append(doctest.DocTestSuite(
                file[:-3],
                setUp=lambda globs: timer.reset_time(),
                tearDown=lambda globs: timer.print_duration()
            ))

    sys.path.pop()
    return tests


if __name__ == '__main__':
    suite = unittest.TestSuite()

    for tests in (
        get_unittests('topic'),
        get_doctests('leetcode'),
        get_doctests('pramp'),
        get_doctests('other'),
    ):
        suite.addTests(tests)

    unittest.TextTestRunner(verbosity=2).run(suite)

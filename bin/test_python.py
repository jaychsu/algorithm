#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import unittest
import doctest


def log(func):
    def wrapper(dirname, *args, **kw):
        print('[{}]: Starting to test...'.format(dirname))
        res = func(dirname, *args, **kw)
        print('[{}]: Finished to test.\n\n'.format(dirname))
        return res
    return wrapper


@log
def run_unittest(dirname):
    ROOT_DIR = os.path.join(
        os.path.dirname(__file__),
        '../{dirname}'.format(dirname=dirname)
    )
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

        suite.addTests(tests)

    unittest.TextTestRunner(verbosity=2).run(suite)


@log
def run_doctest(dirname):
    ROOT_DIR = os.path.join(
        os.path.dirname(__file__),
        '../{dirname}'.format(dirname=dirname)
    )
    suite = unittest.TestSuite()

    sys.path.append(ROOT_DIR)

    for path, _, files in os.walk(ROOT_DIR):
        if 'pycache' in path:
            continue

        for file in files:
            if (file.startswith('_') or
                not file.endswith('.py')):
                continue

            suite.addTest(doctest.DocTestSuite(file[:-3]))

    sys.path.pop()
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    run_unittest('topic')
    run_doctest('leetcode')
    run_doctest('other')

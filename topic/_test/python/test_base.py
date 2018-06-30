import unittest
import datetime


class TaskTimer:
    def __init__(self):
        self.reset_time()

    def reset_time(self):
        self.timestamp = datetime.datetime.now()

    def print_duration(self):
        duration = datetime.datetime.now() - self.timestamp
        print(duration.microseconds, 'us')


class TestBase(unittest.TestCase):
    MSG_TEMPLATE = '{status}: {msg}'

    @classmethod
    def setUpClass(cls):
        print(cls.MSG_TEMPLATE.format(
            status=cls.__name__,
            msg='Starting tests...'
        ))

    @classmethod
    def tearDownClass(cls):
        print(cls.MSG_TEMPLATE.format(
            status=cls.__name__,
            msg='Finished tests.\n'
        ))

    def setUp(self):
        self.task_timer = TaskTimer()

    def tearDown(self):
        self.task_timer.print_duration()

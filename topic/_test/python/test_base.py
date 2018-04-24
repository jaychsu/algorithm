import unittest
import datetime

MSG_TEMPLATE = '{status}: {msg}'


class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(MSG_TEMPLATE.format(
            status=cls.__name__,
            msg='Starting tests...'
        ))

    @classmethod
    def tearDownClass(cls):
        print(MSG_TEMPLATE.format(
            status=cls.__name__,
            msg='Finished tests.\n'
        ))

    def setUp(self):
        self.t0 = datetime.datetime.now()

    def tearDown(self):
        duration = datetime.datetime.now() - self.t0
        print(duration.microseconds, 'us')

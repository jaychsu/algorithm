import unittest

MSG_TEMPLATE = '{status}: {msg}'

class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(MSG_TEMPLATE.format(
            status=cls.__name__,
            msg='starting tests...'
        ))

    @classmethod
    def tearDownClass(cls):
        print(MSG_TEMPLATE.format(
            status=cls.__name__,
            msg='finished tests.\n'
        ))

from _test.python import *
from hash.python import GeoHash


class TestGeoHash(TestBase):
    CASES = (
        ((39.92816697, 116.38954991), 'wx4g0s8q3jf9'),
        ((51.5171437, -0.1337183), 'gcpvhfqth5sk'),
        ((51.5160862, -0.1294528), 'gcpvj41wzw8b'),
        ((37.4846102, -122.1516928), '9q9jhrggemb1'),
        ((37.4219999, -122.0862462), '9q9hvu7wbq2s'),
        ((-90, -180), '000000000000'),
        ((-90, 0), '5bpbpbpbpbpb'),
        ((-90, 180), 'pbpbpbpbpbpb'),
        ((0, -180), '2pbpbpbpbpbp'),
        ((0, 0), '7zzzzzzzzzzz'),
        ((0, 180), 'rzzzzzzzzzzz'),
        ((90, -180), 'bpbpbpbpbpbp'),
        ((90, 0), 'gzzzzzzzzzzz'),
        ((90, 180), 'zzzzzzzzzzzz'),
    )

    def test_encode(self):
        gh = GeoHash()

        for i, o in self.CASES:
            self.assertEqual(gh.encode(*i, len(o)), o)

    def test_decode(self):
        EPS = 1e-6
        gh = GeoHash()

        for (lat1, lng1), i in self.CASES:
            lat2, lng2 = gh.decode(i)
            self.assertTrue(abs(lat1 - lat2) < EPS)
            self.assertTrue(abs(lng1 - lng2) < EPS)

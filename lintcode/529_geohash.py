"""
main concept is in `../module/geohash.py`
"""


class GeoHash:
    base32 = []

    """
    @param: latitude: one of a location coordinate pair
    @param: longitude: one of a location coordinate pair
    @param: precision: an integer between 1 to 12
    @return: a base32 string
    """
    def encode(self, latitude, longitude, precision=5):
        if not self.base32:
            self.base32 = self.get_base32_list()

        times = (precision * 5) // 2 + 1
        lat_codes = self._loc_to_bins( latitude, times,  -90,  90)
        lng_codes = self._loc_to_bins(longitude, times, -180, 180)

        bin_codes = []
        for i in range(times):
            bin_codes.extend((str(lng_codes[i]), str(lat_codes[i])))

        hash_codes = []
        hash_code = ''
        for i in range(0, len(bin_codes), 5):
            hash_code = int(''.join(bin_codes[i : i + 5]), 2)
            hash_codes.append(self.base32[hash_code])

        return ''.join(hash_codes[:precision])

    def _loc_to_bins(self, location, times, left, right):
        mid = 0
        bins = []

        for i in range(times):
            mid = left + (right - left) / 2.0
            if location > mid:
                left = mid
                bins.append(1)
            else:
                right = mid
                bins.append(0)

        return bins

    def get_base32_list(self):
        base32_list = [str(i) for i in range(10)]

        ignored_char = (ord('a'), ord('i'), ord('l'), ord('o'))
        for i in range(ord('a'), ord('z') + 1):
            if i in ignored_char:
                continue
            base32_list.append(chr(i))

        return base32_list

"""
main concept is in `../module/geohash.py`
"""


class GeoHash:
    base32 = []

    """
    @param: geohash: geohash a base32 string
    @return: latitude and longitude a location coordinate pair
    """
    def decode(self, geohash):
        if not geohash:
            return []
        if not self.base32:
            self.base32 = self.get_base32_list()

        bin_codes = []
        for char in geohash:
            if char not in self.base32:
                return []
            bin_codes.extend(self._oct_to_bins(self.base32.index(char)))

        n = len(bin_codes)
        lat_codes = [bin_codes[i] for i in range(1, n, 2)]
        lng_codes = [bin_codes[i] for i in range(0, n, 2)]

        return [
            self._bins_to_loc(lat_codes,  -90,  90),
            self._bins_to_loc(lng_codes, -180, 180)
        ]

    def _bins_to_loc(self, bins, left, right):
        mid = 0

        for code in bins:
            mid = left + (right - left) / 2.0
            if code:
                left = mid
            else:
                right = mid

        return left + (right - left) / 2.0

    def _oct_to_bins(self, val_in_oct):
        bins = []
        for i in range(5):
            if val_in_oct % 2:
                bins.append(1)
            else:
                bins.append(0)
            val_in_oct = val_in_oct >> 1

        return reversed(bins)

    def get_base32_list(self):
        base32_list = [str(i) for i in range(10)]

        ignored_char = (ord('a'), ord('i'), ord('l'), ord('o'))
        for i in range(ord('a'), ord('z') + 1):
            if i in ignored_char:
                continue
            base32_list.append(chr(i))

        return base32_list

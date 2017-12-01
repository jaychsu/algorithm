class GeoHash:
    base32 = []

    def __init__(self):
        self.base32 = self.get_base32()

    """
    @param: geohash: geohash a base32 string
    @return: latitude and longitude a location coordinate pair
    """
    def decode(self, geohash):
        if not geohash:
            return []

        bin_codes = []
        for char in geohash:
            if char not in self.base32:
                return []
            bin_codes.extend(self.oct_to_bin_list(self.base32.index(char)))

        n = len(bin_codes)
        lng_codes = [bin_codes[i] for i in range(0, n, 2)]
        lat_codes = [bin_codes[i] for i in range(1, n, 2)]

        return [
            self.find_area(lat_codes, -90, 90),
            self.find_area(lng_codes, -180, 180)
        ]

    def find_area(self, codes, left, right):
        mid = 0

        for code in codes:
            mid = left + (right - left) / 2.0
            if code:
                left = mid
            else:
                right = mid

        return left + (right - left) / 2.0

    def oct_to_bin_list(self, val_in_oct):
        bin_codes = []

        for i in range(5):
            if val_in_oct % 2:
                bin_codes.append(1)
            else:
                bin_codes.append(0)
            val_in_oct //= 2

        return reversed(bin_codes)

    def get_base32(self):
        result = []

        for i in range(10):
            result.append(str(i))

        ignored_char = (ord('a'), ord('i'), ord('l'), ord('o'))
        for i in range(ord('a'), ord('z') + 1):
            if i in ignored_char:
                continue
            result.append(chr(i))

        return result

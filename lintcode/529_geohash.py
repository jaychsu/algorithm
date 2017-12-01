"""
main concept

1. use binary search to convert `lng` and `lat` to `bin_code`
   `1`: up or right
   `0`: down or left
2. merge `lng_codes` and `lat_codes` alternately into one `bin_codes`
   `lng_codes[0] + lat_codes[0] + lng_codes[1] + ...`
3. pick every 5 digit from `bin_codes` and convert that to `base32`
"""


class GeoHash:
    base32 = []
    searching_times = 0

    def __init__(self):
        self.base32 = self.get_base32()

    """
    @param: latitude: one of a location coordinate pair
    @param: longitude: one of a location coordinate pair
    @param: precision: an integer between 1 to 12
    @return: a base32 string
    """
    def encode(self, latitude, longitude, precision):
        self.searching_times = (precision * 5 // 2) + 1
        lng_codes = self.get_bin(longitude, -180, 180)
        lat_codes = self.get_bin(latitude, -90, 90)

        bin_codes = []
        for i in range(self.searching_times):
            bin_codes.extend((lng_codes[i], lat_codes[i]))

        hash_codes = []
        hash_code = ''
        for i in range(0, len(bin_codes), 5):
            hash_code = int(''.join(bin_codes[i:i + 5]), 2)
            hash_codes.append(self.base32[hash_code])

        return ''.join(hash_codes[:precision])

    def get_bin(self, target, left, right):
        mid = 0
        bin_codes = []

        for i in range(self.searching_times):
            mid = left + (right - left) / 2.0
            if target > mid:
                left = mid
                bin_codes.append('1')
            else:
                right = mid
                bin_codes.append('0')

        return bin_codes

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

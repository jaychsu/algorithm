"""
main concept for encoding

1. use binary search to convert `lng` and `lat` to `bin_code`
   `1`: up or right
   `0`: down or left
2. merge `lng_codes` and `lat_codes` alternately into one `bin_codes`
   `lng_codes[0] + lat_codes[0] + lng_codes[1] + ...`
3. pick every 5 digit from `bin_codes` and convert that to `base32`
"""


class GeoHash:
    base32 = []

    @classmethod
    def encode(cls, latitude, longitude, precision=5):
        if not cls.base32:
            cls.base32 = cls.get_base32_list()

        times = (precision * 5) // 2 + 1
        lat_codes = cls._loc_to_bins( latitude, times,  -90,  90)
        lng_codes = cls._loc_to_bins(longitude, times, -180, 180)

        bin_codes = []
        for i in range(times):
            bin_codes.extend((str(lng_codes[i]), str(lat_codes[i])))

        hash_codes = []
        hash_code = ''
        for i in range(0, len(bin_codes), 5):
            hash_code = int(''.join(bin_codes[i : i + 5]), 2)
            hash_codes.append(cls.base32[hash_code])

        return ''.join(hash_codes[:precision])

    @classmethod
    def decode(cls, geohash):
        if not geohash:
            return []
        if not cls.base32:
            cls.base32 = cls.get_base32_list()

        bin_codes = []
        for char in geohash:
            if char not in cls.base32:
                return []
            bin_codes.extend(cls._oct_to_bins(cls.base32.index(char)))

        n = len(bin_codes)
        lat_codes = [bin_codes[i] for i in range(1, n, 2)]
        lng_codes = [bin_codes[i] for i in range(0, n, 2)]

        return [
            cls._bins_to_loc(lat_codes,  -90,  90),
            cls._bins_to_loc(lng_codes, -180, 180)
        ]

    @classmethod
    def get_base32_list(cls):
        base32_list = [str(i) for i in range(10)]

        ignored_char = (ord('a'), ord('i'), ord('l'), ord('o'))
        for i in range(ord('a'), ord('z') + 1):
            if i in ignored_char:
                continue
            base32_list.append(chr(i))

        return base32_list

    @classmethod
    def _loc_to_bins(cls, location, times, left, right):
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

    @classmethod
    def _bins_to_loc(cls, bins, left, right):
        mid = 0

        for code in bins:
            mid = left + (right - left) / 2.0
            if code:
                left = mid
            else:
                right = mid

        return left + (right - left) / 2.0

    @classmethod
    def _oct_to_bins(cls, val_in_oct):
        bins = []
        for i in range(5):
            if val_in_oct % 2:
                bins.append(1)
            else:
                bins.append(0)
            val_in_oct = val_in_oct >> 1

        return reversed(bins)

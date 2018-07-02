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
    def __init__(self):
        ignored_chars = {ord(i) for i in 'ailo'}
        base32 = [str(i) for i in range(10)]
        base32.extend(
            chr(i)
            for i in range(ord('a'), ord('z') + 1)
            if i not in ignored_chars
        )
        base32i = {base32[i]: i for i in range(len(base32))}

        self.base32 = base32
        self.base32i = base32i

    def encode(self, latitude, longitude, precision=5):
        digits = precision * 5 // 2 + 1
        lngcode = self._pos_to_bin(longitude, digits, -180, 180)
        latcode = self._pos_to_bin( latitude, digits,  -90,  90)

        bincode = []
        for i in range(digits):
            bincode.append(lngcode[i])
            bincode.append(latcode[i])

        geohash = [
            self.base32[int(''.join(bincode[i:i + 5]), 2)]
            for i in range(0, len(bincode), 5)
        ]

        return ''.join(geohash[:precision])

    def decode(self, geohash):
        bincode = []
        for i in geohash:
            if i not in self.base32i:
                return []
            code = bin(self.base32i[i])[2:].rjust(5, '0')
            bincode.extend(list(code))

        n = len(bincode)
        latcode = [bincode[i] for i in range(1, n, 2)]
        lngcode = [bincode[i] for i in range(0, n, 2)]

        return [
            self._bin_to_pos(latcode,  -90,  90),
            self._bin_to_pos(lngcode, -180, 180),
        ]

    def _bin_to_pos(self, bincode, start, end):
        for i in bincode:
            mid = (start + end) / 2.0

            if i == '1':
                start = mid
            else:
                end = mid

        return (start + end) / 2.0

    def _pos_to_bin(self, position, digits, start, end):
        bincode = []

        for _ in range(digits):
            mid = (start + end) / 2.0

            if mid < position:
                bincode.append('1')
                start = mid
            else:
                bincode.append('0')
                end = mid

        return bincode

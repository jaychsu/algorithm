"""
Test Case:

addRestaurant("Lint Cafe", 12.4999999, 11.599999)
addRestaurant("Code Cafe", 10.4999999, 11.512109)
neighbors(10.5, 11.6, 6.7)
removeRestaurant(1)
addRestaurant("Cafe2", 11.4999999, 11.599999)
addRestaurant("Cafe3", 12.4999999, 11.512109)
neighbors(10.5, 13.6, 8896.7)
neighbors(8.5, 11.6, 6996.7)
addRestaurant("Cafe4", 11.4999999, 11.599999)
addRestaurant("Cafe5", 12.4999999, 78.512109)
removeRestaurant(3)
neighbors(8.5, 70.6, 3200.7)
: if `k` > the maximum error, return all hashcodes
"""

"""
Definition of Location:
class Location:
    # @param {double} latitude, longitude
    # @param {Location}
    @classmethod
    def create(cls, latitude, longitude):
        # This will create a new location object

Definition of Restaurant:
class Restaurant:
    # @param {str} name
    # @param {Location} location
    # @return {Restaurant}
    @classmethod
    def create(cls, name, location):
        # This will create a new restaurant object,
        # and auto fill id

Definition of Helper
class Helper:
    # @param {Location} location1, location2
    @classmethod
    def get_distance(cls, location1, location2):
        # return calculate the distance between two location

Definition of GeoHash
class GeoHash:
    # @param {Location} location
    # @return a string
    @classmethom
    def encode(cls, location):
        # return convert location to a geohash string

    # @param {str} hashcode
    # @return {Location}
    @classmethod
    def decode(cls, hashcode):
        # return convert a geohash string to location
"""

"""
range query from list by `bisect`
"""
import bisect
from YelpHelper import Location, Restaurant, GeoHash, Helper


class MiniYelp:
    ERROR_IN_KM = (
        2500, 630, 78,
        20, 2.4, 0.61,
        0.076, 0.01911, 0.00478,
        0.0005971, 0.0001492, 0.0000186
    )

    restaurants = {}
    restr_to_geohash = {}
    geohashs = []

    # @param {str} name
    # @param {Location} location
    # @return {int} restaurant's id
    def add_restaurant(self, name, location):
        restaurant = Restaurant.create(name, location)
        hashcode = self.get_restr_hashcode(restaurant)

        self.restaurants[hashcode] = restaurant
        self.restr_to_geohash[restaurant.id] = hashcode
        bisect.insort(self.geohashs, hashcode)

        return restaurant.id

    # @param {int} restaurant_id
    # @return nothing
    def remove_restaurant(self, restaurant_id):
        hashcode = self.restr_to_geohash[restaurant_id]
        index = bisect.bisect_left(self.geohashs, hashcode)

        self.geohashs.pop(index)
        del self.restaurants[hashcode]
        del self.restr_to_geohash[restaurant_id]

    # @param {Location} location
    # @param {double} k, distance smaller than k miles
    # @return {str[]} a list of restaurant's name and sort by
    # distance from near to far.
    def neighbors(self, location, k):
        length = self.get_length(k)
        prefix = GeoHash.encode(location)[:length]

        # chr(ord('z') + 1) == '{'
        left = bisect.bisect_left(self.geohashs, prefix)
        right = bisect.bisect(self.geohashs, prefix + '{')

        neighbors = []
        hashcode = restaurant = distance = None
        for i in range(left, right):
            hashcode = self.geohashs[i]
            restaurant = self.restaurants[hashcode]
            distance = Helper.get_distance(location, restaurant.location)
            if distance <= k:
                neighbors.append((distance, restaurant))

        neighbors.sort(key=lambda item: item[0])
        return [
            restr.name
            for _, restr in neighbors
        ]

    def get_length(self, k):
        n = len(self.ERROR_IN_KM)

        for i in range(n):
            if k > self.ERROR_IN_KM[i]:
                return i

        return n

    def get_restr_hashcode(self, restaurant):
        return '{0}:{1}'.format(
            GeoHash.encode(restaurant.location),
            restaurant.id
        )


"""
trie
"""
from YelpHelper import Location, Restaurant, GeoHash, Helper


class Trie:
    def __init__(self):
        self.root = self._new_node()

    def __repr__(self):
        return repr(self.root)

    def put(self, key):
        if not key:
            return

        parent = self.root
        parent['keys'].add(key)
        for char in key:
            if char not in parent['children']:
                parent['children'][char] = self._new_node()
            parent['children'][char]['keys'].add(key)
            parent = parent['children'][char]

    def pick(self, key):
        if not key:
            return

        parent = self.root
        parent['keys'].discard(key)
        for char in key:
            if char not in parent['children']:
                return
            parent = parent['children'][char]
            parent['keys'].discard(key)

    def get_keys_by_prefix(self, prefix):
        parent = self.root
        if not prefix:
            return list(parent['keys'])

        for char in prefix:
            if char not in parent['children']:
                return []
            parent = parent['children'][char]

        return list(parent['keys'])

    def _new_node(self):
        return {
            'keys': set(),
            'children': {}
        }


class MiniYelp:
    ERROR_IN_KM = (
        2500, 630, 78,
        20, 2.4, 0.61,
        0.076, 0.01911, 0.00478,
        0.0005971, 0.0001492, 0.0000186
    )

    trie = Trie()
    restaurants = {}
    restr_to_geohash = {}

    # @param {str} name
    # @param {Location} location
    # @return {int} restaurant's id
    def add_restaurant(self, name, location):
        restaurant = Restaurant.create(name, location)
        hashcode = self.get_restr_hashcode(restaurant)

        self.restaurants[hashcode] = restaurant
        self.restr_to_geohash[restaurant.id] = hashcode
        self.trie.put(hashcode)

        return restaurant.id

    # @param {int} restaurant_id
    # @return nothing
    def remove_restaurant(self, restaurant_id):
        hashcode = self.restr_to_geohash[restaurant_id]

        del self.restaurants[hashcode]
        del self.restr_to_geohash[restaurant_id]
        self.trie.pick(hashcode)

    # @param {Location} location
    # @param {double} k, distance smaller than k miles
    # @return {str[]} a list of restaurant's name and sort by
    # distance from near to far.
    def neighbors(self, location, k):
        length = self.get_length(k)
        prefix = GeoHash.encode(location)[:length]
        hashcodes = self.trie.get_keys_by_prefix(prefix)

        neighbors = []
        restaurant = distance = None
        for hashcode in hashcodes:
            restaurant = self.restaurants[hashcode]
            distance = Helper.get_distance(location, restaurant.location)
            if distance <= k:
                neighbors.append((distance, restaurant))

        neighbors.sort(key=lambda item: item[0])
        return [
            restr.name
            for _, restr in neighbors
        ]

    def get_length(self, k):
        n = len(self.ERROR_IN_KM)

        for i in range(n):
            if k > self.ERROR_IN_KM[i]:
                return i

        return n

    def get_restr_hashcode(self, restaurant):
        return '{0}:{1}'.format(
            GeoHash.encode(restaurant.location),
            restaurant.id
        )

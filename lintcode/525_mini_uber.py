"""
Definition of Trip:
class Trip:
    self.id; # trip's id, primary key
    self.driver_id, self.rider_id; # foreign key
    self.lat, self.lng; # pick up location
    def __init__(self, rider_id, lat, lng):

Definition of Helper
class Helper:
    @classmethod
    def get_distance(cls, lat1, lng1, lat2, lng2):
        # return calculate the distance between (lat1, lng1) and (lat2, lng2)
"""
from Trip import Trip, Helper


class MiniUber:
    driver_to_locs = {}
    driver_to_trip = {}
    INFINITY = float('inf')

    # @param {int} driver_id an integer
    # @param {double} lat, lng driver's location
    # return {trip} matched trip information
    #               if there have matched rider or null
    def report(self, driver_id, lat, lng):
        if not driver_id:
            return

        if driver_id in self.driver_to_trip:
            return self.driver_to_trip[driver_id]

        if driver_id in self.driver_to_locs:
            self.driver_to_locs[driver_id]['lat'] = lat
            self.driver_to_locs[driver_id]['lng'] = lng
        else:
            self.driver_to_locs[driver_id] = self._new_location(lat, lng)

    # @param rider_id an integer
    # @param lat, lng rider's location
    # return a trip
    def request(self, rider_id, lat, lng):
        if not rider_id:
            return
        trip = Trip(rider_id, lat, lng)
        _distance = distance = self.INFINITY
        driver_id = -1

        for _driver_id, _loc in self.driver_to_locs.items():
            _distance = Helper.get_distance(_loc['lat'], _loc['lng'], lat, lng)
            if _distance < distance:
                driver_id = _driver_id
                distance = _distance

        if driver_id == -1:
            return trip

        trip.driver_id = driver_id
        self.driver_to_trip[driver_id] = trip
        del self.driver_to_locs[driver_id]

        return trip

    def _new_location(self, lat, lng):
        return {
            'lat': lat,
            'lng': lng
        }

VEHICLE_ID = {
    'MOTOCYCLE': 'MOTOCYCLE',
    'CAR': 'CAR',
    'BUS': 'BUS',
}


class Vehicle:
    def __init__(self):
        self.type = ''
        self.costs = 0
        self.at_level = None
        self.at_spots = None

    def unpark(self):
        if not self.at_level:
            return

        for x, y in self.at_spots:
            self.at_level.spots[x, y] = None

        self.at_level = None
        self.at_spots = None


class Motorcycle(Vehicle):
    def __init__(self):
        self.type = VEHICLE_ID['MOTOCYCLE']
        self.costs = 1


class Car(Vehicle):
    def __init__(self):
        self.type = VEHICLE_ID['CAR']
        self.costs = 1


class Bus(Vehicle):
    def __init__(self):
        self.type = VEHICLE_ID['BUS']
        self.costs = 5


class Level:
    def __init__(self, id, m, n):
        self.id = id
        self.m = m
        self.n = n
        self.spots = {}

    def get_range(self, vehicle_type):
        quarter = self.n // 4

        if vehicle_type == VEHICLE_ID['BUS']:
            return range(quarter * 3, self.n)

        if vehicle_type == VEHICLE_ID['CAR']:
            return range(quarter, self.n)

        return range(self.n)

    def park_vehicle(self, vehicle):
        """
        :type vehicle: Vehicle
        :rtype: bool
        """
        RANGE = self.get_range(vehicle.type)

        for x in range(self.m):
            gotcha = 0

            for y in RANGE:
                if self.spots.get((x, y)):
                    gotcha = 0
                    continue

                gotcha += 1

                if gotcha == vehicle.costs:
                    spots = []

                    for i in range(y, y - gotcha, -1):
                        spots.append((x, i))
                        self.spots[x, i] = vehicle

                    vehicle.at_level = self
                    vehicle.at_spots = spots
                    return True

        return False


class ParkingLot:
    def __init__(self, k, m, n):
        """
        :type k: int, number of levels
        :type m: int, each level has m rows of spots
        :type n: int, each row has n spots
        """
        self.levels = [Level(i, m, n) for i in range(k)]

    def park_vehicle(self, vehicle):
        """
        :type vehicle: Vehicle
        :rtype: bool
        """
        if any(
            level.park_vehicle(vehicle)
            for level in self.levels
        ):
            return True

        return False

    def unpark_vehicle(self, vehicle):
        """
        :type vehicle: Vehicle
        """
        vehicle.unpark()

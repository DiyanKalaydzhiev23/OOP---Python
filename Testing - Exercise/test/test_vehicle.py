from unittest import TestCase, main
from project.vehicle import Vehicle
from sys import maxsize


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(20.5, 175.5)

    def test_initializing(self):
        self.assertEqual(20.5, self.vehicle.fuel)
        self.assertEqual(20.5, self.vehicle.capacity)
        self.assertEqual(175.5, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_default_consumption(self):
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_not_enough_fuel_error(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(maxsize)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_fuel_change_after_driving(self):
        expected = 19.25
        self.vehicle.drive(1)
        self.assertEqual(expected, self.vehicle.fuel)

    def test_over_refueling(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(maxsize)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_fuel_adding_after_refuel(self):
        self.vehicle.drive(1)
        self.vehicle.refuel(1)
        expected = 20.25
        self.assertEqual(expected, self.vehicle.fuel)

    def test_string_representation(self):
        expected = f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"

        self.assertEqual(expected, str(self.vehicle))


if __name__ == '__main__':
    main()
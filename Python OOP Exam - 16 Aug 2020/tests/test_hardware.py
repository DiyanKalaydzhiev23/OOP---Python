from unittest import TestCase, main
from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(TestCase):

    def setUp(self):
        self.h = Hardware("SSD", "Power", 100, 100)

    def test_initializing(self):
        self.assertEqual("SSD", self.h.name)
        self.assertEqual("Power", self.h.type)
        self.assertEqual(100, self.h.capacity)
        self.assertEqual(100, self.h.memory)

    def test_install_error(self):
        software = Software("Linux", "Light", 1000, 1000)
        with self.assertRaises(Exception) as ex:
            self.h.install(software)

        expected = "Software cannot be installed"
        self.assertEqual(expected, str(ex.exception))

    def test_adding_software(self):
        software = Software("Linux", "Light", 10, 10)
        self.h.install(software)
        self.assertIn(software, self.h.software_components)

    def test_uninstalling(self):
        software = Software("Linux", "Light", 10, 10)
        self.h.install(software)
        self.h.uninstall(software)
        self.assertNotIn(software, self.h.software_components)
    


if __name__ == '__main__':
    main()
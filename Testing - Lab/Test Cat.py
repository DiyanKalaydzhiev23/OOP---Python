class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


from unittest import TestCase, main


class CatTests(TestCase):

    def setUp(self):
        self.cat = Cat("Pancho")

    def test_increase_cat_size_after_eating(self):
        expected_size = self.cat.size + 1
        self.cat.eat()
        self.assertEqual(expected_size, self.cat.size)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_cannot_eat_twice(self):
        self.cat.eat()

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    def test_cat_cannot_sleep_if_not_fed(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_not_sleepy_after_sleep(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()

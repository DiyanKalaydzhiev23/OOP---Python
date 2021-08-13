from unittest import TestCase, main
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):

    def setUp(self):
        self.f = PaintFactory("Test", 10)

    def test_initializing(self):
        self.assertEqual("Test", self.f.name)
        self.assertEqual(10, self.f.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.f.valid_ingredients)
        self.assertEqual({}, self.f.ingredients)

    def test_products_property(self):
        self.assertEqual({}, self.f.products)

    def test_non_valid_add_ingredient_error(self):
        with self.assertRaises(TypeError) as te:
            self.f.add_ingredient("not a color", 10)

        expected = f"Ingredient of type not a color not allowed in PaintFactory"
        self.assertEqual(expected, str(te.exception))

    def test_valid_ingredient_no_space_error(self):
        with self.assertRaises(ValueError) as ve:
            self.f.add_ingredient("white", 100)

        expected = "Not enough space in factory"
        self.assertEqual(expected, str(ve.exception))

    def test_adding_new_valid_product_with_valid_quantity(self):
        self.f.add_ingredient("white", 1)
        self.assertEqual({"white": 1}, self.f.ingredients)

    def test_remove_non_existing_ingredient(self):
        with self.assertRaises(KeyError) as ke:
            self.f.remove_ingredient("not existing ingredient", 1)

        expected = "'No such ingredient in the factory'"
        self.assertEqual(expected, str(ke.exception))

    def test_remove_valid_ingredient_non_valid_quantity(self):
        self.f.ingredients = {"white": 1}
        with self.assertRaises(ValueError) as ve:
            self.f.remove_ingredient("white", 10)

        expected = "Ingredients quantity cannot be less than zero"
        self.assertEqual(expected, str(ve.exception))

    def test_remove_valid_ingredient_valid_quantity(self):
        self.f.ingredients = {"white": 1}
        self.f.remove_ingredient("white", 1)
        self.assertEqual({"white": 0}, self.f.ingredients)


if __name__ == '__main__':
    main()

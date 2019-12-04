import unittest
import tests.base

from src.models.design import Design
from src.models.flower import Flower


class TestBouquet(tests.base.TestBase):
    def setUp(self):
        # TODO Replace with lists of different values (preferably random) and connect attributes
        self.design_spec = 'AL10a15b5c3n40'
        self.design_name = 'A'
        self.design_size = 'L'
        self.total_amount = 40
        self.fixed_amount = 33
        self.extra_amount = 7
        self.flowers = [
            {'flower': Flower('aL'), 'amount': 10},
            {'flower': Flower('bL'), 'amount': 15},
            {'flower': Flower('cL'), 'amount': 5},
            {'flower': Flower('nL'), 'amount': 3},
        ]
        self.design = Design(self.design_spec)

    def test_init_correct(self):
        self.assertEqual(self.design.spec, self.design_spec)
        self.assertEqual(self.design.name, self.design_name)
        self.assertEqual(self.design.size, self.design_size)
        self.assertEqual(self.design.total_amount, self.total_amount)
        self.assertListOfDictEqual(self.design.flowers, self.flowers)

    def test_init_incorrect(self):
        with self.assertRaises(Exception) as cm:
            Design('AbRaKaDaBrA')

        self.assertIn('Wrong format of the bouquet design:', cm.exception.message)

    def test_init_invalid(self):
        with self.assertRaises(Exception) as cm:
            Design('AL10a15b5c3n32')

        self.assertIn('Wrong amount of the flowers in the design:', cm.exception.message)

    def test_repr(self):
        self.assertEqual(self.design_spec, repr(self.design))

    def test_parse_flowers_set(self):
        self.assertListOfDictEqual(self.design.parse_flowers_set('10a15b5c3n'), self.flowers)

    def test_get_extra_amount(self):
        self.assertEqual(self.design.get_extra_amount(), self.extra_amount)

    def test_get_fixed_amount(self):
        self.assertEqual(self.design.get_fixed_amount(), self.fixed_amount)

    def test_validate_amount(self):
        self.assertTrue(self.design.validate_amount())


if __name__ == '__main__':
    unittest.main()

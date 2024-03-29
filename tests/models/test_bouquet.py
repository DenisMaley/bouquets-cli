import unittest
import tests.base

from src.models.bouquet import Bouquet
from src.models.flower import Flower


class TestBouquet(tests.base.TestBase):
    def setUp(self):
        # TODO Replace with lists of different values (preferably random) and loop through
        self.bouquet_name = 'B'
        self.bouquet_size = 'L'
        self.bouquet = Bouquet(self.bouquet_name, self.bouquet_size)

    def test_init(self):
        self.assertEqual(self.bouquet.name, self.bouquet_name)
        self.assertEqual(self.bouquet.size, self.bouquet_size)
        # Empty lists/dicts evaluate to False
        self.assertFalse(self.bouquet.flowers)

    def test_add(self):
        self.__add_flowers()
        self.assertDictEqual({'h': 2, 'b': 1, 'a': 3}, self.bouquet.flowers)

    def test_repr(self):
        self.__add_flowers()
        # Flowers should be in alphabetic order
        self.assertEqual('BLa3b1h2', repr(self.bouquet))

    def __add_flowers(self):
        # TODO Replace with lists of different values (preferably random) and loop through
        # TODO Also connect bouquet size, bouquet spec and flowers dict to these values
        # Flowers with wrong size will be ignored
        self.bouquet.add(Flower('hL'))
        self.bouquet.add(Flower('bL'))
        self.bouquet.add(Flower('aL'))
        self.bouquet.add(Flower('aS'))
        self.bouquet.add(Flower('hL'))
        self.bouquet.add(Flower('hS'))
        self.bouquet.add(Flower('aL'))
        self.bouquet.add(Flower('aL'))
        self.bouquet.add(Flower('tS'))
        self.bouquet.add(Flower('qS'))


if __name__ == '__main__':
    unittest.main()

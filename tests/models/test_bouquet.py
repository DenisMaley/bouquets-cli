import unittest

from src.models.bouquet import Bouquet
from src.models.flower import Flower


class TestBouquet(unittest.TestCase):
    def setUp(self):
        self.bouquet_name = 'B'
        self.bouquet_size = 'L'
        self.bouquet = Bouquet(self.bouquet_name, self.bouquet_size)

    def test_init(self):
        self.assertEqual(self.bouquet.name, self.bouquet_name)
        self.assertEqual(self.bouquet.size, self.bouquet_size)
        # Empty lists/dicts evaluate to False
        self.assertFalse(self.bouquet.flowers)

    def test_add(self):
        self.add_flowers()
        self.assertDictEqual({'h': 2, 'b': 1, 'a': 3}, self.bouquet.flowers)

    def test_repr(self):
        self.add_flowers()
        #Flowers should be in alphabetic order
        self.assertEqual('BLa3b1h2', self.bouquet.__repr__())

    def add_flowers(self):
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

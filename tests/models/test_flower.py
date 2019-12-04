import unittest

from src.models.flower import Flower


class TestFlower(unittest.TestCase):
    def setUp(self):
        self.flower_name = 'a'
        self.flower_size = 'S'
        self.flower_spec = '{}{}'.format(self.flower_name, self.flower_size)
        self.flower = Flower(self.flower_spec)

    def test_init_correct(self):
        self.assertEqual(self.flower.spec, self.flower_spec)
        self.assertEqual(self.flower.name, self.flower_name)
        self.assertEqual(self.flower.size, self.flower_size)

    def test_init_incorrect(self):
        with self.assertRaises(Exception) as cm:
            Flower('aM')

        self.assertIn('Wrong format of the flower:', cm.exception.message)

    def test_repr(self):
        self.assertEqual(self.flower_spec, self.flower.__repr__())


if __name__ == '__main__':
    unittest.main()

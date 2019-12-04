import unittest


class TestBase(unittest.TestCase):

    def assertListOfDictEqual(self, l1, l2):
        self.assertEqual(self.__jsonify_list_of_dict(l1), self.__jsonify_list_of_dict(l2))

    @staticmethod
    def __jsonify_list_of_dict(_list):
        for i, _dict in enumerate(_list):
            _list[i] = {k: repr(v) for k, v in _dict.items()}
        return _list

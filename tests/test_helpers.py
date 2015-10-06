import unittest

from collections import OrderedDict

from omnikassa.helpers import (
    data_to_str,
    str_to_data,
)


class HelpersTests(unittest.TestCase):
    def test_data_to_str(self):
        data = OrderedDict([('a', 1), ('b', 2)])
        self.assertEqual('a=1|b=2', data_to_str(data))

    def test_str_to_data(self):
        dct = str_to_data('a=1|b=2')
        self.assertDictEqual(dct, {'a': '1', 'b': '2'})

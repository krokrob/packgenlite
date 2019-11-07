# -*- coding: UTF-8 -*-

# Import from standard library
import os
import wagon_tools
import unittest
import pandas as pd

# Import from our lib
from wagon_tools.lib import get_data, clean_data


class TestUtils(unittest.TestCase):

    def test_get_data(self):
        res = 'tons of data'
        out = get_data()
        self.assertEqual(res, out)

    # @unittest.skip('')
    def test_clean_data(self):
        datapath = os.path.dirname(os.path.abspath(wagon_tools.__file__)) + '/data'
        df = pd.read_csv('{}/data.csv'.format(datapath))
        out = clean_data(df.columns[3])
        self.assertEqual('GAME', out)


if __name__ == '__main__':
    unittest.main()

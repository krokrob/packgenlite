# -*- coding: UTF-8 -*-

# Import from standard library
import os
import proj
import unittest
import pandas as pd

# Import from our lib
from proj.lib import clean_data


class TestUtils(unittest.TestCase):

    # @unittest.skip('')
    def test_clean_data(self):
        datapath = os.path.dirname(os.path.abspath(proj.__file__)) + '/data'
        df = pd.read_csv('{}/data.csv.gz'.format(datapath))
        self.assertListEqual(list(df.columns)[:6],
                             ['id', 'civility', 'birthdate', 'city',
                              'postal_code', 'vote_1'])
        self.assertEqual(df.shape, (999, 142))
        out = clean_data(df)
        self.assertEqual(out.shape, (985, 119))

if __name__ == '__main__':
    unittest.main()

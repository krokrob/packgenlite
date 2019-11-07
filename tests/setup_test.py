# -*- coding: UTF-8 -*-

# Import from standard library
import os
import unittest

# Import from our wagon_tools
import wagon_tools
from wagon_tools.setup import get_git_hash
from wagon_tools.setup import get_dt_version


class TestSetup(unittest.TestCase):

    def test_get_git_hash(self):
        out = get_git_hash()
        self.assertEqual(len('3dd6710'), len(out))

    def test_get_dt_version(self):
        out = get_dt_version()
        self.assertEqual(2, out.count('_'))

if __name__ == '__main__':
    unittest.main()


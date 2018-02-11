#!/usr/bin/env python3

import unittest


class TestPy23(unittest.TestCase):

    def test_nothing(self):
        self.assertEqual('foo', 'foo')


if __name__ == '__main__':
    unittest.main()

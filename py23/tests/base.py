#!/usr/bin/env python3

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import six
import tempfile
import unittest

from os import getpid, unlink
from os.path import exists, join

from ..py23 import (
    binary_file_open,
    iteritems_fun,
    subprocess_echo,
)


class TestPy23(unittest.TestCase):
    '''Test our functions work'''

    important_data = {
        2: 'Python 2',
        3: 'Python 3',
    }

    def setUp(self):
        self.object_type = 'type' if six.PY2 else 'class'
        self.filename = join(tempfile.gettempdir(), 'py23.{}'.format(getpid()))
        self.output_data = 'testing is cool'
        with open(self.filename, 'w') as ff:
            ff.write(self.output_data)

    def tearDown(self):
        if exists(self.filename):
            unlink(self.filename)

    def test_binary_file(self):
        expected_output = "I read in {} as <{} 'str'>".format(
            self.filename, self.object_type)
        actual_output = binary_file_open(self.filename)
        self.assertEqual(
            actual_output, expected_output, 'Did not get file as a str'
        )

    def test_iteritems_fun(self):
        for version in [2, 3]:
            actual_output = iteritems_fun(self.important_data, version)
            self.assertEqual(
                actual_output,
                'I am writing Python {}'.format(version),
                'Output was not Python {}'.format(version)
            )

    def test_subprocess_echo(self):
        actual_output = subprocess_echo()
        expected_output = (
            'echo of Hello World! match as they are both <{} \'str\'>'.format(
                self.object_type
            )
        )
        self.assertEqual(
            actual_output, expected_output, 'Output from echo did not match'
        )


if __name__ == '__main__':
    unittest.main()

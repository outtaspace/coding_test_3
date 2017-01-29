#!/usr/bin/env python

import unittest
from unittest.mock import MagicMock

from city_info.command import Command


class TestCommand(unittest.TestCase):
    def testing_abc(self):
        some_exception = TypeError
        some_regex = 'Can\'t instantiate abstract class Command'
        with self.assertRaisesRegex(some_exception, some_regex):
            Command(reader=MagicMock(), writer=MagicMock())


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python

import unittest
from unittest.mock import Mock

from city_info.command import Command, ICommandIOLayer


class TestICommandIOLayer(unittest.TestCase):
    def testing_abc(self):
        some_exception = TypeError
        some_regex = 'Can\'t instantiate abstract class ICommandIOLayer'
        with self.assertRaisesRegex(some_exception, some_regex):
            ICommandIOLayer()

        self.assertTrue(hasattr(Command, 'reader'))
        self.assertTrue(hasattr(Command, 'writer'))


class TestCommand(unittest.TestCase):
    def testing_abc(self):
        some_exception = TypeError
        some_regex = 'Can\'t instantiate abstract class Command'
        with self.assertRaisesRegex(some_exception, some_regex):
            Command(reader=Mock(), writer=Mock())

        self.assertTrue(issubclass(Command, ICommandIOLayer))

        self.assertTrue(hasattr(Command, 'execute'))


if __name__ == '__main__':
    unittest.main()

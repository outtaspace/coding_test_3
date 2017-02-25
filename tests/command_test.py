#!/usr/bin/env python

import unittest
from unittest.mock import Mock

from city_info.command import Command, ICommandIOLayer
from city_info.command.utils import parse_line


class TestICommandIOLayer(unittest.TestCase):
    def testing_abc(self):
        some_exception = TypeError
        some_regex = 'Can\'t instantiate abstract class ICommandIOLayer'
        with self.assertRaisesRegex(some_exception, some_regex):
            ICommandIOLayer()

        self.assertTrue(hasattr(Command, 'reader'))
        self.assertTrue(hasattr(Command, 'writer'))


class TestCommandUtils(unittest.TestCase):
    def testing_parse_line(self):
        line = ''
        self.assertEqual(parse_line(line), None)

        line = '1. Tokyo, Japan - 32,450,000'
        self.assertEqual(parse_line(line), dict(
            id='1',
            city='Tokyo',
            country='Japan',
            population='32,450,000'
        ))

        line = '6. Jakarta. Indonesia - 18,900,000'
        self.assertEqual(parse_line(line), dict(
            id='6',
            city='Jakarta.',
            country='Indonesia',
            population='18,900,000'
        ))

        line = '7. Sao Paulo; Brazil - 18,850,000'
        self.assertEqual(parse_line(line), dict(
            id='7',
            city='Sao Paulo',
            country='Brazil',
            population='18,850,000'
        ))

        line = '14. Moscow, Russian Fed. - 15,000,000'
        self.assertEqual(parse_line(line), dict(
            id='14',
            city='Moscow',
            country='Russian Fed.',
            population='15,000,000'
        ))


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

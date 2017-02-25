#!/usr/bin/env python

from pprint import pformat
import unittest
from unittest.mock import Mock

from city_info.command import Command
from city_info.command.all import All


class TestCommandAll(unittest.TestCase):
    all_raw_lines = """
ID, City, Country,Population
1. Tokyo, Japan - 32,450,000
6. Jakarta. Indonesia - 18,900,000
7. Sao Paulo; Brazil - 18,850,000
14. Moscow, Russian Fed. - 15,000,000
    """

    descriptions = [
        dict(
            id='1',
            city='Tokyo',
            country='Japan',
            population='32,450,000'
        ),
        dict(
            id='6',
            city='Jakarta.',
            country='Indonesia',
            population='18,900,000'
        ),
        dict(
            id='7',
            city='Sao Paulo',
            country='Brazil',
            population='18,850,000'
        ),
        dict(
            id='14',
            city='Moscow',
            country='Russian Fed.',
            population='15,000,000'
        )
    ]

    def testing_abs(self):
        self.assertTrue(issubclass(All, Command))

        command = All(reader=Mock(), writer=Mock())
        self.assertTrue(isinstance(command, Command))
        self.assertTrue(isinstance(command, All))

    def testing_write_summary(self):
        writer = Mock()
        command = All(reader=Mock(), writer=writer)

        descriptions = [1, 2, 3]
        command._write_summary(descriptions=descriptions)
        writer.write.assert_called_once_with(pformat(descriptions))

    def testing_build_descriptions(self):
        command = All(reader=Mock(), writer=Mock())
        self.assertEqual(
            command._build_descriptions(all_raw_lines=self.all_raw_lines),
            self.descriptions
        )

    def testing_execute(self):
        reader = Mock()
        reader_attrs = {'readlines.return_value': self.all_raw_lines}
        reader.configure_mock(**reader_attrs)

        writer = Mock()

        command = All(reader=reader, writer=writer)
        self.assertEqual(command.execute(), None)

        reader.readlines.assert_called_once_with()

        writer.write.assert_called_once_with(pformat(self.descriptions))


if __name__ == '__main__':
    unittest.main()

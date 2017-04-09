#!/usr/bin/env python

import io
from pprint import pformat
import unittest
from unittest.mock import Mock, patch

from city_info.command import Command
from city_info.command.all import All
import tests.command_data as command_data


class TestCommandAll(unittest.TestCase):
    all_raw_lines = command_data.all_raw_lines
    cities = command_data.cities

    def testing_abc(self):
        self.assertTrue(issubclass(All, Command))

        command = All(reader=Mock(), writer=Mock())
        self.assertTrue(isinstance(command, Command))
        self.assertTrue(isinstance(command, All))

    def testing_write_summary(self):
        writer = Mock()
        command = All(reader=Mock(), writer=writer)

        command._write_summary(cities=self.cities)
        writer.write.assert_called_once_with(pformat(self.cities) + '\n')

    def testing_build_cities(self):
        reader = Mock()
        all_raw_lines = io.StringIO(self.all_raw_lines).readlines()
        reader_attrs = {'readlines.return_value': all_raw_lines}
        reader.configure_mock(**reader_attrs)

        command = All(reader=reader, writer=Mock())
        cities = command._build_cities()
        reader.readlines.assert_called_once_with()
        self.assertEqual(cities, self.cities)

    @patch('city_info.command.all.All._write_summary')
    @patch('city_info.command.all.All._build_cities')
    def testing_execute(self, _build_cities, _write_summary):
        _build_cities.return_value = self.cities

        command = All(reader=Mock(), writer=Mock())
        self.assertEqual(command.execute(), None)
        _build_cities.assert_called_once_with()
        _write_summary.assert_called_once_with(cities=self.cities)


if __name__ == '__main__':
    unittest.main()

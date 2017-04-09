#!/usr/bin/env python

import io
import unittest
from unittest.mock import Mock, patch

from city_info.command import Command
from city_info.command.city import City
import tests.command_data as command_data


class TestCommandAll(unittest.TestCase):
    all_raw_lines = command_data.all_raw_lines
    cities = command_data.cities

    def testing_abc(self):
        self.assertTrue(issubclass(City, Command))

        command = City(reader=Mock(), writer=Mock(), city='city')
        self.assertTrue(isinstance(command, Command))
        self.assertTrue(isinstance(command, City))

    def testing_write_summary(self):
        writer = Mock()
        command = City(reader=Mock(), writer=writer, city=self.cities[0].name)

        command._write_summary(city=self.cities[0])
        writer.write.assert_called_once_with(str(self.cities[0]) + '\n')

    def testing_build_cities(self):
        reader = Mock()
        all_raw_lines = io.StringIO(self.all_raw_lines).readlines()
        reader_attrs = {'readlines.return_value': all_raw_lines}
        reader.configure_mock(**reader_attrs)

        command = City(reader=reader, writer=Mock(), city=self.cities[0].name)
        cities = command._build_cities()
        reader.readlines.assert_called_once_with()
        self.assertEqual(cities, self.cities)

    @patch('city_info.command.city.City._write_summary')
    @patch('city_info.command.city.City._build_cities')
    def testing_execute(self, _build_cities, _write_summary):
        _build_cities.return_value = self.cities

        command = City(reader=Mock(), writer=Mock(), city=self.cities[0].name)
        self.assertEqual(command.execute(), None)
        _build_cities.assert_called_once_with()
        _write_summary.assert_called_once_with(city=self.cities[0])


if __name__ == '__main__':
    unittest.main()

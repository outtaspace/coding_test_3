#!/usr/bin/env python

import io
import unittest
from unittest.mock import Mock

from city_info.command import Command
from city_info.command.city import City
import tests.command_data as command_data


class TestCommandAll(unittest.TestCase):
    all_raw_lines = command_data.all_raw_lines

    descriptions = command_data.descriptions

    def testing_abc(self):
        self.assertTrue(issubclass(City, Command))

        command = City(reader=Mock(), writer=Mock(), city='city')
        self.assertTrue(isinstance(command, Command))
        self.assertTrue(isinstance(command, City))

    def testing_build_summary(self):
        summary = City._build_summary(self.descriptions[0])
        self.assertEqual(summary, (
            'id=1;'
            ' city=Tokyo;'
            ' country=Japan;'
            ' population=32,450,000'
        ))

    def testing_build_description(self):
        lines = io.StringIO(self.all_raw_lines)
        self.assertEqual(
            City._build_description(line=lines.readline()),
            None
        )
        self.assertEqual(
            City._build_description(line=lines.readline()),
            self.descriptions[0]
        )
        self.assertEqual(
            City._build_description(line=lines.readline()),
            self.descriptions[1]
        )

    def testing_write_summary(self):
        writer = Mock()
        command = City(reader=Mock(), writer=writer, city='city')

        description = self.descriptions[0]
        command._write_summary(description=description)

        summary = City._build_summary(description=description)
        writer.write.assert_called_once_with(summary + '\n')

    def testing_execute(self):
        reader = io.StringIO(self.all_raw_lines)
        writer = Mock()

        description = self.descriptions[2]

        command = City(
            reader=reader,
            writer=writer,
            city=description['city']
        )
        self.assertEqual(command.execute(), None)

        summary = City._build_summary(description=description)
        writer.write.assert_called_once_with(summary + '\n')


if __name__ == '__main__':
    unittest.main()

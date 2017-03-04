#!/usr/bin/env python

import io
from pprint import pformat
import unittest
from unittest.mock import Mock

from city_info.command import Command
from city_info.command.all import All
import tests.command_data as command_data


class TestCommandAll(unittest.TestCase):
    all_raw_lines = command_data.all_raw_lines

    descriptions = command_data.descriptions

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
        writer.write.assert_called_once_with(pformat(descriptions) + '\n')

    def testing_build_descriptions(self):
        all_raw_lines = io.StringIO(self.all_raw_lines).readlines()
        descriptions = All._build_descriptions(all_raw_lines=all_raw_lines)
        self.assertEqual(
            descriptions,
            self.descriptions
        )

    def testing_execute(self):
        reader = Mock()
        all_raw_lines = io.StringIO(self.all_raw_lines).readlines()
        reader_attrs = {'readlines.return_value': all_raw_lines}
        reader.configure_mock(**reader_attrs)

        writer = Mock()

        command = All(reader=reader, writer=writer)
        self.assertEqual(command.execute(), None)

        reader.readlines.assert_called_once_with()

        writer.write.assert_called_once_with(pformat(self.descriptions) + '\n')


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python

import unittest
from unittest.mock import MagicMock, patch

from city_info.command_factory import CommandFactory, InvalidMode


class TestCommandFactory(unittest.TestCase):
    def test_resolving_class_name(self):
        self.assertEqual(
            CommandFactory.resolve_class_location(mode='all'),
            'city_info.command.all'
        )
        self.assertEqual(
            CommandFactory.resolve_class_location(mode='city'),
            'city_info.command.city'
        )

    def test_resolving_class_location(self):
        with self.assertRaises(InvalidMode):
            CommandFactory.resolve_class_name(mode='unexpected_mode')
        with self.assertRaises(InvalidMode):
            CommandFactory.resolve_class_name(mode=dict())
        self.assertEqual(
            CommandFactory.resolve_class_name(mode='all'),
            'All'
        )
        self.assertEqual(
            CommandFactory.resolve_class_name(mode='city'),
            'City'
        )

    @patch('city_info.command_factory.importlib.import_module')
    def test_loading_module(self, import_module):
        class_location = 'city_info.command.all'

        return_value = MagicMock()
        import_module.return_value = return_value

        module = CommandFactory.import_module(class_location)
        import_module.assert_called_with(class_location)
        self.assertEqual(module, return_value)

    @patch('city_info.command_factory.CommandFactory.import_module')
    def test_creating_instance(self, import_module):
        class_location = 'city_info.command.all'

        class All:
            def __init__(self, reader: str, writer: str) -> None:
                self.reader = reader
                self.writer = writer

        return_value = MagicMock(All=All)
        import_module.return_value = return_value

        instance = CommandFactory.create(
            mode='all',
            reader='reader',
            writer='writer'
        )
        import_module.assert_called_with(class_location)
        self.assertTrue(isinstance(instance, All))
        self.assertEqual(getattr(instance, 'reader'), 'reader')
        self.assertEqual(getattr(instance, 'writer'), 'writer')


if __name__ == '__main__':
    unittest.main()

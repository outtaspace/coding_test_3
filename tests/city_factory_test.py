#!/usr/bin/env python

import unittest

from cerberus import DocumentError
from city_info.city import City
from city_info.city_factory import CityFactory


class TestCityFactory(unittest.TestCase):
    def testing_create(self):
        description = dict(
            id=1,
            name='Tokyo',
            country='Japan',
            population=32450000
        )
        city = CityFactory.create(description=description)
        self.assertTrue(isinstance(city, City))

    def testing_parse_string(self):
        raw_string = ''
        self.assertEqual(CityFactory._parse_string(raw_string), None)

        raw_string = '1. Tokyo, Japan - 32,450,000'
        self.assertEqual(CityFactory._parse_string(raw_string), dict(
            id='1',
            name='Tokyo',
            country='Japan',
            population='32,450,000'
        ))

        raw_string = '6. Jakarta. Indonesia - 18,900,000'
        self.assertEqual(CityFactory._parse_string(raw_string), dict(
            id='6',
            name='Jakarta.',
            country='Indonesia',
            population='18,900,000'
        ))

        raw_string = '7. Sao Paulo; Brazil - 18,850,000'
        self.assertEqual(CityFactory._parse_string(raw_string), dict(
            id='7',
            name='Sao Paulo',
            country='Brazil',
            population='18,850,000'
        ))

        raw_string = '14. Moscow, Russian Fed. - 15,000,000'
        self.assertEqual(CityFactory._parse_string(raw_string), dict(
            id='14',
            name='Moscow',
            country='Russian Fed.',
            population='15,000,000'
        ))

    def testing_create_from_string(self):
        raw_string = ''
        with self.assertRaises(DocumentError) as cm:
            CityFactory.create_from_string(raw_string=raw_string)
        validation_error = cm.exception
        self.assertEqual(str(validation_error), 'document is missing')

        raw_string = '1. Tokyo, Japan - 32,450,000'
        city = CityFactory.create_from_string(raw_string=raw_string)
        self.assertTrue(isinstance(city, City))
        self.assertEqual(city.id, 1)
        self.assertEqual(city.name, 'Tokyo')
        self.assertEqual(city.country, 'Japan')
        self.assertEqual(city.population, 32450000)

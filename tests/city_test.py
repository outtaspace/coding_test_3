#!/usr/bin/env python

import unittest

from city_info.city import City


class TestCity(unittest.TestCase):
    __id = 1
    __name = 'Tokyo'
    __country = 'Japan'
    __population = 32450000

    def test_creating_city(self):
        city = self.__create_city()
        self.__test_city(city)

    def test_repr(self):
        city = self.__create_city()
        self.__test_city(eval(repr(city)))

    def test_str(self):
        city = self.__create_city()
        self.__test_city(eval(str(city)))

    def test_eq(self):
        city = self.__create_city()
        other = self.__create_city()
        self.assertEqual(city, other)

    def test_ne(self):
        city = self.__create_city()
        other = City(
            id=self.__id,
            name=self.__name + 'something else',
            country=self.__country,
            population=self.__population
        )
        self.assertNotEqual(city, other)

    def __create_city(self):
        return City(
            id=self.__id,
            name=self.__name,
            country=self.__country,
            population=self.__population
        )

    def __test_city(self, city: City):
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'name'))
        self.assertTrue(hasattr(city, 'country'))
        self.assertTrue(hasattr(city, 'population'))

        self.assertEqual(city.id, self.__id)
        self.assertEqual(city.name, self.__name)
        self.assertEqual(city.country, self.__country)
        self.assertEqual(city.population, self.__population)

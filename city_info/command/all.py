from pprint import pformat
from typing import List

from city_info.city import City
from city_info.command import Command


class All(Command):
    def execute(self) -> None:
        cities = self._build_cities()
        self._write_summary(cities=cities)

    def _write_summary(self, cities: List[City]) -> None:
        self.writer.write(pformat(cities) + '\n')

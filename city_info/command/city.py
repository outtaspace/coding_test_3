from city_info.city import City as _City
from city_info.command import Command


class City(Command):
    def __init__(self, reader: object, writer: object, city: str) -> None:
        super().__init__(reader=reader, writer=writer)
        self.__city = city

    @property
    def city(self) -> str:
        return self.__city

    def execute(self) -> None:
        cities = self._build_cities()
        for city in cities:
            if self.city == city.name:
                self._write_summary(city=city)
                break

    def _write_summary(self, city: _City) -> None:
        self.writer.write(str(city) + '\n')

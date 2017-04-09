import abc
from typing import List

from cerberus import DocumentError
from city_info.city import City
from city_info.city_factory import CityFactory


class ICommandIOLayer(abc.ABC):
    @property
    @abc.abstractmethod
    def reader(self) -> object:
        pass

    @property
    @abc.abstractmethod
    def writer(self) -> object:
        pass


class Command(ICommandIOLayer, abc.ABC):
    def __init__(self, reader: object, writer: object) -> None:
        self.__reader = reader
        self.__writer = writer

    @abc.abstractmethod
    def execute(self) -> None:
        pass

    @property
    def reader(self) -> object:
        return self.__reader

    @property
    def writer(self) -> object:
        return self.__writer

    def _build_cities(self) -> List[City]:
        cities = []
        for line in self.reader.readlines():
            try:
                city = CityFactory.create_from_string(raw_string=line)
            except DocumentError:
                pass
            else:
                cities.append(city)
        return cities

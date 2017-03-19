import abc


class ICommandIOLayer(abc.ABC):
    @property
    @abc.abstractmethod
    def reader(self) -> object:
        pass

    @property
    @abc.abstractmethod
    def writer(self):
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
    def writer(self):
        return self.__writer

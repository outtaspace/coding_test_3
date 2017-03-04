import abc


class ICommandIOLayer(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def reader(self) -> object:
        pass

    @reader.setter
    @abc.abstractmethod
    def reader(self, reader):
        pass

    @property
    @abc.abstractmethod
    def writer(self):
        pass

    @writer.setter
    @abc.abstractmethod
    def writer(self, writer):
        pass


class Command(ICommandIOLayer, metaclass=abc.ABCMeta):
    def __init__(self, reader: object, writer: object) -> None:
        self.__reader = reader
        self.__writer = writer

    @abc.abstractmethod
    def execute(self) -> None:
        pass

    @property
    def reader(self) -> object:
        return self.__reader

    @reader.setter
    def reader(self, reader):
        self.__reader = reader

    @property
    def writer(self):
        return self.__writer

    @writer.setter
    def writer(self, writer):
        self.__writer = writer

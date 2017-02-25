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
        self._reader = reader
        self._writer = writer

    @abc.abstractmethod
    def execute(self) -> None:
        pass

    @property
    def reader(self) -> object:
        return self._reader

    @reader.setter
    def reader(self, reader):
        self._reader = reader

    @property
    def writer(self):
        return self._writer

    @writer.setter
    def writer(self, writer):
        self._writer = writer

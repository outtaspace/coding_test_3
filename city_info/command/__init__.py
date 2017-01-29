from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    def __init__(self, reader: object, writer: object) -> None:
        self.reader = reader
        self.writes = writer

    @abstractmethod
    def execute(self) -> None:
        pass

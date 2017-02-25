from city_info.command import Command
from city_info.command.utils import parse_line


class City(Command):
    def __init__(self, reader: object, writer: object, city: str) -> None:
        super().__init__(reader=reader, writer=writer)
        self.__city = city

    @property
    def city(self) -> str:
        return self.__city

    def execute(self) -> None:
        for line in self.reader.readlines():
            description = self._build_description(line=line)
            if description is None:
                continue
            if description['city'] == self.city:
                self._write_summary(description)
                break

    def _write_summary(self, description: dict) -> None:
        summary = self._build_summary(description=description)
        self.writer.write(summary + '\n')

    @staticmethod
    def _build_summary(description: dict) -> str:
        summary_template = (
            'id={id};'
            ' city={city};'
            ' country={country};'
            ' population={population}'
        )
        return summary_template.format(**description)

    @staticmethod
    def _build_description(line: str) -> dict:
        return parse_line(line)

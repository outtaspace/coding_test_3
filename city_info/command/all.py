from pprint import pformat

from city_info.command import Command
from city_info.command.utils import parse_line


class All(Command):
    def execute(self) -> None:
        all_raw_lines = self.reader.readlines()
        descriptions = self._build_descriptions(all_raw_lines=all_raw_lines)
        self._write_summary(descriptions=descriptions)

    def _write_summary(self, descriptions: list) -> None:
        self.writer.write(pformat(descriptions) + '\n')

    @staticmethod
    def _build_descriptions(all_raw_lines: list) -> list:
        descriptions = []
        for raw_line in all_raw_lines:
            description = parse_line(raw_line)
            if description is not None:
                descriptions.append(description)
        return descriptions

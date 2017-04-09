import re

from cerberus import Validator
from city_info.city import City


class CityFactory:
    __validator = Validator(dict(
        id=dict(type='integer', coerce=int),
        name=dict(type='string'),
        country=dict(type='string'),
        population=dict(
            type='integer',
            coerce=lambda p: int(p.replace(',', ''))
        )
    ), allow_unknown=True)

    __regex = re.compile("""
        ^
        (\d+)
        \.
        \s+
        ([^;,]+)[;,.]?
        \s+
        ([^;,]+)[;,.]?
        \s-\s
        (.+)
        $
    """, flags=re.X)

    @classmethod
    def create(cls, description: dict) -> City:
        cls.__validator.validate(description)
        city = cls.__validator.document
        return City(
            id=city['id'],
            name=city['name'],
            country=city['country'],
            population=city['population']
        )

    @classmethod
    def create_from_string(cls, raw_string: str) -> City:
        description = cls._parse_string(raw_string=raw_string)
        return cls.create(description=description)

    @classmethod
    def _parse_string(cls, raw_string: str) -> dict:
        match = cls.__regex.findall(raw_string)
        result = None
        if len(match):
            match = match[0]
            result = dict(
                id=match[0],
                name=match[1],
                country=match[2],
                population=match[3]
            )
        return result

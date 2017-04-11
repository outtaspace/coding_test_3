import re

from cerberus import Validator
from city_info.city import City


class CityFactory:
    __validator = Validator(dict(
        id=dict(required=True, type='integer', coerce=int),
        name=dict(required=True, type='string'),
        country=dict(required=True, type='string'),
        population=dict(required=True, type='integer', coerce=int)
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
    def create(cls, **kwargs) -> City:
        if cls.__validator.validate(kwargs):
            description = cls.__validator.document
            return City(**description)
        else:
            raise ValidationError(cls.__validator.errors)

    @classmethod
    def create_from_string(cls, raw_string: str) -> City:
        description = cls._parse_string(raw_string=raw_string)
        return cls.create(**description)

    @classmethod
    def _parse_string(cls, raw_string: str) -> dict:
        match = cls.__regex.findall(raw_string)
        result = {}
        if len(match):
            match = match[0]
            result['id'] = match[0]
            result['name'] = match[1]
            result['country'] = match[2]
            result['population'] = match[3].replace(',', '')
        return result


class ValidationError(Exception):
    pass

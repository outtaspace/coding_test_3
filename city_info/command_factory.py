import abc
import importlib


class Factory(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def resolve_class_name(mode: str) -> str:
        pass

    @staticmethod
    @abc.abstractmethod
    def resolve_class_location(mode: str) -> str:
        pass

    @staticmethod
    @abc.abstractmethod
    def import_module(class_location: str) -> object:
        pass

    @classmethod
    @abc.abstractmethod
    def create(cls, mode: str, *args: dict, **kwargs: dict) -> object:
        pass


class CommandFactory(Factory):
    @staticmethod
    def resolve_class_name(mode: str) -> str:
        mode_to_class_name = dict(all='All', city='City')
        if isinstance(mode, str) and mode in mode_to_class_name:
            return mode_to_class_name[mode]
        else:
            raise InvalidMode

    @staticmethod
    def resolve_class_location(mode: str) -> str:
        return 'city_info.command.{mode}'.format(mode=mode)

    @staticmethod
    def import_module(class_location: str) -> object:
        return importlib.import_module(class_location)

    @classmethod
    def create(cls, mode: str, *args: dict, **kwargs: dict) -> object:
        class_name = cls.resolve_class_name(mode)
        class_location = cls.resolve_class_location(mode)

        module = cls.import_module(class_location)

        return getattr(module, class_name)(*args, **kwargs)


class InvalidMode(Exception):
    pass

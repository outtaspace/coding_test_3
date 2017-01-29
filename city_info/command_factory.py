import importlib


class CommandFactory:
    @classmethod
    def resolve_class_name(cls, mode: str) -> str:
        mode_to_class_name = dict(all='All', city='City')
        return mode_to_class_name[mode]

    @classmethod
    def resolve_class_location(cls, mode: str) -> str:
        return 'city_info.command.{mode}'.format(mode=mode)

    @classmethod
    def import_module(cls, class_location: str) -> object:
        return importlib.import_module(class_location)

    @classmethod
    def create(cls, mode: str, *args: dict, **kwargs: dict) -> object:
        class_name = cls.resolve_class_name(mode)
        class_location = cls.resolve_class_location(mode)

        module = cls.import_module(class_location)

        return getattr(module, class_name)(*args, **kwargs)

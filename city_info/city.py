class City:
    def __init__(self, id: str, name: str, country: str, population: int) -> None: # noqa
        self.__id = id # noqa
        self.__name = name
        self.__country = country
        self.__population = population

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def country(self):
        return self.__country

    @property
    def population(self):
        return self.__population

    def __str__(self):
        fmt = (
            'City(id={id},'
            ' name="{name}",'
            ' country="{country}",'
            ' population={population}'
            ')'
        )
        return fmt.format(
            id=self.id,
            name=self.name,
            country=self.country,
            population=self.population
        )

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

from abc import ABC , abstractmethod


class AbstractPerson(ABC):

    @abstractmethod
    def get_person_name(self):
        raise NotImplementedError()

    @abstractmethod
    def get_birth_day(self):
        raise NotImplementedError()

    @abstractmethod
    def get_city_name(self):
        raise NotImplementedError()

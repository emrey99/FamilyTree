from members.AbstractPerson import AbstractPerson


class BasePerson(AbstractPerson):

    def __init__(self,name,city_name):
        self.name = name
        self.city_name = city_name

    def get_person_name(self):
        return self._name


    def set_person_name(self, value):
        self._name = value

    def get_city_name(self):
        return self._city_name()


    def set_city_name(self, value):
        self._city_name = value

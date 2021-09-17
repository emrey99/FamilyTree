from members.BasePerson import BasePerson


class Child(BasePerson):
    def __init__(self,  name,city_name):
        super().__init__(name, city_name)

from members.BasePerson import BasePerson


class GrandMother2(BasePerson):
    def __init__(self, name, city_name, person_id):
        super().__init__(name, city_name)
        self.person_id = person_id

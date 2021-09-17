from abc import ABC , abstractmethod
from common.constants.ExceptionMessages import *

class AbstractController:

    @abstractmethod
    def insert_child(self,name,city_name):
        raise NotImplementedError()

    @abstractmethod
    def insert_mother(self,name, city_name,person_id):
        raise NotImplementedError()

    @abstractmethod
    def insert_father(self, name, city_name,person_id):
        raise NotImplementedError()

    @abstractmethod
    def remove_child(self,name):
        raise NotImplementedError()

    @abstractmethod
    def remove_father(self,name):
        raise NotImplementedError()

    @abstractmethod
    def remove_mother(self,name):
        raise NotImplementedError()

    @abstractmethod
    def insert_grand_father1(self,name,city_name,person_id):
        raise NotImplementedError()

    @abstractmethod
    def insert_grand_father2(self, name, city_name, person_id):
        raise NotImplementedError()

    @abstractmethod
    def insert_grand_mother1(self, name, city_name, person_id):
        raise NotImplementedError()

    @abstractmethod
    def insert_grand_mother2(self, name, city_name, person_id):
        raise NotImplementedError()

    @abstractmethod
    def remove_grand_mother1(self, name):
        raise NotImplementedError()

    @abstractmethod
    def remove_grand_father2(self, name):
        raise NotImplementedError()

    @abstractmethod
    def remove_grand_father1(self, name):
        raise NotImplementedError()

    @abstractmethod
    def remove_grand_mother2(self, name):
        raise NotImplementedError()

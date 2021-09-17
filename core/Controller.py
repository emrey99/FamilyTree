import mysql.connector

from members.Family.Child import Child
from members.Family.Father import Father
from members.Family.GrandFather1 import GrandFather1
from members.Family.GrandFather2 import GrandFather2
from members.Family.GrandMother1 import GrandMother1
from members.Family.GrandMother2 import GrandMother2
from members.Family.Mother import Mother

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="emre99",
    database="family_tree"
)

mycursor = mydb.cursor()


from core.Interfaces.AbstractContoller import AbstractController


class Controller(AbstractController):

    def __init__(self):
        pass

    def insert_child(self,name,city_name):

        try:
            child = Child(name,city_name)

            sql = f"INSERT INTO person (name,city_name) VALUES (%s,%s)"

            val = [child.name,child.city_name]

            mycursor.execute(sql,val)

            mydb.commit()

        except:

            mydb.rollback()


    def remove_child(self,name):

        try:

          child = Child(name,None)

          sql = f"DELETE FROM person WHERE name = '{child.name}'"

          mycursor.execute(sql)

          mydb.commit()

          print(mycursor.rowcount, "record(s) deleted")

        except:

            print("There is no such child in the DB")



    def insert_father(self, name, city_name,person_id):

        try:

            father = Father(name , city_name,person_id)

            sql = f"INSERT INTO father (name,city_name,person_id) VALUES {father.name,father.city_name,father.person_id}"

            mycursor.execute(sql)

            mydb.commit()

        except:

            mydb.rollback()

    def remove_father(self,name):

        try:

           father = Father(name,None,None)

           sql = f"DELETE FROM father WHERE name = '{father.name}'"

           mycursor.execute(sql)

           mydb.commit()

           print(mycursor.rowcount, "record(s) deleted")

        except:

            print("There is no such father name in the DB")

    def insert_mother(self, name, city_name,person_id):

        try:

            mother = Mother(name,city_name,person_id)

            sql = f"INSERT INTO mother (name,city_name,person_id) VALUES {mother.name,mother.city_name,mother.person_id}"

            mycursor.execute(sql)

            mydb.commit()

        except:

            mydb.rollback()

    def remove_mother(self,name):

        try:

            mother = Mother(name,None,None)

            sql = f"DELETE FROM mother WHERE name = '{mother.name}'"

            mycursor.execute(sql)

            mydb.commit()

            print(mycursor.rowcount, "record(s) deleted")

        except:

            print("There is no such mother in the DB")

    def insert_grand_father1(self,name,city_name,person_id):

        try:

            grandfather1 = GrandFather1(name,city_name,person_id)

            sql = f"INSERT INTO grandfather1 (name,city_name,person_id) VALUES {grandfather1.name,grandfather1.city_name, grandfather1.person_id}"

            mycursor.execute(sql)

            mydb.commit()

        except:

            mydb.rollback()

    def remove_grand_father2(self,name):

        try:

           grandfather2 = GrandFather2(name,None,None)

           sql = f"DELETE FROM grandfather2 WHERE name = '{grandfather2.name}'"

           mycursor.execute(sql)

           mydb.commit()

           print(mycursor.rowcount, "record(s) deleted")

        except:

            print("There is no such grand father name in the DB")

    def insert_grand_father2(self,name,city_name,person_id):

        try:

            grandfather1 = GrandFather2(name,city_name,person_id)

            sql = f"INSERT INTO grandfather2 (name,city_name,person_id) VALUES {grandfather1.name,grandfather1.city_name, grandfather1.person_id}"

            mycursor.execute(sql)

            mydb.commit()

        except:

            mydb.rollback()

    def remove_grand_father1(self,name):

        try:

           grandfather2 = GrandFather1(name,None,None)

           sql = f"DELETE FROM grandfather1 WHERE name = '{grandfather2.name}'"

           mycursor.execute(sql)

           mydb.commit()

           print(mycursor.rowcount, "record(s) deleted")

        except:

            print("There is no such grand father name in the DB")


    def remove_grand_mother1(self,name):

        try:

           grandmother1 = GrandMother1(name,None,None)

           sql = f"DELETE FROM grandmother1 WHERE name = '{grandmother1.name}'"

           mycursor.execute(sql)

           mydb.commit()

           print(mycursor.rowcount, "record(s) deleted")

        except:

            print("There is no such grand father name in the DB")

    def insert_grand_mother1(self, name, city_name, person_id):

        try:

            grandmother1 = GrandMother1(name, city_name, person_id)

            sql = f"INSERT INTO grandmother1 (name,city_name,person_id) VALUES {grandmother1.name, grandmother1.city_name, grandmother1.person_id}"

            mycursor.execute(sql)

            mydb.commit()

        except:

            mydb.rollback()

    def insert_grand_mother2(self, name, city_name, person_id):

        try:

            grandmother2 = GrandMother2(name, None, None)

            sql = f"INSERT INTO grandmother2 (name,city_name,person_id) VALUES {grandmother2.name}"

            mycursor.execute(sql)

            mydb.commit()

        except:

            mydb.rollback()

    def remove_grand_mother2(self,name):

        try:

           grandmother2 = GrandMother2(name,None,None)

           sql = f"DELETE FROM grandmother2 WHERE name = '{grandmother2.name}'"

           mycursor.execute(sql)

           mydb.commit()

           print(mycursor.rowcount, "record(s) deleted")

        except:

            print("There is no such grand father name in the DB")

class AgAg:
    def human(self):
        print("Aung Aung is a Human")

class MgMg:
    def human(self):
        print("Maung Maung is a Human")

class KoKo:
    def human(self):
        print("Ko Ko is a human")
class People:
    def get_func(self,obj):
        obj.human()

agag = AgAg()

mgmg = MgMg()

koko = KoKo()
people = People()

people.get_func(agag)

list = [agag,mgmg,koko]
for obj in list:
    people.get_func(obj)
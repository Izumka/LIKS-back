from Parser import Data


class Seach:
    def __init__(self):
        self.medicatoin = Data().Medication

    def search_by_name(self, string):
        result = [drug for drug in self.medicatoin if string in drug.med_name.split(',')[0].lower()]
        return result

    def search_by_component(self, string):
        result = [drug for drug in self.data if string in drug.med_composition]
        return result

    def search_for_user(self,where, string):
        for i in where:
            if string in i.name:
                return i

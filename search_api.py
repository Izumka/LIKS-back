from Parser import Data


class Seach:
    def __init__(self):
        self.medicatoin = Data().Medication

    def search_by_name(self, string):
        # print(self.medicatoin)
        result = [drug for drug in self.medicatoin if string in drug.med_name.split(',')[0].lower()]
        return result

    def search_by_component(self, string):
        # print(self.medicatoin)
        result = [drug for drug in self.medicatoin if string in drug.med_composition.lower()]
        # print(result)
        return result

    def search_for_user(self,where, string):
        for i in where:
            if string in i.name:
                return i

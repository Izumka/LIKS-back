from Tables.liks_db import Doctors, Medication, PrescriptionMed, Prescriptions


class Data:
    def __init__(self):
        # self.drugs = []
        self.Doctors = []
        self.Prescriptions = []
        self.PrescriptionsMed = []
        self.Medication = []


        self.parse()

    def parse(self):
        for i in Doctors.query.all():
            self.Doctors.append(i)

        for i in Medication.query.all():
            self.Medication.append(i)

        for i in PrescriptionMed.query.all():
            self.PrescriptionsMed.append(i)

        for i in Prescriptions.query.all():
            self.Prescriptions.append(i)
    @staticmethod
    def toJSon(data):
        JSon = dict()

        list_data = data.__str__().split("|")
        print(list_data)
        for part in list_data:
            el = part.split("~")
            print(el)
            JSon[el[0]] = el[1]

        return  JSon
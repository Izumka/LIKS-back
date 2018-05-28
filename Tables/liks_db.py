from flask_sqlalchemy import SQLAlchemy
from APP import APP


class DB:
    def __init__(self, app):
        self.db = SQLAlchemy(app)


idb = DB(APP().app)


class Doctors(idb.db.Model):
    __tablename__ = 'doctors'
    iddoctors = idb.db.Column(idb.db.INTEGER, autoincrement=True, primary_key=True)
    email = idb.db.Column(idb.db.String, unique=True)
    name = idb.db.Column(idb.db.String)
    surname = idb.db.Column(idb.db.String)
    position = idb.db.Column(idb.db.String)

    def __init__(self, email, name, surname, position, ):
        self.email = email
        self.name = name
        self.surname = surname
        self.position = position

    def __repr__(self):
        return 'iddoctors:{}|email:{}|name:{}|surname:{}|position:{}'.format(
            self.iddoctors,
            self.email,
            self.name,
            self.surname,
            self.position)

    def __str__(self):
        return 'iddoctors~{}|email~{}|name~{}|surname~{}|position~{}'.format(
            self.iddoctors,
            self.email,
            self.name,
            self.surname,
            self.position)

class Prescriptions(idb.db.Model):
    __tablename__ = 'prescriptions'
    prescription_id = idb.db.Column(idb.db.INTEGER, autoincrement=True, primary_key=True)
    prescription_date = idb.db.Column(idb.db.TIMESTAMP)  # default=idb.db.TIMESTAMP
    prescription_signa = idb.db.Column(idb.db.String)
    doctors_iddoctors = idb.db.Column(idb.db.INTEGER, primary_key=True)

    def __init__(self, prescription_signa, doctors_iddoctors):
        self.prescription_signa = prescription_signa
        self.doctors_iddoctors = doctors_iddoctors

    def __repr__(self):
        return 'prescription_id:{}|prescription_date:{}|prescription_signa:{}|doctors_iddoctors:{}'.format(
            self.prescription_id,
            self.prescription_date,
            self.prescription_signa,
            self.doctors_iddoctors)

    def __str__(self):
        return 'prescription_id~{}|prescription_date~{}|prescription_signa~{}|doctors_iddoctors~{}'.format(
            self.prescription_id,
            self.prescription_date,
            self.prescription_signa,
            self.doctors_iddoctors)


class Medication(idb.db.Model):
    __tablename__ = 'medication'
    med_id = idb.db.Column(idb.db.INTEGER, autoincrement=True, primary_key=True)
    med_url = idb.db.Column(idb.db.String, unique=True)
    med_name = idb.db.Column(idb.db.String)
    med_man_country = idb.db.Column(idb.db.String)
    med_composition = idb.db.Column(idb.db.String)
    med_release_type = idb.db.Column(idb.db.String)

    def __init__(self, med_url, med_name, med_man_country, med_composition, med_release_type):
        # self.med_id = med_url
        self.med_url = med_url
        self.med_name = med_name
        self.med_man_country = med_man_country
        self.med_composition = med_composition
        self.med_release_type = med_release_type

    def __repr__(self):
        return 'med_id~{}|med_ur~{}|med_name~{}|med_man_country~{}|med_composition~{}|med_release_type~{}'.format(
            self.med_id,
            self.med_url,
            self.med_name,
            self.med_man_country,
            self.med_composition,
            self.med_release_type)

    def __str__(self):
        return 'med_id~{}|med_ur~{}|med_name~{}|med_man_country~{}|med_composition~{}|med_release_type~{}'.format(
            self.med_id,
            self.med_url,
            self.med_name,
            self.med_man_country,
            self.med_composition,
            self.med_release_type)


class PrescriptionMed(idb.db.Model):
    __tablename__ = 'prescription_med'
    prescriptions_prescription_id = idb.db.Column(idb.db.INTEGER, primary_key=True)
    medication_med_id = idb.db.Column(idb.db.INTEGER, primary_key=True)
    med_dosage = idb.db.Column(idb.db.String)
    med_term = idb.db.Column(idb.db.INTEGER)

    def __init__(self, medication_med_id, med_dosage, med_term):
        self.medication_med_id = medication_med_id
        self.med_dosage = med_dosage
        self.med_term = med_term

    def __repr__(self):
        return 'prescriptions_prescription_id:{}|medication_med_id:{}|med_dosage:{}|med_term:{}'.format(
            self.prescriptions_prescription_id,
            self.medication_med_id,
            self.med_dosage,
            self.med_term
        )

    def __str__(self):
        return 'prescriptions_prescription_id~{}|medication_med_id~{}|med_dosage~{}|med_term~{}'.format(
            self.prescriptions_prescription_id,
            self.medication_med_id,
            self.med_dosage,
            self.med_term)

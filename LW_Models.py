from tkinter import StringVar, IntVar, Text

class Address(object):
    """ A model class for creating a mailing address. """
    def __init__ (self):
        self.first_name = StringVar()
        self.last_name = StringVar()
        self.address = StringVar()
        self.city = StringVar()
        self.state = StringVar()
        self.zipcode = StringVar()
        self.gender = IntVar()
        self.gender.set(1)
        self.data_fields = [ ('First Name', self.first_name),
                             ('Last Name', self.last_name),
                             ('Address', self.address),
                             ('City', self.city),
                             ('State', self.state),
                             ('Zipcode', self.zipcode),
                            ]

    def return_address_block(self):
        self.address_block = self.first_name.get() + ' ' + self.last_name.get() + '\n' +\
                self.address.get() + '\n' + self.city.get() + ' ' + self.state.get() +\
                ' ' + self.zipcode.get()
        return self.address_block

    def return_salutation_block(self):
        if self.gender.get() == 1:
            return 'Dear Mr. ' + self.last_name.get() + ':'
        elif self.gender.get() == 2:
            return 'Dear Ms. ' + self.last_name.get() + ':'

    def return_cc_block(self):
        return 'cc:  Hon. Judge ' + self.last_name.get()

    def return_data_fields(self):
        return self.data_fields


class JudgeAddress(Address):
    """ A subclass of the Address class that overrides
    methods for saluation and address block."""
    def return_address_block(self):
        self.address_block = 'Hon. Judge ' + self.last_name.get() + '\n' +\
                        self.address.get() + '\n' + self.city.get() + ' ' + self.state.get() +\
                        ' ' + self.zipcode.get()
        return self.address_block

    def return_salutation_block(self):
        return 'Dear Judge ' + self.last_name.get() + ':'


class PrisonerAddress(Address):
    """ A subclass of the Address class that adds
    fields for prisoner number and institution. """
    def __init__(self):
        Address.__init__(self)
        self.inmate_number = StringVar()
        self.prison = StringVar()
        self.data_fields.insert(2, ('Prisoner Number', self.inmate_number))
        self.data_fields.insert(2, ('Institution', self.prison))


class AttorneyAddress(Address):
    """ A subclass of the Address class that adds a
    field for attorney number. """
    def __init__(self):
        Address.__init__(self)
        self.atty_number = StringVar()
        self.data_fields.insert(2, ('Attorney Number', self.atty_number))


class POLAttorneyAddress(AttorneyAddress):
    """ A subclass of the AttorneyAddress class that removes
    all fields except first and last name and attorney number."""
    def __init__(self):
        AttorneyAddress.__init__(self)
        del self.data_fields[3:]


class CaseInformation(object):
    """ A model class that includes the case name, case number,
    and court name of a case. """
    def __init__(self):
        self.case_name = StringVar()
        self.case_number = StringVar()
        self.court_name = StringVar()
        self.data_fields = [('Case Name', self.case_name),
                            ('Case Number', self.case_number),
                            ('Court Name', self.court_name),
                            ]

    def return_data_fields(self):
        return self.data_fields

class POLCaseInformation(CaseInformation):
    """ A subclassof the Case Information class that eliminates
    court name in the data fields."""
    def __init__(self):
        CaseInformation.__init__(self)
        del self.data_fields[2]


class AppReinstatementCaseInformation(POLCaseInformation):
    """ A subclassof the POL Case Information class that add fields for
    dates of court orders and filings."""
    def __init__(self):
        POLCaseInformation.__init__(self)
        self.application_date = StringVar()
        self.suspension_date = StringVar()
        self.suspension_description = StringVar()
        self.data_fields.insert(2, ('Suspension Date', self.suspension_date))
        self.data_fields.insert(3, ('Application Date', self.application_date))


class PetReinstatementCaseInformation(AppReinstatementCaseInformation):
    """ A subclassof the POL Case Information class that add fields for
    dates of court orders and filings."""
    def __init__(self):
        AppReinstatementCaseInformation.__init__(self)
        del self.data_fields[3]
        self.application_date = StringVar()
        self.report_date = StringVar()
        self.data_fields.insert(3, ('Petition Date', self.application_date))
        self.data_fields.insert(4, ('Report Date', self.report_date))


class AppProbationCaseInformation(AppReinstatementCaseInformation):
    """ A subclassof the POL Case Information class that add fields for
    dates of court orders and filings and a field for relator counsel
    of record."""
    def __init__(self):
        AppReinstatementCaseInformation.__init__(self)
        self.probation_period = StringVar()
        self.reinstatement_date = StringVar()
        self.appointment_date = StringVar()
        self.relator_COR = StringVar()
        self.data_fields.insert(4, ('Reinstatement Date', self.reinstatement_date))
        self.data_fields.insert(5, ('Monitor Appointment Date', self.appointment_date))
        self.data_fields.insert(6, ('Probation Period', self.probation_period))
        self.data_fields.insert(7, ('Relator COR', self.relator_COR))

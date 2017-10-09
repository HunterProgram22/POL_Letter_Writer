from tkinter.filedialog import askopenfilename
from tkinter import messagebox, END
import os, docx, time
#from LW_Labels import printLabels


GEN_FILEPATH = 'S:\\Deputy Clerks'

POL_PATH = "S:\\Practice of Law\\Practice of Law Documents\\"
ARE_PATH = "Letters to Agencies\\Applications for Reinstatement\\"
PRL_PATH = "Letters to Agencies\\Petitions for Reinstatement\\"
ATP_PATH = "Letters to Agencies\\Termination of Probation\\"

TEMPLATE_PATH = "S:\\Practice of Law\\Practice of Law Documents\\Templates\\"
POL_TEMPLATE = TEMPLATE_PATH + 'NewDocument.docx'
ARE_TEMPLATE = POL_PATH + ARE_PATH + "NewDocument.docx"
PRL_TEMPLATE = POL_PATH + PRL_PATH + "NewDocument.docx"
ATP_TEMPLATE = POL_PATH + ATP_PATH + "NewDocument.docx"

LFCP_APP_REINSTATE_TEMPLATE = TEMPLATE_PATH + 'LFCP_APP_REINSTATE_TEMPLATE.docx'
LFCP_ATP_PROBATION_TEMPLATE = TEMPLATE_PATH + 'LFCP_ATP_PROBATION_TEMPLATE.docx'
BOARD_APP_REINSTATE_TEMPLATE = TEMPLATE_PATH  + 'BOARD_APP_REINSTATE_TEMPLATE.docx'
BOARD_ATP_PROBATION_TEMPLATE = TEMPLATE_PATH  + 'BOARD_ATP_PROBATION_TEMPLATE.docx'
BOARD_PET_REINSTATE_TEMPLATE = TEMPLATE_PATH  + 'BOARD_PET_REINSTATE_TEMPLATE.docx'
OAS_APP_REINSTATE_TEMPLATE = TEMPLATE_PATH  + 'OAS_APP_REINSTATE_TEMPLATE.docx'
OAS_ATP_PROBATION_TEMPLATE = TEMPLATE_PATH  + 'OAS_ATP_PROBATION_TEMPLATE.docx'
OLAP_APP_REINSTATE_TEMPLATE = TEMPLATE_PATH  + 'OLAP_APP_REINSTATE_TEMPLATE.docx'
APPLICANT_PROBATION_TEMPLATE = TEMPLATE_PATH  + 'APPLICANT_PROBATION_TEMPLATE.docx'


DATE_LETTER = time.strftime("%B %d, %Y")
DATE_FILENAME = time.strftime("%m-%d-%y")


# MENU BUTTONS
def open_blank_file():
    os.startfile(TEMPLATE)

def open_existing_ARE_file():
    name = askopenfilename(initialdir=POL_PATH + ARE_PATH)
    if name:
        os.startfile(name)
    else:
        return None

def open_existing_PRL_file():
    name = askopenfilename(initialdir=POL_PATH + PRL_PATH)
    if name:
        os.startfile(name)
    else:
        return None

def open_existing_ATP_file():
    name = askopenfilename(initialdir=POL_PATH + ATP_PATH)
    if name:
        os.startfile(name)
    else:
        return None

def open_doc(document):
    if messagebox.askyesno("Modify Template?",
            "If you modify the template and then save the changes they are permanent " +\
            "and future letters will incorporate the changes, do you want to proceed?"):
        os.startfile(document)
    else:
        return None

def print_doc(document):
    os.startfile(document, "print")

def application_exit():
    exit()

#def button_print_label(recipient):
    #printLabels(recipient)

def button_create_BOARD_letter(tab):
    if tab.tab_name == "ARE":
        fields = return_field_values(tab.attorney_fields, tab.case_information_fields,
                        tab, tab.text_field)
        letter = BOARD_AppForReinstatementLetter(tab.attorney_fields, ARE_TEMPLATE)
    elif tab.tab_name == "PRL":
        fields = return_field_values(tab.attorney_fields, tab.case_information_fields, tab)
        letter = BOARD_PetForReinstatementLetter(tab.attorney_fields, PRL_TEMPLATE)
    elif tab.tab_name == "ATP":
        fields = return_field_values(tab.attorney_fields, tab.case_information_fields,
                        tab, tab.text_field)
        letter = BOARD_AppForProbationLetter(tab.attorney_fields, ATP_TEMPLATE)
    letter.create_letter(fields)

def button_create_OAS_letter(tab):
    fields = return_field_values(tab.attorney_fields, tab.case_information_fields,
                        tab, tab.text_field)
    if tab.tab_name == "ARE":
        letter = OAS_AppForReinstatementLetter(tab.attorney_fields, ARE_TEMPLATE)
    elif tab.tab_name == "ATP":
        letter = OAS_AppForProbationLetter(tab.attorney_fields, ATP_TEMPLATE)
    letter.create_letter(fields)

def button_create_LFCP_letter(tab):
    fields = return_field_values(tab.attorney_fields, tab.case_information_fields,
                        tab, tab.text_field)
    if tab.tab_name == "ARE":
        letter = LFCP_AppForReinstatementLetter(tab.attorney_fields, ARE_TEMPLATE)
    elif tab.tab_name == "ATP":
        letter = LFCP_AppForProbationLetter(tab.attorney_fields, ATP_TEMPLATE)
    letter.create_letter(fields)

def button_create_OLAP_letter(tab):
    fields = return_field_values(tab.attorney_fields, tab.case_information_fields,
                        tab, tab.text_field)
    letter = OLAP_AppForReinstatementLetter(tab.attorney_fields, ARE_TEMPLATE)
    letter.create_letter(fields)

def button_create_APPLICANT_letter(tab):
    fields = return_field_values(tab.attorney_fields, tab.case_information_fields,
                        tab, tab.text_field)
    letter = APPLICANT_AppForProbationLetter(tab.attorney_fields, ATP_TEMPLATE)
    letter.create_letter(fields)

def return_field_values(attorney, case_information, tab, tab_text=None):
    field_values = {}
    if attorney.gender.get() == 1:
        field_values["prefix"] = "Mr."
        field_values["gender"] ="his"
    else:
        field_values["prefix"] = "Ms."
        field_values["gender"] = "her"
    field_values["first_name"] = attorney.first_name.get()
    field_values["last_name"] = attorney.last_name.get()
    field_values["attorney_number"] = attorney.atty_number.get()
    field_values["address"] = attorney.address.get()
    field_values["city"] = attorney.city.get()
    field_values["state"] = attorney.state.get()
    field_values["zipcode"] = attorney.zipcode.get()
    field_values["case_name"] = case_information.case_name.get()
    field_values["case_number"] = case_information.case_number.get()
    field_values["application_date"] = case_information.application_date.get()
    field_values["suspension_date"] = case_information.suspension_date.get()
    if tab.tab_name == "ATP":
        field_values["probation_period"] = case_information.probation_period.get()
        field_values["reinstatement_date"] = case_information.reinstatement_date.get()
        field_values["appointment_date"] = case_information.appointment_date.get()
        field_values["relator_COR"] = case_information.relator_COR.get()
        field_values["suspension_description"] = tab_text.get("1.0", "end-1c")
    if tab.tab_name == "PRL":
        field_values["report_date"] = case_information.report_date.get()
    if tab.tab_name == "ARE":
        field_values["suspension_description"] = tab_text.get("1.0", "end-1c")
    return field_values


# CLEAR BUTTONS
def clear_fields(fields):
    for field in fields.data_fields:
        field[1].set('')


class Letter(object):
    """ A class controller object that is the base for creating letters."""
    def __init__(self, recipient, *args):
        self.letter = docx.Document(TEMPLATE)
        self.recipient = recipient
        self.date_paragraph = self.letter.add_paragraph(DATE_LETTER)
        self.date_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        self.letter.add_paragraph(self.recipient.return_address_block())
        if args:
            self.args = args
            self.case_info = args[0]
            self.letter.add_paragraph(self.case_info.return_re_block())
        self.letter.add_paragraph(self.recipient.return_salutation_block())

    def add_signature_block(self, staff_member):
        self.letter.add_paragraph(staff_member)

    def save_and_open_letter(self, *subargs):
        if subargs:
            self.docname = self.recipient.last_name.get() + ', ' +\
            self.recipient.first_name.get() + ' (' + subargs[0].last_name.get() + ', ' +\
            subargs[0].first_name.get() + ' ' + DATE_FILENAME + ').docx'
        else:
            self.docname = self.recipient.last_name.get() + ', ' + self.recipient.first_name.get() + ' (' +\
                    DATE_FILENAME + ').docx'
        self.letter.save(PATH + self.docname)
        os.startfile(PATH + self.docname)


class POL_Letter(Letter):
    def __init__(self, attorney, template):
        self.working_document = template
        self.letter = docx.Document(self.working_document)
        for paragraph in self.letter.paragraphs:
            p = paragraph._element
            p.getparent().remove(p)
            p._p = p._element = None
        self.letter.save(self.working_document)
        self.attorney = attorney
        self.path = POL_PATH

    def create_letter(self, fields):
        self.master_template = docx.Document(self.template)
        self.string = ""
        for paragraph in self.master_template.paragraphs:
            self.string = self.string + '\n' + paragraph.text
        self.newstring = self.string.format(**fields)
        self.letter.add_paragraph(self.newstring)
        self.letter.save(self.working_document)
        os.startfile(self.working_document)

    def open_letter(self):
        os.startfile(TEMPLATE)

    def save_and_open_letter(self, agency):
        self.docname = self.attorney.last_name.get() + ', ' +\
                self.attorney.first_name.get() + ' (' + agency + ').docx'
        self.letter.save(self.path + self.docname)
        os.startfile(self.path + self.docname)


class BOARD_AppForReinstatementLetter(POL_Letter):
    def __init__(self, attorney, template):
        POL_Letter.__init__(self, attorney, template)
        self.template = BOARD_APP_REINSTATE_TEMPLATE
        self.agency = "BOARD"
        self.path = POL_PATH + ARE_PATH


class BOARD_AppForProbationLetter(POL_Letter):
    def __init__(self, attorney, template):
        POL_Letter.__init__(self, attorney, template)
        self.template = BOARD_ATP_PROBATION_TEMPLATE
        self.agency = "BOARD"
        self.path = POL_PATH + ATP_PATH


class BOARD_PetForReinstatementLetter(POL_Letter):
    def __init__(self, attorney, template):
        POL_Letter.__init__(self, attorney, template)
        self.template = BOARD_PET_REINSTATE_TEMPLATE
        self.agency = "BOARD"
        self.path = POL_PATH + PRL_PATH


class LFCP_AppForReinstatementLetter(POL_Letter):
    def __init__(self, attorney, template):
        POL_Letter.__init__(self, attorney, template)
        self.template = LFCP_APP_REINSTATE_TEMPLATE
        self.agency = "LFCP"
        self.path = POL_PATH + ARE_PATH


class LFCP_AppForProbationLetter(POL_Letter):
    def __init__(self, attorney, template):
        POL_Letter.__init__(self, attorney, template)
        self.template = LFCP_ATP_PROBATION_TEMPLATE
        self.agency = "LFCP"
        self.path = POL_PATH + ATP_PATH


class OAS_AppForReinstatementLetter(POL_Letter):
    def __init__(self, attorney, template):
        POL_Letter.__init__(self, attorney, template)
        self.template = OAS_APP_REINSTATE_TEMPLATE
        self.agency = "OAS"
        self.path = POL_PATH + ARE_PATH


class OAS_AppForProbationLetter(POL_Letter):
    def __init__(self, attorney, template):
        POL_Letter.__init__(self, attorney, template)
        self.template = OAS_ATP_PROBATION_TEMPLATE
        self.agency = "OAS"
        self.path = POL_PATH + ATP_PATH


class OLAP_AppForReinstatementLetter(POL_Letter):
    def __init__(self, attorney, template):
        POL_Letter.__init__(self, attorney, template)
        self.template = OLAP_APP_REINSTATE_TEMPLATE
        self.agency = "OLAP"
        self.path = POL_PATH + ARE_PATH


class APPLICANT_AppForProbationLetter(POL_Letter):
    def __init__(self, attorney, template):
        POL_Letter.__init__(self, attorney, template)
        self.template = APPLICANT_PROBATION_TEMPLATE
        self.agency = "Applicant"
        self.path = POL_PATH + ATP_PATH


def main():
    pass

if __name__ == '__main__':
    main()

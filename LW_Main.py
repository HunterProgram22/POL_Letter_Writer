from tkinter import Tk, E
import tkinter.ttk as ttk
from LW_Views import AppWindow
from LW_Models import Address, JudgeAddress, CaseInformation, POLCaseInformation, \
    POLAttorneyAddress, AppReinstatementCaseInformation, PetReinstatementCaseInformation, \
    AppProbationCaseInformation, AttorneyAddress
from LW_Controller import *
from LW_Labels import print_label_template, print_label


TEMPLATE_PATH = "S:\\Practice of Law\\Practice of Law Documents\\Templates\\"

LFCP_APP_REINSTATE_TEMPLATE = TEMPLATE_PATH + 'LFCP_APP_REINSTATE_TEMPLATE.docx'
LFCP_ATP_PROBATION_TEMPLATE = TEMPLATE_PATH + 'LFCP_ATP_PROBATION_TEMPLATE.docx'
BOARD_APP_REINSTATE_TEMPLATE = TEMPLATE_PATH  + 'BOARD_APP_REINSTATE_TEMPLATE.docx'
BOARD_ATP_PROBATION_TEMPLATE = TEMPLATE_PATH  + 'BOARD_ATP_PROBATION_TEMPLATE.docx'
BOARD_PET_REINSTATE_TEMPLATE = TEMPLATE_PATH  + 'BOARD_PET_REINSTATE_TEMPLATE.docx'
OAS_APP_REINSTATE_TEMPLATE = TEMPLATE_PATH  + 'OAS_APP_REINSTATE_TEMPLATE.docx'
OAS_ATP_PROBATION_TEMPLATE = TEMPLATE_PATH  + 'OAS_ATP_PROBATION_TEMPLATE.docx'
OLAP_APP_REINSTATE_TEMPLATE = TEMPLATE_PATH  + 'OLAP_APP_REINSTATE_TEMPLATE.docx'
APPLICANT_PROBATION_TEMPLATE = TEMPLATE_PATH  + 'APPLICANT_PROBATION_TEMPLATE.docx'

TAB_LIST = ['App for Reinstatement', 'Petition for Reinstatement', 'Termination of Probation',]

root = Tk()
root.geometry("950x900")
root.title("Practice of Law Letter Writer")

rows = 0
while rows < 50:
    root.rowconfigure(rows, weight=1)
    root.columnconfigure(rows, weight=1)
    rows += 1
application = AppWindow(root)
application.init_tabs(TAB_LIST)


"___ARE TAB___"
are_tab = application.tab_list[0]
are_tab.set_tab_name("ARE")
are_tab.add_heading('Attorney')
are_tab.add_attorney_fields(POLAttorneyAddress())
are_tab.init_tab_fields_list(are_tab.attorney_fields, gender='Yes')

are_tab.set_row_cursor(6)
are_tab.add_heading('Case Information')
are_tab.add_case_information_fields(AppReinstatementCaseInformation())
are_tab.init_tab_fields_list(are_tab.case_information_fields)
are_tab.init_text_tab_field('Suspension')

are_tab.set_col_cursor(2)
are_tab.set_row_cursor(2)

are_tab.init_button("Create Board Letter", lambda: button_create_BOARD_letter(are_tab))
are_tab.init_button("Create OAS Letter", lambda: button_create_OAS_letter(are_tab))
are_tab.init_button("Create LFCP Letter", lambda: button_create_LFCP_letter(are_tab))
are_tab.init_button("Create OLAP Letter", lambda: button_create_OLAP_letter(are_tab))
are_tab.set_row_cursor(7)
are_tab.init_button("Clear Attorney", lambda: clear_fields(are_tab.attorney_fields))
are_tab.init_button("Clear Case Information", lambda: clear_fields(are_tab.case_information_fields))
are_tab.set_col_cursor(3)
are_tab.set_row_cursor(2)
are_tab.init_button("Print Board Label", lambda: print_label_template(BOARD_APP_REINSTATE_TEMPLATE))
are_tab.init_button("Print OAS Label", lambda: print_label_template(OAS_APP_REINSTATE_TEMPLATE))
are_tab.init_button("Print LFCP Label", lambda: print_label_template(LFCP_APP_REINSTATE_TEMPLATE))
are_tab.init_button("Print OLAP Label", lambda: print_label_template(OLAP_APP_REINSTATE_TEMPLATE))


"___PRL TAB___"
prl_tab = application.tab_list[1]
prl_tab.set_tab_name("PRL")
prl_tab.add_heading('Attorney')
prl_tab.add_attorney_fields(POLAttorneyAddress())
prl_tab.init_tab_fields_list(prl_tab.attorney_fields, gender='Yes')

prl_tab.set_row_cursor(6)
prl_tab.add_heading('Case Information')
prl_tab.add_case_information_fields(PetReinstatementCaseInformation())
prl_tab.init_tab_fields_list(prl_tab.case_information_fields)

prl_tab.set_col_cursor(2)
prl_tab.set_row_cursor(2)
prl_tab.init_button("Create Board Letter", lambda: button_create_BOARD_letter(prl_tab))
prl_tab.set_row_cursor(4)
prl_tab.init_button("Clear Attorney", lambda: clear_fields(prl_tab.attorney_fields))
prl_tab.set_row_cursor(7)
prl_tab.init_button("Clear Case Information", lambda: clear_fields(prl_tab.case_information_fields))
prl_tab.set_col_cursor(3)
prl_tab.set_row_cursor(2)
prl_tab.init_button("Print Board Label", lambda: print_label_template(BOARD_PET_REINSTATE_TEMPLATE))


"___ATP TAB___"
atp_tab = application.tab_list[2]
atp_tab.set_tab_name("ATP")
atp_tab.add_heading('Attorney')
atp_tab.add_attorney_fields(AttorneyAddress())
atp_tab.init_tab_fields_list(atp_tab.attorney_fields, gender='Yes')

atp_tab.add_heading('Case Information')
atp_tab.add_case_information_fields(AppProbationCaseInformation())
atp_tab.init_tab_fields_list_split(atp_tab.case_information_fields)
atp_tab.set_row_cursor(15)
atp_tab.set_col_cursor(0)
atp_tab.init_text_tab_field('Suspension', height=8)

atp_tab.set_col_cursor(2)
atp_tab.set_row_cursor(2)
atp_tab.init_button("Create Board Letter", lambda: button_create_BOARD_letter(atp_tab))
atp_tab.init_button("Create OAS Letter", lambda: button_create_OAS_letter(atp_tab))
atp_tab.init_button("Create LFCP Letter", lambda: button_create_LFCP_letter(atp_tab))
atp_tab.init_button("Create Applicant Letter", lambda: button_create_APPLICANT_letter(atp_tab))
atp_tab.set_row_cursor(8)
atp_tab.init_button("Clear Attorney", lambda: clear_fields(atp_tab.attorney_fields))
atp_tab.set_row_cursor(10)
atp_tab.init_button("Clear Case Information", lambda: clear_fields(atp_tab.case_information_fields))
atp_tab.set_col_cursor(3)
atp_tab.set_row_cursor(2)
atp_tab.init_button("Print Board Label", lambda: print_label_template(BOARD_ATP_PROBATION_TEMPLATE))
atp_tab.init_button("Print OAS Label", lambda: print_label_template(OAS_ATP_PROBATION_TEMPLATE))
atp_tab.init_button("Print LFCP Label", lambda: print_label_template(LFCP_ATP_PROBATION_TEMPLATE))
atp_tab.init_button("Print Applicant Label", lambda: print_label(atp_tab.attorney_fields))


root.mainloop()

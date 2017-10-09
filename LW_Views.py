from tkinter import Frame, Menu, W, E, Label, Entry, Radiobutton, Checkbutton, \
    Button, Text, WORD
import tkinter.ttk as ttk
from LW_Controller import open_blank_file, open_existing_ARE_file, open_existing_PRL_file, \
    open_existing_ATP_file, application_exit, print_doc, open_doc
from LW_Addresses import PRISON_LIST
from tinydb import TinyDB, Query
from functools import partial

BTNWIDTH = 20
TEMPLATE_PATH = "S:\\Practice of Law\\Practice of Law Documents\\Templates\\"
TEMPLATE = TEMPLATE_PATH + 'Template.docx'


class AppWindow(ttk.Frame):
    """ A class view object for creating the main application window. """
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.master = master
        self.style = ttk.Style()
        self.style.configure('BlueText.TButton', font='helvetica 8', foreground='blue', padding=5)
        self.db = TinyDB(TEMPLATE_PATH + "Templates.JSON")
        self.init_window()
        self.init_menu()


    def init_window(self):
        """ Initialiezs the main window as a notebook object. """
        self.notebook = ttk.Notebook(self.master)
        self.notebook.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

    def init_menu(self):
        """ Initializes the menu of the main application."""
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu, borderwidth=10)
        self.file = Menu(self.menu)
        self.edit_templates = Menu(self.menu)
        self.file.add_command(label="New", command=open_blank_file)
        self.file.add_command(label="Open ARE Letter", command=open_existing_ARE_file)
        self.file.add_command(label="Open PRL Letter", command=open_existing_PRL_file)
        self.file.add_command(label="Open ATP Letter", command=open_existing_ATP_file)
        self.file.add_command(label="Exit", command=application_exit)
        self.template_list = []
        for item in self.db:
            self.edit_templates.add_command(label=item['name'], command=partial(open_doc, TEMPLATE_PATH + item['docpath']))
        self.menu.add_cascade(label="File", menu=self.file)
        self.menu.add_cascade(label="Edit Templates", menu=self.edit_templates)

    def init_tabs(self, tab_list):
        """ Initializes tabs from a list provided as an argument and creates a
        list of the tabs. """
        self.tab_list = []
        for tabs in tab_list:
            self.tab = TabWindow(self.notebook)
            self.notebook.add(self.tab, text=tabs)
            self.tab_list.append(self.tab)


class TabWindow(ttk.Frame):
    """ A class view object for creating tab windows on the main application. """
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.master = master
        self.row_cursor = 0 # Used for setting fields in tab window
        self.col_cursor = 0

    def set_col_cursor(self, column):
        self.col_cursor = column

    def set_row_cursor(self, row):
        self.row_cursor = row

    def set_tab_name(self, name):
        self.tab_name = name

    def add_attorney_fields(self, attorney_object):
        self.attorney_fields = attorney_object

    def add_case_information_fields(self, case_information_object):
        self.case_information_fields = case_information_object

    def add_heading(self, heading):
        """ Adds a heading to a tab window and moves the row cursor to
        the next row. """
        ttk.Label(self, text=heading, width=30, font="Times 12 bold").grid(
                    row=self.row_cursor, column=self.col_cursor, columnspan=2, sticky=W,
                    pady=10, padx=5)
        self.row_cursor += 1

    def add_sub_heading(self, subheading):
        """ Adds a sub-heading (smaller font than heading) to a tab window and
        moves the row cursor to the next row. """
        ttk.Label(self, text=subheading, width=50, font="Times 8").grid(
                        row=self.row_cursor, column=self.col_cursor, columnspan=2,
                        pady=5, padx=20)
        self.row_cursor += 1

    def init_tab_fields_list(self, model, gender='No'):
        """ Initializes the fields from a model object on to the tab window.
        Tracks the row (row_cursor) of each field so that fields do not
        overlap on create."""
        self.model = model #Model is the type of model from the model package (i.e. attorney or case information)
        if gender == 'Yes':
            self.add_gender_button()
        for field in self.model.return_data_fields():
            Label(self, text=field[0]).grid(row=self.row_cursor, column=self.col_cursor,
                    sticky=W, padx=10, pady=5)
            Entry(self, textvariable=field[1], width=20).grid(row=self.row_cursor,
                    column=self.col_cursor+1, pady=5)
            self.row_cursor += 1

    def init_tab_fields_list_split(self, model, gender='No'):
        """ Initializes the fields from a model object on to the tab window.
        Tracks the row (row_cursor) of each field so that fields do not
        overlap on create. Splits large lists into two columns."""
        self.model = model #Model is the type of model from the model package (i.e. attorney or case information)
        if gender == 'Yes':
            self.add_gender_button()
        count = 0
        for field in self.model.return_data_fields():
            if count == 5:
                self.row_cursor = self.row_cursor - 3
                self.col_cursor = self.col_cursor + 2
            Label(self, text=field[0]).grid(row=self.row_cursor, column=self.col_cursor,
                    sticky=W, padx=10, pady=5)
            Entry(self, textvariable=field[1], width=20).grid(row=self.row_cursor,
                    column=self.col_cursor+1, pady=5)
            self.row_cursor += 1
            count += 1


    def add_gender_button(self):
        Radiobutton(self, text="Mr.", variable=self.model.gender, value=1).grid(
                    row=self.row_cursor, column=self.col_cursor, sticky=E)
        Radiobutton(self, text="Ms.", variable=self.model.gender, value=2).grid(
                    row=self.row_cursor, column=self.col_cursor + 1, sticky=W)
        self.row_cursor += 1

    def init_text_tab_field(self, text, height=10, width=50, columnspan=3):
        """Initializes a single field from a model object on to the tab window.
        Moves row_cursor to the next row."""
        Label(self, text=text).grid(row=self.row_cursor, column=self.col_cursor,
                        sticky=W, padx=10, pady=5)
        self.text_field = Text(self, width=width, height=height, wrap=WORD)
        self.text_field.grid(row=self.row_cursor, column=self.col_cursor + 1, columnspan=columnspan, pady=5)
        self.text_field.insert("1.0", "")
        self.row_cursor += 1

    def init_buttons_list(self, button_list):
        """ Initializes a list of buttons for a tab. """
        for button in button_list:
            ttk.Button(self, text=button[0], command=button[1], width=BTNWIDTH, style="BlueText.TButton").grid(
                            row=self.row_cursor, column=self.col_cursor, sticky=W, padx=10)
            self.row_cursor += 1

    def init_button(self, button_name, button_command):
        """ Initializes a single button for a tab. """
        ttk.Button(self, text=button_name, command=button_command, width=BTNWIDTH, style="BlueText.TButton").grid(
                    row=self.row_cursor, column=self.col_cursor, padx=10, pady=3)
        self.row_cursor += 1

    def init_radio_button_yes_no(self, letter_type, variable, question):
        """ Initializes a radio button to answer yes or no to a statement."""
        self.letter_type = letter_type
        self.variable = variable
        self.variable.set(1)
        ttk.Label(self, text=question, width=50, font="Times 10").grid(
                        row=self.row_cursor, column=self.col_cursor, columnspan=2,
                        pady=5, padx=20)
        self.row_cursor += 1
        Radiobutton(self, text="Yes", variable=self.variable, value=1).grid(
                    row=self.row_cursor, column=0, sticky=E)
        Radiobutton(self, text="No", variable=self.variable, value=2).grid(
                    row=self.row_cursor, column=1, sticky=W)
        self.row_cursor += 1

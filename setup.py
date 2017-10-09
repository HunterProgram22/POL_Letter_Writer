from cx_Freeze import setup, Executable
import sys
import os


os.environ['TCL_LIBRARY'] = "C:\\Users\\kudelaj\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\kudelaj\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6"


#base = "Win32GUI" #Use Win32GUI for errors or None for use
base = None

if sys.platform == 'win32':
    base = "Win32GUI"


INCLUDE_MODULES = [

    'lxml',
    'lxml._elementpath',
    'tinydb',
]




executables = [Executable("LW_Main.py", base=base)]

packages = []
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "Letter Writer",
    options =  {'build_exe':{'includes': INCLUDE_MODULES}},
    version = "0.1",
    description = 'First Test',
    executables = executables
)

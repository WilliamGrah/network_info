import sys
from cx_Freeze import setup, Executable
import os


os.environ['TCL_LIBRARY'] = r'C:\Users\William\AppData\Local\Programs\Python\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\William\AppData\Local\Programs\Python\Python36\tcl\tk8.6'

packages = ["idna","tkinter","_tkinter"]
excludes = []
include_files = [
	r'c:\Users\William\AppData\Local\Programs\Python\Python36\DLLs\tcl86t.dll',
	r'c:\Users\William\AppData\Local\Programs\Python\Python36\DLLs\tk86t.dll'
]

options = {
    'build_exe': {
        'packages': packages,
        'excludes': excludes,
        'include_files': include_files
    },
}

setup( 
	name = "main",
	options=options,
	version = "0.1",
	description = "",
	executables = [
		Executable(
			"main.py",
			base = "Win32GUI",
			icon="icon.ico"
  			#compress=False,
    		#copyDependentFiles=True,
    		#appendScriptToExe=True,
    		#appendScriptToLibrary=False,
		)
	]
)

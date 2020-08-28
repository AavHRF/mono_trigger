import PySimpleGUI as sg
import layout as l
import client_functions as cf
import os

app_layout = l.return_app_layout()
version = cf.get_version()

window = sg.Window(f"Mono_Trigger v{version}", layout=app_layout)

while True:
    event = window.Read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    # Get events and execute the proper program based on that
    if event == "Tagging":
        os.system("python3 tagging.py")

    if event == "Operations":
        os.system("python3 ops.py")
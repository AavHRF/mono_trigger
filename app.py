import client_functions as cf
import PySimpleGUI as sg
import layout as l

# VERSION NUMBER
version = "0.1.0a"

# Variable assignment for later
verification_status = False
watch_list = ""
trig_list = dict()
useragent = ""
user_agent = ""

# Get our window layout
layout = dict()
layout = l.return_layout()

# Create & theme the window
sg.theme("Dark Blue 3")

window = sg.Window(f"Mono_Trigger v. {version}", layout=layout)

# Event loop

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == "Verify Nation":
        useragent = values['UAGENT']
        user_agent = cf.sanitize(useragent)
        verify_response = cf.verify_nation(useragent)
        if verify_response == True:
            print("Nation verified successfully!")
            verification_status = True

        elif verify_response == False:
            print("Nation not successfully verified!")

    if event == "Load List":
        try:
            watch_list = sg.popup_get_file("Trigger List")
        except Exception as e:
            print(e)
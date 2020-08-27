import client_functions as cf
import PySimpleGUI as sg

version = cf.get_version()
verification_status = False
useragent = ""
user_agent = ""

layout = [
    [sg.Text('Input Nation'), sg.Input(key='UAGENT')],
    [sg.Text('Input Trigger'), sg.Input(key='TRIG')],
    [sg.Output(size=(50, 10))],
    [sg.Button("Verify Nation"), sg.Button("Begin Watch"), sg.Button('Exit')]
]

window = sg.Window(f"Mono_Trigger v{version}" layout=layout)

while True:
    event, values = window.Read()

    # Break condition
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    # Verification
    if event == "Verify Nation":
        useragent = values['UAGENT']
        user_agent = cf.sanitize(useragent)
        verify_response = cf.verify_nation(user_agent)
        if verify_response == True:
            print("Nation verified successfully!")
            verification_status = True

        elif verify_response == False:
            print("Nation not successfully verified!")

    # Triggering
    if verification_status == False:
        print("Nation is not verified! You must verify your nation to use this tool!")

    else:
        print("Beginning target watch!")
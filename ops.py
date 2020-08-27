import client_functions as cf
import PySimpleGUI as sg

version = cf.get_version()
verification_status = False
useragent = ""
user_agent = ""
starting_inf = ""
trig_nation = ""


layout = [
    [sg.Text('Input Nation'), sg.Input(key='UAGENT')],
    [sg.Text('Input Trigger'), sg.Input(key='TRIG')],
    [sg.Output(size=(50, 10))],
    [sg.Button("Verify Nation"), sg.Button("Begin Watch"), sg.Button('Exit')]
]

window = sg.Window(f"Mono_Trigger v{version}", layout=layout)

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
        if verify_response:
            print("Nation verified successfully!")
            verification_status = True

        elif not verify_response:
            print("Nation not successfully verified!")

    # Triggering
    if event == "Begin Watch":
        if not verification_status:
            print("Nation is not verified! You must verify your nation to use this tool!")

        else:
            trig_nation = values['TRIG']
            print("Beginning target watch!")
            # Get our initial influence value for the trigger nation, and then begin calls.
            starting_inf = cf.watch_nation(trig_nation, user_agent)

            while True:
                inf_watch = cf.watch_nation(trig_nation, user_agent)

                # Check influence condition, if it changes, the nation updated and it's GO TIME!
                if inf_watch != starting_inf:
                    print("UPDATE EVENT DETECTED!")
                    break

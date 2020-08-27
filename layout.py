import PySimpleGUI as sg

def return_layout():
    layout = [
              [sg.Text('Input Nation'), sg.Input(key='UAGENT')],
              [sg.Text('Use Default Ratelimit (0.6s)'), sg.Checkbox('', change_submits=True, enable_events=True, default='1', key="DUM")],
              [sg.Text('Ratelimit Override (Box must not be checked)'), sg.Input(key='RLIM', size=("5"))],
              [sg.Output(size=(60, 10))],
              [sg.Button("Load List"), sg.Button("Verify Nation"), sg.Button("Start Triggering"), sg.Button('Exit')]
    ]
    return layout
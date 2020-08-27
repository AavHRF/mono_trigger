import PySimpleGUI as sg

def return_layout():
    layout = [
              [sg.Text('Input Nation'), sg.Input(key='UAGENT')],
              [sg.Text('Download New Dump'), sg.Checkbox('', change_submits=True, enable_events=True, default='1', key="DUM")],
              [sg.Output(size=(80, 20))],
              [sg.Button("Load List"), sg.Button("Verify Nation"), sg.Button("Start Triggering"), sg.Button('Exit')]
    ]
    return layout
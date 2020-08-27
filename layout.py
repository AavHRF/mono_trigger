import PySimpleGUI as sg

def return_layout():
    layout = [
              [sg.Text('Input Nation'), sg.Input(key='UAGENT')],
              [sg.Output(size=(60, 10))],
              [sg.Button("Load List"), sg.Button("Verify Nation"), sg.Button("Start Triggering"), sg.Button('Exit')]
    ]
    return layout
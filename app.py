import PySimpleGUI as sg
import layout as l
import client_functions as cf

app_layout = l.return_app_layout()
version = cf.get_version()

window = sg.Window(f"Mono_Trigger v{version}", layout=app_layout)

while True:
    event = window.Read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    # Get events and execute the proper program based on that
    if event == "Tagging":
        window.Hide()
        # Variable assignment for later
        verification_status = False
        watch_list = ""
        trig_list = list()
        useragent = ""
        user_agent = ""
        sort_list = dict()
        sorted_list = dict()

        # Get our window layout
        layout = l.return_layout()

        # Create the window
        tag_window = sg.Window(f"Mono_Trigger v. {version}", layout=layout)

        # Event loop

        while True:
            t_event, t_values = tag_window.read()

            if t_event == sg.WIN_CLOSED or t_event == 'Exit':
                break

            if t_event == "Verify Nation":
                useragent = t_values['UAGENT']
                user_agent = cf.sanitize(useragent)
                verify_response = cf.verify_nation(user_agent)
                if verify_response == True:
                    print("Nation verified successfully!")
                    verification_status = True

                elif verify_response == False:
                    print("Nation not successfully verified!")

            if t_event == "Load List":
                try:
                    watch_list = sg.popup_get_file("Trigger List")
                    trig_list = cf.create_trigger_list(watch_list)
                except Exception as e:
                    print(e)

            if t_event == "Start Triggering":
                if verification_status == False:
                    print("You either have not verified your useragent, or you have supplied one that does not work!")
                    cf.debug_log("Verification catch (trigger start function)")
                else:
                    for reg in trig_list:
                        up_time = cf.watch_region(reg, user_agent)
                        sort_list.update(reg, up_time)

                        # Returns as a list of sorted tuples
                        sorted_list = sorted(sort_list.items(), key=operator.itemgetter(1))

                    # Now we have a sorted list of regions to trigger, and now we start watching
                    i = 0
                    while i < len(trig_list):
                        c_target = sorted_list[i]
                        upd_time = c_target[1]
                        while True:
                            watch = cf.watch_region(c_target[0], user_agent)
                            if watch != upd_time:
                                print('UPDATE EVENT DETECTED!')
                                break

    if event == "Operations":
        window.Hide()
        verification_status = False
        useragent = ""
        user_agent = ""
        starting_inf = ""
        trig_nation = ""

        op_layout = [
            [sg.Text('Input Nation'), sg.Input(key='UAGENT')],
            [sg.Text('Input Trigger'), sg.Input(key='TRIG')],
            [sg.Output(size=(50, 10))],
            [sg.Button("Verify Nation"), sg.Button("Begin Watch"), sg.Button('Exit')]
        ]

        o_window = sg.Window(f"Mono_Trigger v{version}", layout=op_layout)

        while True:
            o_event, o_values = o_window.Read()

            # Break condition
            if o_event == sg.WIN_CLOSED or o_event == 'Exit':
                break

            # Verification
            if o_event == "Verify Nation":
                useragent = o_values['UAGENT']
                user_agent = cf.sanitize(useragent)
                verify_response = cf.verify_nation(user_agent)
                if verify_response:
                    print("Nation verified successfully!")
                    verification_status = True

                elif not verify_response:
                    print("Nation not successfully verified!")

            # Triggering
            if o_event == "Begin Watch":
                if not verification_status:
                    print("Nation is not verified! You must verify your nation to use this tool!")

                else:
                    trig_nation = o_values['TRIG']
                    print("Beginning target watch!")
                    # Get our initial influence value for the trigger nation, and then begin calls.
                    starting_inf = cf.watch_nation(trig_nation, user_agent)

                    while True:
                        inf_watch = cf.watch_nation(trig_nation, user_agent)

                        # Check influence condition, if it changes, the nation updated and it's GO TIME!
                        if inf_watch != starting_inf:
                            print("UPDATE EVENT DETECTED!")
                            break

    window.UnHide()
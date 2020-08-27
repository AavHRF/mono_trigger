import client_functions as cf
import PySimpleGUI as sg
import layout as l
import operator

# VERSION NUMBER
version = "1.0.0a"

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
        verify_response = cf.verify_nation(user_agent)
        if verify_response == True:
            print("Nation verified successfully!")
            verification_status = True

        elif verify_response == False:
            print("Nation not successfully verified!")

    if event == "Load List":
        try:
            watch_list = sg.popup_get_file("Trigger List")
            trig_list = cf.create_trigger_list(watch_list)
        except Exception as e:
            print(e)

    if event == "Start Triggering":
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



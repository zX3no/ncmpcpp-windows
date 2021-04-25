from mpd import MPDClient
import sys

from pynput import keyboard

def main():

    class MyException(Exception): pass

    VOL_INC = 5

    client = MPDClient()               # create client object
    # network timeout in seconds (floats allowed), default: None
    client.timeout = 10
    # timeout for fetching the result of the idle command is handled seperately, default: None
    client.idletimeout = None
    client.connect("192.168.0.100", 6600)  # connect to localhost:6600

    def on_activate_shift_caps():
         client.pause()  # play/pause

    def on_activate_exit():
        raise MyException()

    def on_activate_vol_up():
        client.volume(+VOL_INC)

    def on_activate_vol_down():
        client.volume(-VOL_INC)

    def on_activate_prev():
        client.previous();

    def on_activate_next():
        client.next();

    with keyboard.GlobalHotKeys({
            #todo read hotkeys from file
            '<alt>+<shift>+1': on_activate_vol_down,
            '<alt>+<shift>+2': on_activate_vol_up,
            '<alt>+<shift>+q': on_activate_prev,
            '<alt>+<shift>+w': on_activate_next,
            '<shift>+<caps_lock>': on_activate_shift_caps,
            '<esc>': on_activate_exit}) as idk:
        try:
            idk.join()
        except MyException as e:
            print('Exit button pressed')
            client.close()                     # send the close command
            client.disconnect()                # disconnect from the server


if __name__ == "__main__":
    main()

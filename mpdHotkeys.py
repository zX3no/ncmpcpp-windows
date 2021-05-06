from mpd import MPDClient
from contextlib import contextmanager
import sys

from pynput import keyboard

def main():

    class MyException(Exception): pass

    VOL_INC = 5
    HOST, PORT = '192.168.0.100', 6600
    client = MPDClient()  
   
    @contextmanager
    def connection():
        try:
            client.connect(HOST, PORT)
            yield
        finally:
            client.close()
            client.disconnect()

    def queue(command):
        with connection():
            try:
                if command == 'vol_down':
                    client.volume(-VOL_INC)
                elif command == 'vol_up':
                    client.volume(+VOL_INC)
                else:
                    result = getattr(client, command)()
            except mpd.CommandError:
                return 'invalid command'

        return 'queued'

    def on_activate_shift_caps():
         queue('pause')

    def on_activate_exit():
        raise MyException()

    def on_activate_vol_up():
        queue('vol_up')

    def on_activate_vol_down():
        queue('vol_down')

    def on_activate_prev():
        queue('previous')

    def on_activate_next():
        queue('next')

    with keyboard.GlobalHotKeys({
            #todo read hotkeys from file
            '<alt>+<shift>+1': on_activate_vol_down,
            '<alt>+<shift>+2': on_activate_vol_up,
            '<alt>+<shift>+q': on_activate_prev,
            '<alt>+<shift>+w': on_activate_next,
            '<shift>+<caps_lock>': on_activate_shift_caps,
            '<shift>+<caps_lock>': on_activate_shift_caps}) as idk:
            #'<esc>': on_activate_exit}) as idk:
        try:
            idk.join()
        except MyException as e:
            print('Exit button pressed')
            client.close()                     # send the close command
            client.disconnect()                # disconnect from the server


if __name__ == "__main__":
    main()

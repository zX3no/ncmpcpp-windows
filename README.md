# Ncmpcpp on Windows

## Setting up MPD

1. Download the latest version of `mpd.exe` from https://www.musicpd.org/download/win32/.
2. Create a folder called `mpd` and add `mpd.exe` to it. I used `C:/mpd`, replace all occurrences with your directory location.
3. Create a folder inside `mpd` called `playlists`.
4. Create a file called `mpd.conf` and open it.
5. Copy the contents inside
    ```
    bind_to_address "your_ip_adress"
    port "6600"

    music_directory "C:/replace_with_my_music_directory"
    log_file "C:/mpd/mpd.log"
    db_file "C:/mpd/mpd.db"
    playlist_directory "C:/mpd/playlists"
    state_file "C:/mpd/mpdstate"
    pid_file "C:/mpd/mpd.pid"

    audio_output {
        type "winmm"
        name "replace_with_any_name"
        mixer_type "software"
        device "replace_with_device_name"
    }
    ```
    Replace all `directories` with your own.

    Edit `bind_to_address` to your **local ip** eg. `"192.168.0.123"`. Don't use **127.0.0.1**!

    Edit `name` to anything your want.

    Edit `device` name with one of these two ways:

    1. In the windows 10 sound settings. Under `Output - Choose your output device`. Copy the text circled in red to `device`.
   
        ![](https://github.com/zX3no/zX3no/blob/main/Writing/Images/device.png?raw=true)

    2. Press Win+R. Type dxdiag. Click the **sound** tab and copy the device name into `device`.
6. Open cmd or PowerShell there and run `cd C:\mpd`.
7. Then run MPD with: 
   
    PS: `./mpd mpd.conf`

    CMD: `mpd mpd.conf`
8. You're now running a MPD server.
9.  Your folder structure should look like:
    ```
    mpd
    |   mpd.conf
    │   mpd.db
    |   mpd.exe
    |   mpd.log
    |   mpdstate
    |
    └───playlists
    ```
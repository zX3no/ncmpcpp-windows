# Ncmpcpp on Windows

## Table of contents
1. [MPD](#mpd)
2. [ncmpcpp](#ncmpcpp)
3. [Global hotkeys](#hotkeys)
## Setting up MPD <a name="mpd"></a>
1. Install [Chocolatey:](https://chocolatey.org/install)
2. Open a terminal and run: `choco install mpd`
3. Create a folder called `mpd`. I used `C:/mpd` as my directory. Remember to replace all occurrences of my directory with your own.
4. Create a folder inside `mpd` called `playlists`.
5. Create a file called `mpd.conf` and open it.
6. Copy the contents inside
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
   
        ![](https://github.com/zX3no/ncmpcppOnWindows/blob/main/Images/device.png?raw=true)

    2. Press Win+R. Type dxdiag. Click the **sound** tab and copy the device name into `device`.
7. In terminal run `cd C:\mpd`.
8. Then run MPD with: `mpd mpd.conf`
9. MPD is now running. You'll get a couple of errors; ignore these.
10. Your folder structure should look like:
    ```
    mpd
    |   mpd.conf
    │   mpd.db
    |   mpd.log
    |   mpdstate
    |
    └───playlists
    ```
11. To automatically run mpd at boot, create a service:
    ``` 
    sc create mpd binpath="mpd.exe c:\mpd\mpd.conf" 
    sc config mpd start=delayed-auto
    ```

## Setting up ncmpcpp <a name="ncmpcpp"></a>

1. You cannot run ncmpcpp natively on windows so you'll need to use Windows Subsystem for Linux. [You can install it here.](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

    I used Ubuntu for this example. 
2. `sudo apt install ncmpcpp`
3. `mkdir -p ~/.ncmcpp/lyrics`
4. `nano ~/.ncmpcpp/config`
5. Paste the following config. Make sure to change **mpd_host** and **mpd_music_dir**.

    On linux, the **C:/** drive can be accessed with: **/mnt/c/**
   
 ```
# https://github.com/ncmpcpp/ncmpcpp/blob/master/doc/config
# http://manpages.ubuntu.com/manpages/trusty/man1/ncmpcpp.1.html

### MPD ###
mpd_host = "LOCAL_IP_HERE"
mpd_port = 6600 
mpd_connection_timeout = 5

### Directories ###
mpd_music_dir = "/mnt/c/replace/with/my/music/directory"  
lyrics_directory  = ~/.ncmpcpp/lyrics
ncmpcpp_directory  = ~/.ncmpcpp

### Library View ###
media_library_primary_tag = album_artist

### Playlist View ###
user_interface = alternative

## Header ##

# Left
statusbar_time_color = blue   
player_state_color = cyan 

display_bitrate = yes

# Middle
header_window_color = cyan
# Controls color of browse, media library etc..
main_window_color = cyan
alternative_ui_separator_color = cyan

alternative_header_first_line_format = $0$aqqu$/a {$7%A - $9}{$5%t$9}|{$8%f$9} $0$atqq$/a$9
alternative_header_second_line_format = {$6%b$9}

# Right
state_flags_color = cyan
volume_color = blue 

## Body ##
song_columns_list_format = (5)[blue]{l} (30)[green]{A} (30)[magenta]{b} (50)[yellow]{t}
playlist_display_mode = columns
playlist_disable_highlight_delay = 0 
selected_item_prefix = "* "
current_item_prefix = $(blue)$r

## Footer ##
statusbar_color = red

### Navigation ###
cyclic_scrolling = yes
jump_to_now_playing_song_at_start = yes

### Progressbar ###
progressbar_look = "=>-"
progressbar_color = cyan
progressbar_elapsed_color = white
now_playing_prefix = "> "
seek_time = 1


### Misc ###
ignore_leading_the = yes
empty_tag_marker = ""
centered_cursor = yes
regular_expressions = extended
default_place_to_search_in = database
mouse_support = yes
colors_enabled = yes

### Console Title ###
# If enabled, ncmpcpp will override current window title with its own one.
enable_window_title = yes

### Editor ###
external_editor = nano
use_console_editor = yes
```
6. Then type: `ncmpcpp`
7. Press `u` to update the music directory

Ncmpcpp should now be working. 

[If you want to learn the default shortcuts.](https://pkgbuild.com/~jelle/ncmpcpp/)

[If you want to change how the players looks or works.](https://github.com/ncmpcpp/ncmpcpp/blob/master/doc/config)

[If you would like to change keyboard shortcuts.](https://github.com/ncmpcpp/ncmpcpp/blob/master/doc/bindings)

## Global hotkeys <a name="hotkeys"></a>
Requirements: `choco install python` and `pip install python-mpd2 pynput`

If you want to pause, play, skip playback by using keyboard shortcuts you download my python script [here.](https://github.com/zX3no/ncmpcppOnWindows/blob/main/mpdHotkeys.py) And edit it to your preferred key bindings.

For information on what keys are avaliable etc. Refer to the [pynput docs.](https://pynput.readthedocs.io/en/latest/keyboard.html#global-hotkeys)

If you want to run this script at startup, create a shorcut with the target as: `C:\Python39\pythonw.exe C:\mpd\mpdHotkeys.py`. Put the shortcut in `C:\Users\username\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`.

You can get to this location easily using run: `shell:startup`
# Ncmpcpp on Windows

## Table of contents
1. [MPD](#mpd)
2. [ncmpcpp](#ncmpcpp)

## Setting up MPD <a name="mpd"></a>
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
   
        ![](https://github.com/zX3no/ncmpcppOnWindows/blob/main/Images/device.png?raw=true)

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
## Setting up ncmpcpp <a name="ncmpcpp"></a>

1. You cannot run ncmpcpp natively on windows so you'll need to use Windows Subsystem for Linux. [You can install it here.](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
2. `sudo apt install ncmpcpp` or `sudo pacman -S ncmpcpp --noconfirm`
3. `mkdir -p ~/.ncmcpp/lyrics`
4. `nano ~/.ncmpcpp/config`
5. Paste the following config. Make sure to change **mpd_host** and **mpd_music_dir**.
 ```   
# Files
mpd_music_dir = "/mnt/c/replace_with_my_music_director"  
mpd_host = "LOCAL_IP_HERE"
mpd_port = "6600"
lyrics_directory  = ~/.ncmpcpp/lyrics
ncmpcpp_directory  = ~/.ncmpcpp
mpd_connection_timeout = "5"  
mpd_crossfade_time = "5"  
 
# Library
media_library_primary_tag = album_artist
 
# Playlist
playlist_disable_highlight_delay = "0"  
playlist_display_mode = "columns"  
playlist_show_remaining_time = "yes"

browser_display_mode = "columns"  
autocenter_mode = "yes"
song_columns_list_format = "(10)[blue]{l} (30)[green]{a} (30)[magenta]{b} (50)[yellow]{t}"  
colors_enabled = "yes"  
main_window_color = "white"  
main_window_highlight_color =  "blue"
header_window_color = "cyan"  
volume_color = "red"  
progressbar_color = "cyan"  
statusbar_color = "white"  
active_column_color = "cyan"  
active_window_border = "blue"

alternative_header_first_line_format = "$0$aqqu$/a {$7%a - $9}{$5%t$9}|{$8%f$9} $0$atqq$/a$9"
alternative_header_second_line_format = "{{$6%b$9}{ [$6%y$9]}}|{%D}"
song_list_format = "{$3%n │ $9}{$7%a - $9}{$5%t$9}|{$8%f$9}$R{$6 │ %b$9}{$3 │ %l$9}"
user_interface = "alternative"
#user_interface =                    "classic"
default_place_to_search_in = "database"


## Navigation ##
cyclic_scrolling = "yes"
header_text_scrolling = "yes"
jump_to_now_playing_song_at_start = "yes"
lines_scrolled = "2"

## Other ##
system_encoding = "utf-8"
regular_expressions = "extended"

## Selected tracks ##
selected_item_prefix = "* "
discard_colors_if_item_is_selected = "no"

## Seeking ##
incremental_seeking = "yes"
seek_time = "1"

## Visibility ##
header_visibility = "yes"
statusbar_visibility = "yes"
titles_visibility = "yes"


progressbar_look =  "=>-"
progressbar_boldness = "yes"
progressbar_elapsed_color = "white"

now_playing_prefix = "> "
song_status_format = " $2%a $4⟫$3⟫ $8%t $4⟫$3⟫ $5%b "
centered_cursor = "yes"

# Misc
display_bitrate = "yes"
# enable_window_title = "no"
follow_now_playing_lyrics = "yes"
ignore_leading_the = "yes"
empty_tag_marker = ""
```
6. Then type: `ncmpcpp`
7. Press `u` to update the music directory

Ncmpcpp should now be working. 

[If you want to learn the default shortcuts.](https://pkgbuild.com/~jelle/ncmpcpp/)

[If you want to change how the players looks or works.](https://github.com/ncmpcpp/ncmpcpp/blob/master/doc/config)

[If you would like to change keyboard shortcuts.](https://github.com/ncmpcpp/ncmpcpp/blob/master/doc/bindings)

### *TODO // Clean up config // Tutorial on remapping keys // Making global shortcuts with python*
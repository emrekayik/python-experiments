# Merry

A simplistic GUI interface for managing Python modules.

# How it works
The script will query pip, format the response in to a list, and output it in to the GUI.
From here, you can browse the list, select the module you want, and at the press of a button, either update or uninstall.
The script also supports printing out your installed modules and allowing you to uninstall modules like that.
Merry also supports installing modules, pressing Install opens up a little box where you can enter in the module you want to downlod from pip.

# Known issues
The GUI looks like it hangs when its doing the updating/background stuff, everything is still working fine, but it will look frozen.

# Planned features
Adding more pip commands support.

Version Pinning/Locking.

Installing from Git support. (Unsure if this works at all, it might already)

Multi-selecting modules in the listbox.

Icons!

Fancier GUI.

Virtualenv support. (Currently this works if you run the GUI while sourced in to a virtualenv already)


# Misc info
Tested to work on Python 3.7, probably will not work on earlier versions.
You can easily edit config.json to change how a few things work.

`pip_command` is the command the script will use, by default this is `pip3`

`auto_update_check` will decide if the script should auto-check for updates on startup. (currently not recommended) Defaults `false`.

`add_user_flag` decides if the script should install modules to your user or globally, example: the difference between pip3 install requests --user or just pip3 install requests.

Icon created by https://www.deviantart.com/lustriouscharming
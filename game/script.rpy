﻿# The script of the game goes in this file.

init:
    $ config.keymap['rollback'].remove('mousedown_4')
    $ config.keymap['rollforward'].remove('mousedown_5')

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    show screen new_screen

    " "

    # This ends the game.

    return

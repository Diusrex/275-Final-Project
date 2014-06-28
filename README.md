Morgan Redshaw
    
The origional goal of this project was to create 4 minigames, but that goal was later deemed to not be technical enough, so instead I have created an AI for Novem Tic Tac Toe and have left in the two other games I created (ong and Tetris).
    All of the games are working, but they are not meant to be pretty

Most of the games have their own readme file, which will contain information related to that game only.

For these games to work, you must have pygame installed.

Changing the screenSize:
    If you need to change the screenSize, I cannot guarentee how the screen will look.
        Many of the drawing functions are designed to be able to handle a different size, but some of them are not.
        If the screen's size is decreased by too much, there is a chance that parts of the program will be drawn outside of the screen (mostly for menus and such), or text will be drawn on other objects (mostly in the games themselves)

To exit out of all of the games, press escape or hit the exit button.

To run the complete program, run the file main.py in this directory with ipython3 (or however you run using pygame)

For the imports, the reason why all files simply include button is because all of the code for the button is the same.
    This is different than the other menus and such, which are all different and thus should not be shared.
    
    Furthermore, to increase the ease of running the games individually, the button code is simply common throughout the games

The reason why two of the games use a class for game, but the others don't is based on how much state information is needed by the different functions within game
    The called functions in pong need very limited state information, unlike the other games
    
    Also allows easy separation of initialization from running the game, but pong does not have very much to initialize before running
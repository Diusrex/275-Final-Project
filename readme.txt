Morgan Redshaw and Alex Sampley
    
The origional goal of this project was to create 4 minigames, but that goal was later deemed to not be technical enough, so instead we have created an AI for Novem Tic Tac Toe (description is in it's readme, and in it's 'How to Play' section), and have left in the three other games we created (Minesweeper, Pong and Tetris).
    All of the games are working, but they are not meant to be pretty

For these games to work, you must have pygame installed.

Changing the screenSize:
    If you need to change the screenSize, I cannot guarentee how the screen will look.
        Many of the drawing functions are designed to be able to handle a different size, but some of them are not.
        If the screen's size is decreased by too much, there is a chance that parts of the program will be drawn outside of the screen (mostly for menus and such), or text will be drawn on other objects (mostly in the games themselves)

To run the complete program, run the file main.py in this directory with ipython3 (or however you run using pygame)
    The reason why all of the subdirectories use import directory.x as x is to make it eaiser to convert to running the game individually
    
To run an individual game, checkout the branch ____, and run the file main.py in the wanted games subdirectory.

For the imports, the reason why all files simply include button is because all of the code for the button is the same.
    This is different than the other menus and such, which are all different and thus should not be shared.
    
    Furthermore, to increase the ease of running the games individually, the code is simply common throughout the games
    
LWOTai is a command line program. You need to have Python installed on your system to use it. You can run it from a command line as follows: python lwotai.py The most important thing to know is that the program does not track the deck, cards, hands or use of Reserves. You have to do that either with the board game or on Vassal.
Set up the game as usual and pick the scenario and ideology. You will then be at the Command prompt. You can enter "?" to see the various commands. The most important are the "j" and "u" commands. When it is a player's turn, pick the card they will play and enter that command and the card number. For instance, it is the Jihadist turn at the beginning of the game. Turn over the top card of their hand and then enter j and that card number (e.g. j 22). The program will then tell you what the Jihadist did so you can update your map. It's the same with your plays using the u command. If more information is necessary the program will ask for it.

When you use a card for Ops you then use the command for the operation you want. For instance if you want to disrupt, you enter "disrupt" at the Command prompt. The program will then ask what it needs to know about the disrupt.

There are two timekeeping functions you have to remember to use. After each US Activity Phase, you must enter the "plot" command so that unblocked plots are handled. And at the end of a turn you must enter the "turn" command to handle all the end of turn activities.

At any time you can use the "status" command to get a printout of the entire board position. And you can use the "history" command to see everything that has happened in the game.

Thanks to Dave Horn for implementing the Save and Undo system.

1. A save game is created after every single command whether you want it or not. If someone screws up and closes the window, PC battery dies, crashes, whatever, no problem, load it up again and you will be asked if you want to load the suspended game.

2. Rollback files are created at the beginning of each turn. You can roll back to any previous turn using the 'roll' or 'rollback' command. You will be prompted to enter which turn you want to roll back to.

3. An undo file is created after every card played. The player can undo to the last card at any time (two exceptions) by typing 'undo'. Exceptions are when you load from a previously suspended game or after executing a rollback. The undo file is removed at that exact point to prevent the player from undoing themselves to some other game in the past!

Thanks to Peter Shaw for implementing the Adjust system and for a bunch of bug fixes and cleanup.



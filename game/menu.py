from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
import sys
from .game import Game

class Menu(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Set up a background color
        self.setBackgroundColor(0.2, 0.3, 0.4, 1)

        # Add title text
        title_text = OnscreenText(
            text="My Game",
            pos=(0, 0.5),
            scale=0.2,
            fg=(1, 1, 1, 1),
            shadow=(0, 0, 0, 0.5),
            parent=base.a2dTopCenter
        )

        # Add a "Start" button
        start_button = DirectButton(
            text=("Start", "Start", "Start", "Start"),
            scale=0.1,
            command=self.startGame,
            pos=(0, 0, -0.1),
            parent=base.a2dTopCenter
        )

        # Add an "Exit" button
        exit_button = DirectButton(
            text=("Exit", "Exit", "Exit", "Exit"),
            scale=0.1,
            command=self.exitGame,
            pos=(0, 0, -0.3),
            parent=base.a2dTopCenter
        )

    def startGame(self):
        self.destroy()  # Close the menu
        Game()    # Start the game

    def exitGame(self):
        sys.exit(1)

app = Menu()
app.run()

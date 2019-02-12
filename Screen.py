# Author: Diego Caraballo
# GitHub: https://github.com/DiegoCaraballo
# web: http://www.pythondiario.com

import os

class Screen:

    def __init__(self):
        self.countLike = 0
        self.countRetweet = 0
        self.countFollow = 0
        self.countUnFollow = 0

    def drawScreen(self, listKeywords):
        pass

    # Limpia la pantalla según el sistema operativo
    def clear(self):
        try:
            if os.name == "posix":
                os.system("clear")
            elif os.name == "ce" or os.name == "nt" or os.name == "dos":
                os.system("cls")
        except Exception as e:
            print(e)
            input("Press enter to continue")
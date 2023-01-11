from direct.showbase.ShowBase import ShowBase
from modules.generator import MapMennager
from pandac.PandaModules import WindowProperties 
from modules.colors import *
import modules.player as playerClass


ICON = "textures/wood.jpg"

class Game (ShowBase):
    def __init__(self):
        super().__init__(self)
        # self.model = loader.loadModel ('models/environment')
        # self.model.reparentTo (render)
        # self.model.setScale (0.1)
        # self.model.setPos (-2, 25, -3)
        self.set_background_color (LightBlue)
        windata = WindowProperties ()
        windata.setTitle ("0,6³-2•0,6²•0,8+0,6•0,8²-2•0,8³=-1")
        base.win.requestProperties (windata)
        base.camLens.setFov (90)
        self.mapmanager = MapMennager ()
        self.player = playerClass.Player ((0, 30, 10), self.mapmanager)

game = Game ()

def main ():
    game.run ()

if __name__ == "__main__":
    main ()
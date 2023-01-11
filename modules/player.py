from direct.showbase.ShowBase import ShowBase
#from modules.generator import MapMennager

class Player ():
    def __init__ (self, koordynaty, node2):
        self.node2 = node2
        self.player = loader.loadModel ("models/panda")
        self.player.setPos (koordynaty)
        self.player.setScale (0.1)
        self.player.reparentTo (render)
        self.osoba_1 = False
        #self.standart ()
        self.events ()

    def standart (self):
        base.disableMouse ()
        base.camera.reparentTo (self.player)
        base.camera.setPos ((0, 0, 2))
        base.camera.setH (180)
        self.osoba_1 = True

    def osoba_3 (self):
        base.enableMouse ()
        base.camera.reparentTo (render)
        self.player_pos = self.player.getPos ()
        base.mouseInterfaceNode.setPos ((-self.player_pos[0], -self.player_pos[1], -self.player_pos[2] - 2))
        self.osoba_1 = False

    def checkCamera (self):
        if self.osoba_1:
            self.standart ()
        else:
            self.osoba_3 ()

    def right (self):
        h = self.player.getH ()
        self.player.setH ((h + 3) % 360)

    def left (self):
        h = self.player.getH ()
        self.player.setH ((h - 3) % 360)

    def up (self):
        p = self.player.getP ()
        self.player.setP ((p + 3) % 360)

    def down (self):
        p = self.player.getP ()
        self.player.setP ((p - 3) % 360)

    def circle_left (self):
        r = self.player.getR ()
        self.player.setR ((r + 3) % 360)

    def circle_right (self):
        r = self.player.getR ()
        self.player.setR ((r - 3) % 360)

    # def stan_w_ruch (self, arg):
    #     x__ = round (self.player.getX ())
    #     y__ = round (self.player.getY ())
    #     z__ = round (self.player.getZ ())
        
    #     dx, dy = self.player.get_koordynaty (self, arg)
    #     return x__ + dx, y__ + dy, z__

    # def get_koordynaty (self, kut):
    #     if kut >= 0 and kut <= 20:
    #         return 0, -1

    # def get_stan (self, kut):
    #     pos = self.get_koordynaty (kut)
    #     self.player.setPos (pos)

    def wpered (self):
        h = self.player.getH ()
        r = self.player.getR ()
        p = self.player.getP ()
        x = self.player.getX ()
        y = self.player.getY ()
        z = self.player.getZ ()
        x += h / 360
        y += r / 360
        z += p / 360
        self.player.setPos (x, y, z)


    def events (self):
        base.accept ("f5", self.changeCamera)
        base.accept ("a", self.right)
        base.accept ("a" + "-repeat", self.right)
        base.accept ("d", self.left)
        base.accept ("d" + "-repeat", self.left)
        base.accept ("w", self.up)
        base.accept ("w" + "-repeat", self.up)
        base.accept ("s" + "-repeat", self.down)
        base.accept ("s", self.down)
        base.accept ("q", self.circle_left)
        base.accept ("q" + "-repeat", self.circle_left)
        base.accept ("e", self.circle_right)
        base.accept ("e" + "-repeat", self.circle_right)
        base.accept ("arrow_up", self.wpered)
        base.accept ("arrow_up" + "-repeat", self.wpered)



    def changeCamera (self):
        self.osoba_1 = not self.osoba_1
        self.checkCamera ()

# "escape", "f"+"1-12" (e.g. "f1","f2",..."f12"), "print_screen",
# "scroll_lock", "backspace", "insert", "home", "page_up", "num_lock",
# "tab",  "delete", "end", "page_down", "caps_lock", "enter", "arrow_left",
# "arrow_up", "arrow_down", "arrow_right", "shift", "lshift", "rshift",
# "control", "alt", "lcontrol", "lalt", "space", "ralt", "rcontrol"
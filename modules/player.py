from direct.showbase.ShowBase import ShowBase
#from modules.generator import MapMennager
from panda3d.core import TextNode
from direct.gui.OnscreenText import OnscreenText
from direct.task.Task import Task


class Title (OnscreenText):
    def change_text (self, text):
        self.text = text

class Player ():
    def __init__ (self, koordynaty, node2):
        self.node2 = node2
        self.player = loader.loadModel ("models/panda")
        self.player.setPos (koordynaty)
        self.player.setScale (0.15)
        self.player.reparentTo (render)
        self.standartH = 0
        self.osoba_1 = False
        #self.standart ()
        self.events ()
        h, p, r, x, y, z = self.get_wse ()
        x2, y2, z2, h2, p2, r2 = self.gwzk ()
        self.title = \
            Title (text = f"H = {str(h)}\nP = {str(p)}\nR = {str(r)}\n\n\nX = {str(x)}\nY = {str(y)}\nZ = {str(z)}.",
                            parent = base.a2dBottomRight, align = TextNode.ARight,
                        fg = (0, 0, 0, 1), pos = (-2.45, 1.9), scale = .045,
                        shadow = (1, 1, 1, 0.5))
        self.title2 = Title (text = f"Camera:\nX = {str(int(round (x2, 0)))}\nY = {str(int(round (y2, 0)))}\nZ = {str(int(round (z2, 0)))}\n\n\nH = {str(int(round (h2, 0)))}\nP = {str(int(round (p2, 0)))}\nR = {str(int(round (r2, 0)))}\nclick Esc to update.", 
            parent = base.a2dBottomRight, align = TextNode.ARight,
            fg = (0, 0, 0, 1), pos = (-.15, 1.9), scale = .045,
            shadow = (1, 1, 1, 0.5))
        taskMgr.add(self.turnHead, "camera-task")

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
            #self.grawitaciia ()
        else:
            self.osoba_3 ()
            #self.bez_grawitaciji ()

    def get_wse (self):
        x, y, z = self.player.getPos ()
        h = self.player.getH ()
        p = self.player.getP ()
        r = self.player.getR ()
        return h, p, r, x, y, z

    def gwzk (self):
        x, y, z = base.camera.getPos ()
        h, p, r = base.camera.getHpr ()
        return x, y, z, h, p, r

    def left (self):
        r = self.player.getR ()
        if r >= 342 or r < 18:
            self.player.setR ((r + 3) % 360)
        h, p, r, x, y, z = self.get_wse ()
        self.title.change_text (text = f"H = {str(h)}\nP = {str(p)}\nR = {str(r)}\n\n\nX = {str(x)}\nY = {str(y)}\nZ = {str(z)}.")

    def right (self):
        r = self.player.getR ()
        if r <= 18 or r > 342:
            self.player.setR ((r - 3) % 360)
        h, p, r, x, y, z = self.get_wse ()
        self.title.change_text (text = f"H = {str(h)}\nP = {str(p)}\nR = {str(r)}\n\n\nX = {str(x)}\nY = {str(y)}\nZ = {str(z)}.")


    def forward (self):
        kut = (self.player.getH () + 0) % 360
        self.grawitaciia (kut)
        h, p, r, x, y, z = self.get_wse ()
        self.title.change_text (text = f"H = {str(h)}\nP = {str(p)}\nR = {str(r)}\n\n\nX = {str(x)}\nY = {str(y)}\nZ = {str(z)}.")


    def back (self):
        kut = (self.player.getH () + 180) % 360
        self.grawitaciia (kut)
        h, p, r, x, y, z = self.get_wse ()
        self.title.change_text (text = f"H = {str(h)}\nP = {str(p)}\nR = {str(r)}\n\n\nX = {str(x)}\nY = {str(y)}\nZ = {str(z)}.")


    def go_right (self):
        kut = (self.player.getH () + 270) % 360
        self.grawitaciia (kut)
        h, p, r, x, y, z = self.get_wse ()
        self.title.change_text (text = f"H = {str(h)}\nP = {str(p)}\nR = {str(r)}\n\n\nX = {str(x)}\nY = {str(y)}\nZ = {str(z)}.")


    def go_left (self):
        kut = (self.player.getH () + 90) % 360
        self.grawitaciia (kut)
        h, p, r, x, y, z = self.get_wse ()
        self.title.change_text (text = f"H = {str(h)}\nP = {str(p)}\nR = {str(r)}\n\n\nX = {str(x)}\nY = {str(y)}\nZ = {str(z)}.")


    def get_kut (self, kut):
        h = self.player.getH ()
        p = self.player.getP ()
        from_x, from_y, from_z = round (self.player.getPos ())

        dx, dy = self.difkut (kut)

        return from_x + dx, from_y + dy, from_z

    def grawitaciia (self, kut):
        pos = self.get_kut (kut)
        self.player.setPos (pos)


    def bez_grawitaciji (self): pass

    def difkut (self, kut):
        if kut >= 0 or kut <= 20 or kut >= 355 and kut <= 360:
            return 0, -1
        elif kut >= 20 and kut <= 65:
            return 1, -1
        elif kut >= 65 and kut < 110:
            return 1, 0
        elif kut >= 110 and kut < 155:
            return 1, 1
        elif kut >= 155 and kut < 200:
            return 0, 1
        elif kut >= 200 and kut < 245:
            return -1, 1
        elif kut >= 245 and kut < 290:
            return -1, 0
        elif kut >= 290 and kut < 335:
            return -1, -1

    def esc (self):
        x, y, z, h, p, r = self.gwzk ()
        self.title2.change_text (text = f"Camera:\nX = {str(int(round (x, 0)))}\nY = {str(int(round (y, 0)))}\nZ = {str(int(round (z, 0)))}\n\n\nH = {str(int(round (h, 0)))}\nP = {str(int(round (p, 0)))}\nR = {str(int(round (r, 0)))}\nclick Esc to update.")

    def events (self):
        base.accept ("f5", self.changeCamera)
        base.accept ("a", self.left)
        base.accept ("a" + "-repeat", self.left)
        base.accept ("d", self.right)
        base.accept ("d" + "-repeat", self.right)
        base.accept ("arrow_up", self.forward)
        base.accept ("arrow_up" + "-repeat", self.forward)
        base.accept ("arrow_down", self.back)
        base.accept ("arrow_down" + "-repeat", self.back)
        base.accept ("arrow_left", self.go_left)
        base.accept ("arrow_left" + "-repeat", self.go_left)
        base.accept ("arrow_right", self.go_right)
        base.accept ("arrow_right" + "-repeat", self.go_right)
        base.accept ("escape", self.esc)



    def changeCamera (self):
        self.osoba_1 = not self.osoba_1
        self.checkCamera ()
        

# "escape", "f"+"1-12" (e.g. "f1","f2",..."f12"), "print_screen",
# "scroll_lock", "backspace", "insert", "home", "page_up", "num_lock",
# "tab",  "delete", "end", "page_down", "caps_lock", "enter", "arrow_left",
# "arrow_up", "arrow_down", "arrow_right", "shift", "lshift", "rshift",
# "control", "alt", "lcontrol", "lalt", "space", "ralt", "rcontrol"

    def turnHead(self, task):
        if base.mouseWatcherNode.hasMouse():
            mpos = base.mouseWatcherNode.getMouse ()
            # significant tearing would be visable
            sh = round (-(mpos.getX () * 180), 0)
            self.player.setH ((self.standartH + sh) % 360)
            self.player.setP (round ((-(mpos.getY () * 45) % 360), 0))
            h, p, r, x, y, z = self.get_wse ()
            self.title.change_text (text = f"H = {str(h)}\nP = {str(p)}\nR = {str(r)}\n\n\nX = {str(x)}\nY = {str(y)}\nZ = {str(z)}.")
            if mpos.getX () <= -.7:
                self.standartH += 1
                self.standartH = self.standartH % 360
            if mpos.getX () >= .7:
                self.standartH += -1
                self.standartH = self.standartH % 360

        return Task.cont
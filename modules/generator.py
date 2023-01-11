class MapMennager ():
    def __init__ (self):
        self.model = "eggs/block.egg"
        self.texture = ("textures/stone.jfif",
            "textures/bricks.jpg",
            "textures/earth.png",
            "textures/earth.png",
            "textures/earth.png",
            "textures/earth.png",
            "textures/earth.png",
            "textures/earth.png",
            "textures/earth.png",
            "textures/earth.png",
            "textures/earth.png",
            "textures/earth.png",
            "textures/earth.png")
        self.new ()
        self.create ("map/map.txt")
        
    def addBlock (self, pos, texture):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(texture)) 
        self.block.setPos(pos)
        #self.block.setColor(self.color)
        self.block.reparentTo (self.node2)

    def new (self):
        self.node2 = render.attachNewNode ("Node2")
    
    def create (self, dir):
        with open (dir, "r", encoding = "utf-8") as f:
            y = 0
            for lineb in f:
                element = lineb.split (" ")
                element = element[0:-1]
                for i in element:
                    x = 0
                    for z in range (int(i)):
                        self.addBlock ((x, y, z), texture = self.texture[z])
                        x += 1
                    y += 1
                print (element)
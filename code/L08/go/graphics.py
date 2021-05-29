from constant import *
from graphics_lib import *
from graphics_lib import Canvas as Canvas_

####################################################################
class Canvas:
    def __init__(self):
        margin = 10
        self.height = N*SQ_SIZE + 2*margin
        self.width = self.height # * 3 / 2
        self.canvas = Canvas_(self.width, self.height, (220,179,92), "mini-Go")
        self.layerBoard = Layer()
        # draw board
        self.xOffset = self.yOffset = SQ_SIZE//2 + margin
        for row in range(N):
            y = row*SQ_SIZE + self.yOffset
            p = Path(Point(self.xOffset,y), Point(self.xOffset+SQ_SIZE*(N-1),y))
            p.setBorderColor("black")
            p.setBorderWidth(2)
            p.setDepth(50) 
            self.layerBoard.add(p)
        for col in range(N):
            x = col*SQ_SIZE + self.xOffset
            p = Path(Point(x,self.yOffset), Point(x,self.yOffset+SQ_SIZE*(N-1)))
            p.setBorderColor("black")
            p.setBorderWidth(2)
            p.setDepth(50) 
            self.layerBoard.add(p)

        self.stone = [[None]*N  for i in range(N)]
        self.num_turn = [[None]*N  for i in range(N)]
        self.empty = [[True]*N  for i in range(N)]
        for i in range(N):
            for j in range(N):
                pos = Point(self.xOffset+j*SQ_SIZE, self.yOffset+i*SQ_SIZE)
                self.num_turn[i][j] = Text("", 18, pos)
                self.num_turn[i][j].setDepth(40)
                self.stone[i][j] = Circle(SQ_SIZE*2//5, pos)
                self.stone[i][j].setBorderWidth(1)
                self.stone[i][j].setDepth(45)
                    
        """
        for row in [3,9,15]:
            for col in [3,9,15]:
                pos = Point(self.xOffset+col*SQ_SIZE, self.yOffset+row*SQ_SIZE)
                circle = Circle(SQ_SIZE//10, pos)
                circle.setBorderWidth(1)
                circle.setBorderColor("black")
                circle.setFillColor("black")
                circle.setDepth(49) 
                self.layerBoard.add(circle)
                
        # prepare Text object for displaying message
        textSize = SQ_SIZE // 2
        pos1 = Point(self.width*0.74, self.height*0.05)
        pos2 = Point(self.width*0.85, self.height*0.05)
        pos3 = Point(self.width*0.74, self.height*0.11)
        pos4 = Point(self.width*0.79, self.height*0.11)
        pos5 = Point(self.width*0.79, self.height*0.20)
        pos6 = Point(self.width*0.74, self.height*0.29)
        pos7 = Point(self.width*0.85, self.height*0.29)
        pos8 = Point(self.width*0.74, self.height*0.35)
        pos9 = Point(self.width*0.79, self.height*0.35)
        pos10 = Point(self.width*0.74, self.height*0.50)
        pos11 = Point(self.width*0.81, self.height*0.50)
        pos12 = Point(self.width*0.83, self.height*0.70)
        pos13 = Point(self.width*0.83, self.height*0.97)
        #
        self.titleBlack = Text("Black:", textSize, pos1)
        self.titleBlack.setDepth(48)
        self.layerBoard.add(self.titleBlack)
        self.nameBlack = Text("Ryan", textSize, pos2)
        self.nameBlack.setDepth(48)
        self.layerBoard.add(self.nameBlack)
        self.scoreTitleBlack = Text("Score:", textSize, pos3)
        self.scoreTitleBlack.setDepth(48)
        self.layerBoard.add(self.scoreTitleBlack)
        self.scoreBlack = Text("0", textSize, pos4)
        self.scoreBlack.setDepth(48)
        self.layerBoard.add(self.scoreBlack)
        #
        self.vs = Text("VS", textSize, pos5)
        self.vs.setDepth(48)
        self.layerBoard.add(self.vs)
        # 
        self.titleWhite = Text("White:", textSize, pos6)
        self.titleWhite.setDepth(48)
        self.layerBoard.add(self.titleWhite)
        self.nameWhite = Text("Kakashi", textSize, pos7)
        self.nameWhite.setDepth(48)
        self.layerBoard.add(self.nameWhite)
        self.scoreTitleWhite = Text("Score:", textSize, pos8)
        self.scoreTitleWhite.setDepth(48)
        self.layerBoard.add(self.scoreTitleWhite)
        self.scoreWhite = Text("0", textSize, pos9)
        self.scoreWhite.setDepth(48)
        self.layerBoard.add(self.scoreWhite)
        # 
        self.turnTitle = Text("# Turns:", textSize, pos10)
        self.turnTitle.setDepth(48)
        self.layerBoard.add(self.turnTitle)
        self.turn = Text("0", textSize, pos11)
        self.turn.setDepth(48)
        self.layerBoard.add(self.turn)
        #
        self.msg = Text("Time out", textSize, pos12)
        self.msg.setDepth(48)
        self.layerBoard.add(self.msg)
        #
        self.copyright = Text("Copyright (c) 2017 by Hatake Kakashi", textSize*6//10, pos13)
        self.copyright.setDepth(48)
        self.layerBoard.add(self.copyright)
        """
        self.canvas.add(self.layerBoard)

    def setName(self, name, player):
        if len(name) > 10: name = name[0:10]
        if player == BLACK: self.nameBlack.setMessage(name)
        elif player == WHITE: self.nameWhite.setMessage(name)
        else: assert False

    def setScore(self, score, player):
        if player == BLACK: self.scoreBlack.setMessage(str(score))
        elif player == WHITE: self.scoreWhite.setMessage(str(score))
        else: assert False

    def setTurn(self, turn):
        assert 1 <= N*N*2 <= 100
        self.turn.setMessage(str(turn))

    def addStone(self, row, col, player, nTurn):
        assert (0<=row<N and 0<=col<N)
        assert self.empty[row][col]
        self.empty[row][col] = False
        self.stone[row][col].setBorderColor(["black","white"][player])
        self.stone[row][col].setFillColor(["black","white"][player])
        self.canvas.add(self.stone[row][col])
        self.num_turn[row][col].setMessage(str(nTurn))
        self.num_turn[row][col].setFontColor(["white","black"][player])
        self.canvas.add(self.num_turn[row][col])
        
    def removeStone(self, row, col):
        assert not self.empty[row][col]
        self.empty[row][col] = True
        self.canvas.remove(self.stone[row][col])
        self.canvas.remove(self.num_turn[row][col])
        
    def setMessage(self, s):
        #self.msg.setMessage(s)
        print (s)
    def clearMessage(self):
        #self.msg.setMessage("")
        pass

    def waitInput(self):
        while True:
            event = self.canvas.wait()
            d = event.getDescription()
            if d == "canvas close":
                return d
            if d == "mouse click":
                p = self.canvas.getMouseCoordinates()
                x = p.getX()
                y = p.getY()
                #
                i = int(float(y - self.yOffset)/SQ_SIZE + 0.5)
                j = int(float(x - self.xOffset)/SQ_SIZE + 0.5)
                if 0 <= i < N and 0 <= j < N:
                    return (i,j)

    def clear(self):
        for i in range(N):
            for j in range(N):
                if not self.empty[i][j]:
                    self.removeStone(i,j)
        self.setMessage("")
        
####################################################################
"""
import tkinter as tk
import tkFont
class Canvas:
    def __init__(self):
        sqWidth = 50
        margin = 10
        self.width = N*sqWidth + 2*margin
        self.height = self.width
        bg_rgb = "#%02x%02x%02x" % (220,179,92)
        self.canvas = tk.Canvas(width=self.width, height=self.height, bg=bg_rgb)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)
        fontBW = tkFont.Font(family="Helvetica", size=80) #, weight="bold")
        self.B = [[None]*N  for i in range(N)]
        self.W = [[None]*N  for i in range(N)]
        radius = sqWidth*2//5  # stone's radius
        for i in range(N):
            for j in range(N):
                y, x = margin+i*sqWidth+sqWidth//2, margin+j*sqWidth+sqWidth//2
                if i<N-1 and j<N-1:
                    self.canvas.create_rectangle(x, y, x+sqWidth, y+sqWidth, width=2)
                x0,y0,x1,y1 = x-radius,y-radius,x+radius,y+radius
                self.B[i][j] = self.canvas.create_oval(x0,y0,x1,y1,fill="black",state=tk.HIDDEN, width=0)
                self.W[i][j] = self.canvas.create_oval(x0,y0,x1,y1,fill="white",state=tk.HIDDEN, width=0)
        self.canvas.update()
        
    def addBW(self, player, row, col):
        if player == B:
            self.canvas.itemconfig(self.B[row][col], state=tk.NORMAL)
        elif player == W:
            self.canvas.itemconfig(self.W[row][col], state=tk.NORMAL)
        else: # captured
            self.canvas.itemconfig(self.B[row][col], state=tk.HIDDEN)
            self.canvas.itemconfig(self.W[row][col], state=tk.HIDDEN)
        self.canvas.update()

    def close(self): self.canvas.destroy()

    #def mouse_callback(self, event): print ("clicked at", event.x, event.y)
    #def waitInput(self): pass
    
    def setMessage(self, s):
        x = self.width//2
        y = self.height//2
        self.canvas.create_text(x, y, text=s, fill="red", \
                                font=tkFont.Font(family="Helvetica", size=30))
        self.canvas.update()
        time.sleep(3)
"""

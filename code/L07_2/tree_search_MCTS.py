from board import *
import random
import math

##################################################################
class Node(object):  
    player = None  # root of the tree
    
    def __init__(self, board, turn):
        self.state = board
        self.turn = turn  # may not be Node.player
        self.action = board.validMoves(turn)
        
    def isLeaf(self):
        # should be extended to consider next turn by the opponent..
        return len(self.action) == 0

    def reward(self):
        return 1 if self.state.winner() == Node.player else -1
        
    def randomChild(self):
        move = random.choice(self.action)
        boardNext = self.state.boardAfterMove(self.turn, move)
        return Node(boardNext, opponent(self.turn))
    
##################################################################
class NodeMCTS(Node):
    created = dict() # key: hash value / val: board

    @classmethod
    def init(cls, player):
        Node.player = player
        cls.created.clear()
    
    # should be called by the class method create() only
    def __init__(self, board, parent=None, parentAction=None):
        if parent == None:  # root
            turn = Node.player
        else:
            turn = opponent(parent.turn)
        Node.__init__(self, board, turn)
        self._parent = parent
        self.parentAction = parentAction
        self.child = [None]*len(self.action)  # currently expanded children
        self.N = 0
        self.Q = 0

    @classmethod
    def create(cls, board, parent=None, parentAction=None):
        return NodeMCTS(board, parent, parentAction)
        """
        hashValue = board.hashValue()
        if hashValue in cls.created:
            return cls.created[hashValue]
        else:
            node = NodeMCTS(board, parent, parentAction)
            cls.created[hashValue] = node
            return node
        """
        
    def isRoot(self): return self._parent == None
    def parent(self): return self._parent
    
    def fullyExpanded(self): return (None not in self.child)

    def expand(self):
        n = len(self.action)
        L = []
        for i in range(n):
            if self.child[i] == None:
                L.append(i)
        i = random.choice(L)
        move = self.action[i]
        boardNext = self.state.boardAfterMove(self.turn, move)
        node = NodeMCTS.create(boardNext, self, move)
        self.child[i] = node
        return node

    def bestChild(self, c):
        best = None
        max = -10000000
        for node in self.child:
            if node == None: continue  # node that is not yet expanded
            assert node.N >= 1
            val = float(node.Q)/node.N + c*(math.log(self.N)/node.N)**0.5
            if max < val:
                best = node
                max = val
        return best, max
        
    def update(self, delta):
        self.N += 1
        self.Q += delta

##################################################################
class MCTS:
    def __init__(self, board, player, curDepth, maxDepth, canvas=None):
        #random.seed(0)  # make deterministic for DEBUG
        NodeMCTS.init(player)
        self.root = NodeMCTS.create(board)
        self.player = player
        self.curDepth = curDepth
        self.maxDepth = maxDepth
        self.canvas = canvas
        
    def run(self):
        for i in range(NUM_MC_TRIALS):
            v = self.treePolicy()
            delta = self.defaultPolicy(v)
            self.backup(v, delta)
        bestChild, maxVal = self.root.bestChild(0)
        return (maxVal, bestChild.parentAction)

    def treePolicy(self):
        v = self.root
        depth = self.curDepth
        while not v.isLeaf() and depth < self.maxDepth:
            depth += 1
            if not v.fullyExpanded():
                return v.expand()
            else:
                v, _ = v.bestChild(2)
        return v

    def defaultPolicy(self, v):  # later measure 
        depth = self.curDepth
        while not v.isLeaf() and depth < self.maxDepth:
            depth += 1
            v = v.randomChild()
        # print ("depth of MCTS:", depth)
        return v.reward()

    def backup(self, v, delta):
        while True:
            v.update(delta)
            if v.isRoot(): break
            v = v.parent()

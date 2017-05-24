from copy import deepcopy
from collections import deque
class Node:

    #initialize nodeCount
    #nodeCount is used as a space measurement for efficiency testing (used in init, makeChild)
	#nodeCount = 0

    def __init__(self, state, parent=None):
        # self.nodeCount = 0
        self.state = state
        self.parent = parent
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def expand(self, puzzle):
        return [self.makeChild(puzzle, action) for action in puzzle.getActions(self.state)]

    def makeChild(self, puzzle, action):
        #Node.nodeCount += 1
        childState = puzzle.applyAction(self.state, action)
        return Node(childState, self)

    def getState(self ):
        return self.state


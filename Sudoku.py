from copy import deepcopy
from SudokuHelper import findBox

class Problem(object):
    def __init__(self, initial, size,  rows, cols, goal=None):
        # These values are specific to the problem you are solving (i.e. sudoku, nQueens, ...)
        self.bCols = cols
        self.bRows = rows
        self.size = size
        self.initial = initial
        self.goal = goal

        # An action is the assignment of a single square
        # thus, the set of legal actions for all states is all numbers 1 to n
        self.actions = [i for i in range(1, self.size + 1)]

    def getActions(self, state):
        actionSet = set(self.actions)
        rowNum = 0
        for row in state:       #state is defined as a set of rows
            for col in range(self.size):
                if row[col] == 0:       #0 is syntax for a blank square
                    actionSet.difference_update(set(row))   #difference_update removes matches between two sets
                    actionSet.difference_update(set([r[col] for r in state]))
                    actionSet.difference_update(set(findBox(rowNum, col, self.bRows, self.bCols, state)))
                    return list(actionSet)
            rowNum += 1
        return self.actions

    #apply action to the first blank space discovered
    def applyAction(self, state, action):
        newState = deepcopy(state)
        for row in newState:
            for col in range(self.size):
                if row[col] == 0:
                    row[col] = action
                    return newState

    def isGoal(self, state):
        # If the state is empty, not done yet
        if not state:
            return False

        # If all rows have not yet been filled, not done yet
        if len(state) < self.size:
            return False
        for row in state:
            for col in range(self.size):
                if row[col] == 0:
                    return False

        # If we got this far, the board is complete and legal
        print('WINNER')
        for i in range(self.size):
            output = ''
            for j in range(self.size):
                output += '   ' + str(state[i][j])
            print(output)
        return True
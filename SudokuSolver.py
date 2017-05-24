from bfs import BFS
from dfs import DFS
from Sudoku import *
from SudokuHelper import makeBoxes

def solver(puzzle, r, c, n, search):
    prob = Problem(puzzle, n, r, c, None)
    if search == "BFS":
        end = BFS(prob)
    elif search == "DFS":
        end = DFS(prob)
    if end == None:
        print("error solution not found")
    else:
        makeBoxes(end, r, c)
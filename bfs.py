from collections import deque
from node import *

#BFS uses a queue to search the tree thus always viewing the tree row by row

def BFS(problem):
	# Generate the initial (root) node
	node = Node(problem.initial)

	# For efficiency, check if the node is a goal state BEFORE putting on the queue
	if problem.isGoal(node.getState()):
		return node.getState()

	# Start the frontier queue by adding the root
	frontier=deque()
	frontier.append(node)

	# Keep searching the tree until there is nothing left to explore (i.e. frontier is empty) OR a solution is found
	while len(frontier) > 0:
		node = frontier.popleft()
		for child in node.expand(problem):
			if problem.isGoal(child.getState()):
				return child.getState()
			frontier.append(child)
	return None


def makeBoxes( Alist, bRows, bCols ) :
	# Alist is list of lists of rows in nxn puzzle
	# brows, bcols are dimensions of inner box (e.g. 6x6 puzzle is made of 6 2x3 boxes, so makeBoxes(Alist,2,3)
	# This composes the inner boxes, numbering from top to bottom, left to right.
	# For example 6x6 = | box 0 | box 2 |
	#                   | box 1 | box 3 |

	puzzleSize = len(Alist)
	boxesAcrossCols = puzzleSize // bCols
	boxesDownRows = puzzleSize // bRows
	boxesTotal = boxesAcrossCols * boxesDownRows

	boxes = [ [] for b in range( boxesTotal )]
	for b in range( boxesTotal ):
		# Take all relevant column values from the bRows relevant to box "b"
		# For example, box 3 from above is composed of rows 2,3 and cols 2,3
		for row in range( b%boxesDownRows*bRows, b%boxesDownRows*bRows+bRows ):
			boxes[b].extend( Alist[row][b//boxesDownRows*bCols : b//boxesDownRows*bCols+bCols] )

	print('\nBOXES')
	for b in boxes : print(b)

def findBox(row, col, bRows, bCols, Alist):
    # Alist is list of rows(lists) in nxn puzzle
    # brows, bcols are dimensions of inner box (e.g. 6x6 puzzle is made of 6 2x3 boxes, so makeBoxes(x,y,2,3,Alist)
    # This composes the inner boxes, numbering from top to bottom, left to right.
    # For example 6x6 = | box 0 | box 2 |
    #                   | box 1 | box 3 |

    puzzleSize = len(Alist)
    boxesAcrossCols = puzzleSize // bCols
    boxesDownRows = puzzleSize // bRows
    boxesTotal = boxesAcrossCols * boxesDownRows
    boxes = [[] for b in range(boxesTotal)]

    boxFound = False
    for curBox in range(boxesTotal):
        # Take all relevant column values from the bRows relevant to box "b"
        # For example, box 3 from above is composed of rows 2,3 and cols 2,3
        for rows in range(curBox % boxesDownRows * bRows, curBox % boxesDownRows * bRows + bRows):
            boxes[curBox].extend(Alist[rows][curBox // boxesDownRows * bCols: curBox // boxesDownRows * bCols + bCols])
            if rows == row:
                if col in range (curBox // boxesDownRows * bCols, curBox // boxesDownRows * bCols + bCols):
                    boxFound = True
                    box = curBox
        if boxFound == True:
            return boxes[box]


# Test makeBoxes
def testMakeBoxes():
	A = [[1,2,1,2],
	[3,4,3,4],
	[1,2,1,2],
	[3,4,3,4]]

	B2 = [
		[ 1,2, 1,2, 1, 2 ],
		[ 3,4, 3,4, 3, 4 ],
		[ 5,6, 5,6, 5, 6 ],
		[ 1,2, 1,2, 1, 2 ],
		[ 3,4, 3,4, 3, 4 ],
		[ 5,6, 5,6, 5, 6 ] ]

	B = [[ 1, 2, 3, 1, 2, 3],
	[ 4, 5, 6, 4, 5, 6],
	[ 1, 2, 3, 1, 2, 3],
	[ 4, 5, 6, 4, 5, 6],
	[ 1, 2, 3, 1, 2, 3],
	[ 4, 5, 6, 4, 5, 6]]

	C = [[ 1, 2, 3, 1, 2, 3, 1, 2, 3 ],
	[ 4, 5, 6, 4, 5, 6, 4, 5, 6 ],
	[ 7, 8, 9, 7, 8, 9, 7, 8, 9 ],
	[ 1, 2, 3, 1, 2, 3, 1, 2, 3 ],
	[ 4, 5, 6, 4, 5, 6, 4, 5, 6 ],
	[ 7, 8, 9, 7, 8, 9, 7, 8, 9 ],
	[ 1, 2, 3, 1, 2, 3, 1, 2, 3 ],
	[ 4, 5, 6, 4, 5, 6, 4, 5, 6 ],
	[ 7, 8, 9, 7, 8, 9, 7, 8, 9 ]]

	makeBoxes(A,2,2)
	makeBoxes(B,2,3)
	makeBoxes(B2,3,2)
	makeBoxes(C,3,3)

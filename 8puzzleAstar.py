from copy import deepcopy

# Class to define the puzzle with features for calculating the f value for the A* search
class puzzle:
        def __init__(self, starting, parent):
                self.board = starting
                self.parent = parent
                self.f = 0
                self.g = 0
                self.h = 0
        
        # Used for comparring two boards.
        def __eq__(self, other):
                return self.board == other.board

# For question 1.2 - both heuristics are seen below:
# Calculating the manhattan value, to find the best route
def manhattan(self):
        h = 0
        for i in range(3):
                for n in range(3):
                        x, y = divmod(self.board[i][n], 3) 
                        h += abs(x-i) + abs(y-n) # Finds how far out the number is from its position in the goal state
        return h

# Check how many are in the right row + right column
def colsVsRows(self, goal):
        h = 18 # for a 3x3 grid the highest possible combined value is 18
        q = [], [], []
        g = [], [], []

        # Converting the list to check columns
        for i in range(3):
                for n in range(3):
                        q[i].append(self.board[n][i])
                        g[i].append(goal[n][i])

        for i in range(3):
                for n in range(3):
                        #check the row
                        if self.board[i][n] in goal[i]:
                                h -= 1 
                        # check the column
                        if q[i][n] in g[i]:
                                h -= 1
        return h


# Function to find all of the possible moves for the current blank tile
def possible_move(current):
        current = current.board # asigns to the actual 8 puzzle numbers
        for i in range(3): # For loop for each row and column of the matrix
            for j in range(3):
                if current[i][j] == 0: # Finds the value asigned to the empty space
                        x, y = i, j
                        break
        solutions = []
        # If statements to find all positions to swap the empty space in to
        if x-1 >= 0:
                copy = deepcopy(current) # Using deepcopy for copying the matrix
                copy[x][y] = copy[x-1][y]
                copy[x-1][y] = 0
                move = puzzle(copy, current) # Creates a new object
                solutions.append(move)
        if x+1 < 3:
                copy = deepcopy(current)
                copy[x][y] = copy[x+1][y]
                copy[x+1][y] = 0
                move = puzzle(copy, current)
                solutions.append(move)
        if y-1 >= 0:
                copy = deepcopy(current)
                copy[x][y] = copy[x][y-1]
                copy[x][y-1] = 0
                move = puzzle(copy, current)
                solutions.append(move)
        if y+1 < 3:
                copy = deepcopy(current)
                copy[x][y] = copy[x][y+1]
                copy[x][y+1] = 0
                move = puzzle(copy, current)
                solutions.append(move)
        return solutions

# Function to find the lowest possible next move.
def best_value(openList):
        f = openList[0].f
        index = 0
        for i, item in enumerate(openList):
                if i == 0:
                        continue
                if(item.f < f):
                        f = item.f
                        index = i
        return openList[index], index
       
# Function to run the A-star algorithm
def Astar(puzzle, goal, heuristic):
        openList = [] # All the node that are generated
        closed = [] # All node the explored nodes
        openList.append(puzzle)
        
        while openList:
                current, index = best_value(openList)
                if current == goal:
                        return current
                openList.pop(index)
                closed.append(current)

                X = possible_move(current)
                for move in X:
                        inClosed = False
                        for i, item in enumerate(closed):
                                if item == move:
                                        inClosed = True
                                        break
                        if not inClosed: # If the current move is not in closed
                                new_g_value = current.g + 1 # g value is the number of moves taken to get to this point
                                present = False
                                
                                for n, item in enumerate(openList):
                                        if item == move:
                                                present = True
                                                if new_g_value < openList[n].g:
                                                        openList[n].g = new_g_value
                                                        openList[n].f = openList[n].g + openList[n].h 
                                                        openList[n].parent = current
                                if not present:
                                        move.g = new_g_value
                                        if heuristic == "manhattan":
                                                move.h = manhattan(move)
                                        else:
                                                move.h = colsVsRows(move, goal.board)
                                        move.f = move.g + move.h
                                        move.parent = current
                                        openList.append(move)
          
# The start position for the 8-puzzle 
# Can be changed for any initial state you'd like to use, the 0 represents the blank tile.               
start = puzzle([[7, 2, 4], [5, 0, 6], [8, 3, 1]], None)


# For question 1.3 - this Goal state can be changed, should work with either heuristic.
# The goal state 
goal = puzzle([[0, 1, 2], [3, 4, 5], [6, 7, 8]], None)


# Important - change the commented line to swap the heuristic in use.
# Question 1.3 - Use the "manhattan" heuristic.
heuristic = "manhattan" 
#heuristic = "colVsRows"

goalFound = Astar(start, goal, heuristic)
noMoves = 0 # Counts the number of moves taken to get to the goal
results = []
results.append(goalFound.board)
parent = goalFound.parent

while parent:
        noMoves += 1
        results.append(parent.board)
        parent = parent.parent
                
results.reverse() # Reverses the list to display the method to get to the answer
for i, item in enumerate(results):
        print(item)
print ("Length: " + str(noMoves))                
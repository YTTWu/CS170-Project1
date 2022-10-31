from pip import main
from collections import deque
import math

class Node:
    """
    Define
    data is the array that holds the puzzle
    parent is the previous node
    depth is the depth of the node
    cost is the move of the node
    """
    def __init__(self, data, parent, depth, missingTiles, distance):
        self.data = data
        self.parent = parent
        self.depth = depth
        self.missingTiles = missingTiles
        self.distance = distance

"""
puzzelBoard is the array that holds the puzzle values
zeroPos will hold the position of the zero in the array
findZeroPos() will find the position of the zero in the array
gameSize is the size of the game ex. 3x3, 4x4, 5x5
"""
class PuzzelGame:
    """ keep the puzzel in one dimension array """
    def __init__(self, initialState):
        self.puzzelBoard = initialState
        self.zeroPos = 0
        self.findZeroPos()
        self.gameSize = len(self.puzzelBoard);
        self.rowSize = int(math.sqrt(self.gameSize))
        
    """
    print the game, since its in an array, make a new line when the index is 2, 5, 8
    """
    def printGame(self):
        print("--------------------------------- NEW MOVE ---------------------------------")
        for i in range(len(self.puzzelBoard)):
            print(self.puzzelBoard[i], end = " ")
            if((i + 1) % self.rowSize == 0):
                print("\n")

    def printPath(self, parent):
        for i in range(len(self.puzzelBoard)):
            print(self.puzzelBoard[i], end = " ")
            if((i + 1) % self.rowSize == 0):
                print("\n")
        if parent:
            print("PREVIOUS LEVEL")
            print("DEPTH: ", parent.depth)
            print("               |")
            print("               |")
            print("               V\n")

    """ getter for the array value of the puzzel """
    def getBoard(self):
        return self.puzzelBoard


    """ Uniform Cost Search """
    def uniformCostSearch(self):
        totalNodeExpanded = 0
        largestQueueSize = 0
        # root node
        root = Node(PuzzelGame(self.puzzelBoard), None, 0, 0, 0)
        # object for checking the goal state
        goalCheck = GoalCheck()

        if goalCheck.goalChecker(root.data.getBoard()):
            return [root, totalNodeExpanded, largestQueueSize + 1]
        
        # edge case
        if not root: return None
        # starting our dequeue with the root node
        q = deque([root])
        # instantite a list to hold the visited nodes
        visited = []
        # temp to hold the value of the next move
        temp = []

        

        while q:
            largestQueueSize = max(largestQueueSize, len(q))
            # current state of the game move
            cur_node = q.popleft()

            # get a copy of the current game state, just the value of the array
            temp = cur_node.data.getBoard().copy()
            # skip if we have visited the move
            if temp in visited: continue
            #if not add it to the visited list
            visited.append(temp)

            print("CURRENT LEVEL")
            print("DEPTH: ", cur_node.depth)
            cur_node.data.printGame()
            
            # check if the "0" can move up
            if cur_node.data.moveUp():
                # get a copy of the current game state, just the value of the array
                temp = cur_node.data.getBoard().copy()
                # move it back to the previous position because we were just checking if we could move it
                cur_node.data.moveDown()
                # check if the move is repeated
                if temp not in visited:
                    # if the move is valid, add it to the queue
                    q.append(Node(PuzzelGame(temp), cur_node, cur_node.depth+1, 0, 0))
                    totalNodeExpanded += 1
                    print("NEXT LEVEL")
                    print("DEPTH: ", q[-1].depth)
                    q[-1].data.printGame()
                    # check if the move is the goal state
                    if goalCheck.goalChecker(temp):
                        return [q.pop(),totalNodeExpanded, largestQueueSize + 1]

            # same logic but in different direction   
            if cur_node.data.moveDown():
                temp = cur_node.data.getBoard().copy()
                cur_node.data.moveUp()
                if temp not in visited:
                    q.append(Node(PuzzelGame(temp), cur_node, cur_node.depth+1, 0, 0))
                    totalNodeExpanded += 1
                    print("NEXT LEVEL")
                    print("DEPTH: ", q[-1].depth)
                    q[-1].data.printGame()
                    if goalCheck.goalChecker(temp):
                        return [q.pop(),totalNodeExpanded, largestQueueSize + 1]
                
            # same logic but in different direction
            if cur_node.data.moveLeft():
                temp = cur_node.data.getBoard().copy()
                cur_node.data.moveRight()
                if temp not in visited:
                    q.append(Node(PuzzelGame(temp), cur_node, cur_node.depth+1, 0, 0))
                    totalNodeExpanded += 1
                    print("NEXT LEVEL")
                    print("DEPTH: ", q[-1].depth)
                    q[-1].data.printGame()
                    if goalCheck.goalChecker(temp):
                        return [q.pop(),totalNodeExpanded, largestQueueSize + 1]

            # same logic but in different direction
            if cur_node.data.moveRight():
                temp = cur_node.data.getBoard().copy()
                cur_node.data.moveLeft()
                if temp not in visited:
                    q.append(Node(PuzzelGame(temp), cur_node, cur_node.depth+1, 0, 0))
                    totalNodeExpanded += 1
                    print("NEXT LEVEL")
                    print("DEPTH: ", q[-1].depth)
                    q[-1].data.printGame()
                    if goalCheck.goalChecker(temp):
                        return [q.pop(),totalNodeExpanded, largestQueueSize + 1]
            
            
    # helper function to calculate the missing tiles
    def missingTiles(self):
        count = 0
        for i in range(len(self.puzzelBoard)):
            if (self.puzzelBoard[i] != i+1):
                count += 1
            if (i == self.gameSize - 1 and self.puzzelBoard[i] == 0):
                count -= 1
        return count

    # using dictionary to hold the missing tile for each possible move ex. {8 : node_adderess}
    def misplacedTileHeuristic(self):
        totalNodeExpanded = 0
        largestQueueSize = 0
        # root node
        root = Node(PuzzelGame(self.puzzelBoard), None, 0, 0, 0)
        # calculate the missing tiles for the current state
        root.missingTiles = root.data.missingTiles()
        # object for checking the goal state
        goalCheck = GoalCheck()

        if goalCheck.goalChecker(root.data.getBoard()):
            return [root, totalNodeExpanded, largestQueueSize + 1]
        
        # edge case
        if not root: return None
        # starting our dequeue with the root node
        q = deque([root])
        # instantite a list to hold the visited nodes
        visited = []
        # temp to hold the value of the next move
        temp = []

        while q:
            largestQueueSize = max(largestQueueSize, len(q))
            # current state of the game move
            cur_node = q.popleft()
            totalNodeExpanded += 1
            # get a copy of the current game state, just the value of the array
            temp = cur_node.data.getBoard().copy()
            # skip if we have visited the move
            if temp in visited: continue
            #if not add it to the visited list
            visited.append(temp)

            print("CURRENT LEVEL")
            print("DEPTH: ", cur_node.depth)
            cur_node.data.printGame()
            
            # check if the "0" can move up
            if cur_node.data.moveUp():
                # get a copy of the current game state, just the value of the array
                temp = cur_node.data.getBoard().copy()
                # move it back to the previous position because we were just checking if we could move it
                cur_node.data.moveDown()
                # check if the move is repeated
                if temp not in visited:
                    # create a new node for the new move
                    newMove = PuzzelGame(temp)
                    # if the move is valid, add it to the queue | missingTiles() return the number of missing tiles
                    q.append(Node(newMove, cur_node, cur_node.depth+1, newMove.missingTiles(), 0))
                    print("NEXT LEVEL")
                    print("DEPTH: ", q[-1].depth)
                    q[-1].data.printGame()
                    # check if the move is the goal state
                    if goalCheck.goalChecker(temp):
                        return [q.pop(),totalNodeExpanded, largestQueueSize + 1]

            # same logic but in different direction   
            if cur_node.data.moveDown():
                temp = cur_node.data.getBoard().copy()
                cur_node.data.moveUp()
                if temp not in visited:
                    # create a new node for the new move
                    newMove = PuzzelGame(temp)
                    # if the move is valid, add it to the queue | missingTiles() return the number of missing tiles
                    q.append(Node(newMove, cur_node, cur_node.depth+1, newMove.missingTiles(), 0))
                    print("NEXT LEVEL")
                    print("DEPTH: ", q[-1].depth)
                    q[-1].data.printGame()
                    if goalCheck.goalChecker(temp):
                        return [q.pop(),totalNodeExpanded, largestQueueSize + 1]
                
            # same logic but in different direction
            if cur_node.data.moveLeft():
                temp = cur_node.data.getBoard().copy()
                cur_node.data.moveRight()
                if temp not in visited:
                    # create a new node for the new move
                    newMove = PuzzelGame(temp)
                    # if the move is valid, add it to the queue | missingTiles() return the number of missing tiles
                    q.append(Node(newMove, cur_node, cur_node.depth+1, newMove.missingTiles(), 0))
                    print("NEXT LEVEL")
                    print("DEPTH: ", q[-1].depth)
                    q[-1].data.printGame()
                    if goalCheck.goalChecker(temp):
                        return [q.pop(),totalNodeExpanded, largestQueueSize + 1]

            # same logic but in different direction
            if cur_node.data.moveRight():
                temp = cur_node.data.getBoard().copy()
                cur_node.data.moveLeft()
                if temp not in visited:
                    # create a new node for the new move
                    newMove = PuzzelGame(temp)
                    # if the move is valid, add it to the queue | missingTiles() return the number of missing tiles
                    q.append(Node(newMove, cur_node, cur_node.depth+1, newMove.missingTiles(), 0))
                    print("NEXT LEVEL")
                    print("DEPTH: ", q[-1].depth)
                    q[-1].data.printGame()
                    if goalCheck.goalChecker(temp):
                        return [q.pop(),totalNodeExpanded, largestQueueSize + 1]
            
            #sort the queue based on the missingTiles
            q = deque(sorted(q, key=lambda x: x.missingTiles))


    # helper funciton to calculate the manhattan distance
    def distance(self):
        current = self.puzzelBoard


        distanceCnt = 0
        for i in range(len(current)):
            
            value = current[i]
            goalIndex = value - 1
            if goalIndex == -1:
                continue
                
            rowDiff = abs(i // self.rowSize - goalIndex // self.rowSize)
            colDiff = abs(i % self.rowSize - goalIndex % self.rowSize)
            
            distanceCnt += rowDiff + colDiff
        return distanceCnt





    def manhattamDistanceHeuristic(self):
        totalNodeExpanded = 0
        largestQueueSize = 0
        # root node
        root = Node(PuzzelGame(self.puzzelBoard), None, 0, 0, 0)
        # calculate the missing tiles for the current state
        root.missingTiles = root.data.distance()
        # object for checking the goal state
        goalCheck = GoalCheck()

        if goalCheck.goalChecker(root.data.getBoard()):
            return [root, totalNodeExpanded, largestQueueSize + 1]
        
        # edge case
        if not root: return None
        # starting our dequeue with the root node
        q = deque([root])
        # instantite a list to hold the visited nodes
        visited = []
        # temp to hold the value of the next move
        temp = []

        while q:
            largestQueueSize = max(largestQueueSize, len(q))
            # current state of the game move
            cur_node = q.popleft()
            totalNodeExpanded += 1
            # get a copy of the current game state, just the value of the array
            temp = cur_node.data.getBoard().copy()
            # skip if we have visited the move
            if temp in visited: continue
            #if not add it to the visited list
            visited.append(temp)

            print("CURRENT LEVEL")
            print("DEPTH: ", cur_node.depth)
            cur_node.data.printGame()
            
            # check if the "0" can move up
            if cur_node.data.moveUp():
                # get a copy of the current game state, just the value of the array
                temp = cur_node.data.getBoard().copy()
                # move it back to the previous position because we were just checking if we could move it
                cur_node.data.moveDown()
                # check if the move is repeated
                if temp not in visited:
                    # create a new node for the new move
                    newMove = PuzzelGame(temp)
                    # if the move is valid, add it to the queue | distance() return the shortest distance to the correct position
                    q.append(Node(newMove, cur_node, cur_node.depth+1, 0, newMove.distance()))
                    print("NEXT LEVEL")
                    print("DEPTH: ", q[-1].depth)
                    q[-1].data.printGame()
                    # check if the move is the goal state
                    if goalCheck.goalChecker(temp):
                        return [q.pop(),totalNodeExpanded, largestQueueSize + 1]

            # same logic but in different direction   
            if cur_node.data.moveDown():
                temp = cur_node.data.getBoard().copy()
                cur_node.data.moveUp()
                if temp not in visited:
                    # create a new node for the new move
                    newMove = PuzzelGame(temp)
                    # if the move is valid, add it to the queue | distance() return the shortest distance to the correct position
                    q.append(Node(newMove, cur_node, cur_node.depth+1, 0, newMove.distance()))
                    print("NEXT LEVEL")
                    print("DEPTH: ", q[-1].depth)
                    q[-1].data.printGame()
                    if goalCheck.goalChecker(temp):
                        return [q.pop(),totalNodeExpanded, largestQueueSize + 1]
                
            # same logic but in different direction
            if cur_node.data.moveLeft():
                temp = cur_node.data.getBoard().copy()
                cur_node.data.moveRight()
                if temp not in visited:
                    # create a new node for the new move
                    newMove = PuzzelGame(temp)
                    # if the move is valid, add it to the queue | distance() return the shortest distance to the correct position
                    q.append(Node(newMove, cur_node, cur_node.depth+1, 0, newMove.distance()))
                    print("NEXT LEVEL")
                    print("DEPTH: ", q[-1].depth)
                    q[-1].data.printGame()
                    if goalCheck.goalChecker(temp):
                        return [q.pop(),totalNodeExpanded, largestQueueSize + 1]

            # same logic but in different direction
            if cur_node.data.moveRight():
                temp = cur_node.data.getBoard().copy()
                cur_node.data.moveLeft()
                if temp not in visited:
                    # create a new node for the new move
                    newMove = PuzzelGame(temp)
                    # if the move is valid, add it to the queue | distance() return the shortest distance to the correct position
                    q.append(Node(newMove, cur_node, cur_node.depth+1, 0, newMove.distance()))
                    print("NEXT LEVEL")
                    print("DEPTH: ", q[-1].depth)
                    q[-1].data.printGame()
                    if goalCheck.goalChecker(temp):
                        return [q.pop(),totalNodeExpanded, largestQueueSize + 1]
            
            #sort the queue based on the missingTiles
            q = deque(sorted(q, key=lambda x: x.distance))
        


    def findZeroPos(self):
        for i in range(len(self.puzzelBoard)):
            if(self.puzzelBoard[i] == 0):
                self.zeroPos = i


    def moveUp(self):
        # 0 cant not be at the first row
        if self.zeroPos >= self.rowSize:
            # basic swap
            temp = self.puzzelBoard[self.zeroPos - 3]
            self.puzzelBoard[self.zeroPos - 3] = self.puzzelBoard[self.zeroPos]
            self.puzzelBoard[self.zeroPos] = temp
            self.zeroPos = self.zeroPos - 3
            return True
        else:
            return False
            
    
    def moveDown(self):
        # 0 cant not be at the last row
        if self.zeroPos <= self.gameSize - self.rowSize - 1:
            temp = self.puzzelBoard[self.zeroPos + 3]
            self.puzzelBoard[self.zeroPos + 3] = self.puzzelBoard[self.zeroPos]
            self.puzzelBoard[self.zeroPos] = temp
            self.zeroPos = self.zeroPos + 3
            return True
        else:
            return False

    def moveLeft(self):
        # 0 cant not be at the first column
        if self.zeroPos % self.rowSize != 0:
            temp = self.puzzelBoard[self.zeroPos - 1]
            self.puzzelBoard[self.zeroPos - 1] = self.puzzelBoard[self.zeroPos]
            self.puzzelBoard[self.zeroPos] = temp
            self.zeroPos = self.zeroPos - 1
            return True
        else:
            return False

    def moveRight(self):
        # 0 cant not be at the last column
        if (self.zeroPos + 1) % self.rowSize != 0:
            temp = self.puzzelBoard[self.zeroPos + 1]
            self.puzzelBoard[self.zeroPos + 1] = self.puzzelBoard[self.zeroPos]
            self.puzzelBoard[self.zeroPos] = temp
            self.zeroPos = self.zeroPos + 1
            return True
        else:   
            return False



class GoalCheck:
    def __init__(self) -> None:
        pass

    def goalChecker(self, puzzel):
        for i in range(len(puzzel)):
            if (i == len(puzzel) - 1 and puzzel[i] != 0):
                return False
            if(i != len(puzzel) - 1 and puzzel[i] != i+1):
                return False
        print("GOAL STATE FOUND!!!")
        return True

class PuzzelGameIntro:
    def __init__(self) -> None:
        pass

    def intro(self):
        print("Welcome to the 8 Puzzel Game Solver Program")
        userInput = input("\nType \"1\" to start with a default puzzle\nType \"2\" to start with your own custom puzzle: ")
        puzzelBoard = []
        if userInput == "1":
            print("Default Puzzle: ")
    
            print("Puzzle 1:\n1 2 3\n4 5 6\n7 8 0\n")
            print("Puzzle 2:\n1 2 3\n4 5 6\n0 7 8\n")
            print("Puzzle 3:\n1 3 6\n5 0 7\n4 8 2\n")
            print("Puzzle 4:\n0 7 2\n4 6 1\n3 5 8\n")
            print("Type number to choice default puzzel correspondingly (Type 1 to choose Puzzle 1)")
            defaultChoice = input()
            if defaultChoice == "1":
                puzzelBoard = [1,2,3,4,5,6,7,8,0]
            elif defaultChoice == "2":
                puzzelBoard = [1,2,3,4,5,6,0,7,8]
            elif defaultChoice == "3":
                puzzelBoard = [1,3,6,5,0,7,4,8,2]
            elif defaultChoice == "4":
                puzzelBoard = [0,7,2,4,6,1,3,5,8]

        elif userInput == "2":
            rowSize = input("\nPlease enter the size of the puzzle.\n(For example: (3) 3x3 | (4) 4x4 | (5) 5x5): ")

        

            print("Please enter your puzzle below, use a space to represent the blank")
            temp = ""
            for i in range(int(rowSize)):
                print("\nEnter the row number " + str(i + 1) + " of the puzzel.  Use space in between numbers")
                temp += input() + " "

            puzzelBoard = [int(i) for i in temp.split()]

        print("Please select the algorithm you would like to use: ")
        print("(1). Uniform Cost Search / Breadth First Search")
        print("(2). A* with Misplaced Tile Heuristic")
        print("(3). A* with Manhattan Distance Heuristic")
        userChoice = input()
        if userChoice == '1':
            game = PuzzelGame(puzzelBoard)
            return game.uniformCostSearch()
        elif userChoice == '2':
            game = PuzzelGame(puzzelBoard)
            return game.misplacedTileHeuristic()
        elif userChoice == '3':
            game = PuzzelGame(puzzelBoard)
            return game.manhattamDistanceHeuristic()


    
    
    
def main():
    start = PuzzelGameIntro()

  
    temp = start.intro()
    finalNode = temp[0]
    totalNodeExpanded = temp[1]
    totalDepth = finalNode.depth
    largestQueueSize = temp[2]
    
    print("Total Node Expanded: ", totalNodeExpanded)
    print("Total Depth: ", totalDepth)
    print("Largest Queue Size: ", largestQueueSize)

    print("--------------------------------- BACK TRACING ---------------------------------")

    tail = Node(finalNode.data, finalNode.parent, finalNode.depth, finalNode.missingTiles, finalNode.distance)
    while tail:
        tail.data.printPath(tail.parent)
        tail = tail.parent

main()
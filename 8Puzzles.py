from pip import main
from collections import deque

class Node:
    """
    Define
    data is the array that holds the puzzle
    parent is the previous node
    depth is the depth of the node
    cost is the move of the node
    """
    def __init__(self, data, parent, depth):
        self.data = data
        self.parent = parent
        self.depth = depth

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
        
    """
    print the game, since its in an array, make a new line when the index is 2, 5, 8
    """
    def printGame(self):
        print("--------------------------------- NEW MOVE ---------------------------------")
        for i in range(len(self.puzzelBoard)):
            print(self.puzzelBoard[i], end = " ")
            if(i == 2 or i == 5 or i == 8):
                print("\n")

    def printPath(self, parent):
        for i in range(len(self.puzzelBoard)):
            print(self.puzzelBoard[i], end = " ")
            if(i == 2 or i == 5 or i == 8):
                print("\n")
        if parent:
            print("PREVIOUS LEVEL")
            print("               |")
            print("               |")
            print("               V\n")

    """ getter for the array value of the puzzel """
    def getBoard(self):
        return self.puzzelBoard


    """ Uniform Cost Search """
    def uniformCostSearch(self):
        # root node
        root = Node(PuzzelGame(self.puzzelBoard), None, 0)
        # object for checking the goal state
        goalCheck = GoalCheck()
        
        # edge case
        if not root: return None
        # starting our dequeue with the root node
        q = deque([root])
        # instantite a list to hold the visited nodes
        visited = []
        # temp to hold the value of the next move
        temp = []

        

        while q:
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
                    q.append(Node(PuzzelGame(temp), cur_node, cur_node.depth+1))
                    print("NEXT LEVEL")
                    print("DEPTH: ", q[-1].depth)
                    q[-1].data.printGame()
                    # check if the move is the goal state
                    if goalCheck.goalChecker(temp):
                        return q.pop()

            # same logic but in different direction   
            if cur_node.data.moveDown():
                temp = cur_node.data.getBoard().copy()
                cur_node.data.moveUp()
                if temp not in visited:
                    q.append(Node(PuzzelGame(temp), cur_node, cur_node.depth+1))
                    print("NEXT LEVEL")
                    print("DEPTH: ", q[-1].depth)
                    q[-1].data.printGame()
                    if goalCheck.goalChecker(temp):
                        return q.pop()
                
            # same logic but in different direction
            if cur_node.data.moveLeft():
                temp = cur_node.data.getBoard().copy()
                cur_node.data.moveRight()
                if temp not in visited:
                    q.append(Node(PuzzelGame(temp), cur_node, cur_node.depth+1))
                    print("NEXT LEVEL")
                    print("DEPTH: ", q[-1].depth)
                    q[-1].data.printGame()
                    if goalCheck.goalChecker(temp):
                        return q.pop()

            # same logic but in different direction
            if cur_node.data.moveRight():
                temp = cur_node.data.getBoard().copy()
                cur_node.data.moveLeft()
                if temp not in visited:
                    q.append(Node(PuzzelGame(temp), cur_node, cur_node.depth+1))
                    print("NEXT LEVEL")
                    print("DEPTH: ", q[-1].depth)
                    q[-1].data.printGame()
                    if goalCheck.goalChecker(temp):
                        return q.pop()
            
            

        


    def findZeroPos(self):
        for i in range(len(self.puzzelBoard)):
            if(self.puzzelBoard[i] == 0):
                self.zeroPos = i

    """need to use mod instead fixed number since we need to make the game interchangeble to different size-----------------------------------------come back later"""
    def moveUp(self):
        # 0 cant not be at the first row
        if self.zeroPos != 0 and self.zeroPos != 1 and self.zeroPos != 2:
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
        if self.zeroPos != 6 and self.zeroPos != 7 and self.zeroPos != 8:
            temp = self.puzzelBoard[self.zeroPos + 3]
            self.puzzelBoard[self.zeroPos + 3] = self.puzzelBoard[self.zeroPos]
            self.puzzelBoard[self.zeroPos] = temp
            self.zeroPos = self.zeroPos + 3
            return True
        else:
            return False

    def moveLeft(self):
        # 0 cant not be at the first column
        if self.zeroPos != 0 and self.zeroPos != 3 and self.zeroPos != 6:
            temp = self.puzzelBoard[self.zeroPos - 1]
            self.puzzelBoard[self.zeroPos - 1] = self.puzzelBoard[self.zeroPos]
            self.puzzelBoard[self.zeroPos] = temp
            self.zeroPos = self.zeroPos - 1
            return True
        else:
            return False

    def moveRight(self):
        # 0 cant not be at the last column
        if self.zeroPos != 2 and self.zeroPos != 5 and self.zeroPos != 8:
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

    # come back later------------------------------------------------------------------------------------------------------
    def goalChecker(self, puzzel):
        for i in range(len(puzzel)):
            if (i == 8 and puzzel[i] != 0):
                return False
            if(i != 8 and puzzel[i] != i+1):
                return False
        print("GOAL STATE FOUND!!!")
        return True

class PuzzelGameIntro:
    def __init__(self) -> None:
        pass

    def intro(self):
        print("Welcome to the 8 Puzzel Game Solver Program")
        userInput = input("Type \"1\" to start with a default puzzle Type \"2\" to start with your own custom puzzle: ")
        puzzelBoard = []
        if userInput == "2":
            print("Please enter your puzzle below, use a zero to represent the blank")
            print("Enter the first row, use space or tabs between numbers")
            firstRow = input()
            
            print("Enter the second row, use space or tabs between numbers")
            secondRow = input()
            
            print("Enter the third row, use space or tabs between numbers")
            thirdRow = input()
            
            temp = firstRow + " " + secondRow + " " + thirdRow
            puzzelBoard = [int(i) for i in temp.split()]

            print("Please select the algorithm you would like to use: ")
            print("(1). Uniform Cost Search / Breadth First Search")
            print("(2). A* with Misplaced Tile Heuristic")
            print("(3). A* with Manhattan Distance Heuristic")
            userChoice = input()
            if userChoice == '1':
                game = PuzzelGame(puzzelBoard)
                return game.uniformCostSearch()


    
    
    
def main():
    start = PuzzelGameIntro()

    finalNode = start.intro()
    print("Goal Reached")

    tail = Node(finalNode.data, finalNode.parent, finalNode.depth)
    while tail:
        tail.data.printPath(tail.parent)
        tail = tail.parent

main()
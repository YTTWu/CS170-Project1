from pip import main
from collections import deque

class Node:
    def __init__(self, data, parent, depth, cost):
        self.data = data
        self.parent = parent
        self.depth = depth
        self.cost = cost

class PuzzelGame:
    """ keep the puzzel in one dimension array """
    def __init__(self, initialState):
        self.puzzelBoard = initialState
        self.zeroPos = 0
        self.findZeroPos()
        self.gameSize = len(self.puzzelBoard);
        
    def printGame(self):
        for i in range(len(self.puzzelBoard)):
            print(self.puzzelBoard[i], end = " ")
            if(i == 2 or i == 5 or i == 8):
                print("\n")



    def getBoard(self):
        return self.puzzelBoard


    """ Uniform Cost Search """
    def uniformCostSearch(self):
        root = Node(PuzzelGame(self.puzzelBoard), None, 0, 0)
        goalCheck = GoalCheck()
        
        if not root: return None
        q = deque([root])
        level = 0
        visited = []
        temp = []

        

        while q:
            cur_node = q.popleft()

            temp = cur_node.data.getBoard().copy()

            if temp in visited: continue
            visited.append(temp)

            

            cur_node.data.printGame()
            
            if cur_node.data.moveUp():
                temp = cur_node.data.getBoard().copy()
                cur_node.data.moveDown()
                if temp not in visited:
                    q.append(Node(PuzzelGame(temp),cur_node, cur_node.depth+1, cur_node.cost+1))
                
            if cur_node.data.moveDown():
                temp = cur_node.data.getBoard().copy()
                cur_node.data.moveUp()
                if temp not in visited:
                    q.append(Node(PuzzelGame(temp),cur_node, cur_node.depth+1, cur_node.cost+1))
                

            if cur_node.data.moveLeft():
                temp = cur_node.data.getBoard().copy()
                cur_node.data.moveRight()
                if temp not in visited:
                    q.append(Node(PuzzelGame(temp),cur_node, cur_node.depth+1, cur_node.cost+1))

            if cur_node.data.moveRight():
                temp = cur_node.data.getBoard().copy()
                cur_node.data.moveLeft()
                if temp not in visited:
                    q.append(Node(PuzzelGame(temp),cur_node, cur_node.depth+1, cur_node.cost+1))
                    if goalCheck.goalChecker(temp):
                        return q.pop()
            
            

        


    def findZeroPos(self):
        for i in range(len(self.puzzelBoard)):
            if(self.puzzelBoard[i] == 0):
                self.zeroPos = i

    """need to use mod instead fixed number since we need to make the game interchangeble to different size"""
    def moveUp(self):
        if self.zeroPos != 0 and self.zeroPos != 1 and self.zeroPos != 2:
            temp = self.puzzelBoard[self.zeroPos - 3]
            self.puzzelBoard[self.zeroPos - 3] = self.puzzelBoard[self.zeroPos]
            self.puzzelBoard[self.zeroPos] = temp
            self.zeroPos = self.zeroPos - 3
            self.printGame()
            return True
        else:
            return False
            
    
    def moveDown(self):
        if self.zeroPos != 6 and self.zeroPos != 7 and self.zeroPos != 8:
            temp = self.puzzelBoard[self.zeroPos + 3]
            self.puzzelBoard[self.zeroPos + 3] = self.puzzelBoard[self.zeroPos]
            self.puzzelBoard[self.zeroPos] = temp
            self.zeroPos = self.zeroPos + 3
            self.printGame()
            return True
        else:
            return False
    def moveLeft(self):
        if self.zeroPos != 0 and self.zeroPos != 3 and self.zeroPos != 6:
            temp = self.puzzelBoard[self.zeroPos - 1]
            self.puzzelBoard[self.zeroPos - 1] = self.puzzelBoard[self.zeroPos]
            self.puzzelBoard[self.zeroPos] = temp
            self.zeroPos = self.zeroPos - 1
            self.printGame()
            return True
        else:
            return False

    def moveRight(self):
        if self.zeroPos != 2 and self.zeroPos != 5 and self.zeroPos != 8:
            temp = self.puzzelBoard[self.zeroPos + 1]
            self.puzzelBoard[self.zeroPos + 1] = self.puzzelBoard[self.zeroPos]
            self.puzzelBoard[self.zeroPos] = temp
            self.zeroPos = self.zeroPos + 1
            self.printGame()
            return True
        else:   
            return False

class GoalCheck:
    def __init__(self) -> None:
        pass

    def goalChecker(self, puzzel):
        for i in range(len(puzzel)):
            if (i == 8 and puzzel[i] != 0):
                return False
            if(i != 8 and puzzel[i] != i+1):
                return False
        """need to find the best way to print the puzzel, right now is redondant"""
        for i in range(len(puzzel)):
            print(puzzel[i], end = " ")
            if(i == 2 or i == 5 or i == 8):
                print("\n")
        
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

    if start.intro():
        print("Goal Reached")

    # game.printGame()
    # game.moveDown()
    # game.printGame()
    # game.moveRight()
    # game.printGame()

main()
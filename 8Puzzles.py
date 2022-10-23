from pip import main

class PuzzelGame:
    """ keep the puzzel in one dimension array """
    def __init__(self, initialState):
        self.puzzelBoard = initialState
        self.zeroPos = 0;
        self.gameSize = len(self.puzzelBoard);
        


    def printGame(self):
        for i in range(len(self.puzzelBoard)):
            print(self.puzzelBoard[i], end = " ")
            if(i == 2 or i == 5 or i == 8):
                print("\n")
    
    def uniformCostSearch(self):
        """ Uniform Cost Search """


    def findZeroPos(self):
        for i in range(len(self.puzzelBoard)):
            if(i == 0):
                self.zeroPos = i

    """need to use mod instead fixed number since we need to make the game interchangeble to different size"""
    def moveUp(self):
        if self.zeroPos != 0 or self.zeroPos != 1 or self.zeroPos != 2:
            temp = self.puzzelBoard[self.zeroPos - 3]
            self.puzzelBoard[self.zeroPos - 3] = self.puzzelBoard[self.zeroPos]
            self.puzzelBoard[self.zeroPos] = temp
            self.zeroPos = self.zeroPos - 3
    
    def moveDown(self):
        if self.zeroPos != 6 or self.zeroPos != 7 or self.zeroPos != 8:
            temp = self.puzzelBoard[self.zeroPos + 3]
            self.puzzelBoard[self.zeroPos + 3] = self.puzzelBoard[self.zeroPos]
            self.puzzelBoard[self.zeroPos] = temp
            self.zeroPos = self.zeroPos + 3
    def moveLeft(self):
        if self.zeroPos != 0 or self.zeroPos != 3 or self.zeroPos != 6:
            temp = self.puzzelBoard[self.zeroPos - 1]
            self.puzzelBoard[self.zeroPos - 1] = self.puzzelBoard[self.zeroPos]
            self.puzzelBoard[self.zeroPos] = temp
            self.zeroPos = self.zeroPos - 1

    def moveRight(self):
        if self.zeroPos != 2 or self.zeroPos != 5 or self.zeroPos != 8:
            temp = self.puzzelBoard[self.zeroPos + 1]
            self.puzzelBoard[self.zeroPos + 1] = self.puzzelBoard[self.zeroPos]
            self.puzzelBoard[self.zeroPos] = temp
            self.zeroPos = self.zeroPos + 1

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

            return PuzzelGame(puzzelBoard)
    
    
    
def main():
    start = PuzzelGameIntro()

    game = start.intro()

    game.printGame()
    game.moveDown()
    game.printGame()
    game.moveRight()
    game.printGame()

main()
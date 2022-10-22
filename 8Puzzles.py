from pip import main

class PuzzelGame:
    def __init__(self, firstRow, secondRow, thirdRow):
        self.firstRow = firstRow
        self.secondRow = secondRow
        self.thirdRow = thirdRow


    def printGame(self):
        print(self.firstRow)
        print(self.secondRow)
        print(self.thirdRow)
        print("/n")

class PuzzelGameIntro:
    def __init__(self) -> None:
        pass

    def intro(self):
        print("Welcome to the 8 Puzzel Game Solver Program")
        userInput = input("Type \"1\" to start with a default puzzle Type \"2\" to start with your own custom puzzle: ")
        
        if userInput == "2":
            print("Please enter your puzzle below, use a zero to represent the blank")
            print("Enter the first row, use space or tabs between numbers")
            firstRow = input()
            print("Enter the second row, use space or tabs between numbers")
            secondRow = input()
            print("Enter the third row, use space or tabs between numbers")
            thirdRow = input()
            return PuzzelGame(firstRow, secondRow, thirdRow)
    
    
        


    
def main():
    game = PuzzelGameIntro()

    puzzel = game.intro()
    puzzel.printGame()

main()
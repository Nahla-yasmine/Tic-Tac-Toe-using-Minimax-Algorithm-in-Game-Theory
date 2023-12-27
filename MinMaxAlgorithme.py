class TicTacToe:
    #Initialize with empty board
    def __init__(self):
        
        self.board = [" " for _ in range(9)]
#Format and print board
    def show(self):
        
        print("""
          {} | {} | {}
         -----------
          {} | {} | {}
         -----------
          {} | {} | {}
        """.format(*self.board))
    #Clear the board
    def clearBoard(self):
       
        self.board = [" " for _ in range(9)]
    #"""Return the winner of the game or 'Nobody' if it's a draw"""
    def whoWon(self):
        
        if self.checkWin("X"):
            return "X the player"
        elif self.checkWin("O"):
            return "O Machine"
        elif self.gameOver():
            return "Nobody"
#Return empty spaces on the board"""
    def availableMoves(self):
       
        moves = []
        for i in range(0, len(self.board)):
            if self.board[i] == " ":
                moves.append(i)
        return moves
    #"""Make a move on the board"""
    def makeMove(self, position, player):
               self.board[position] = player
    #Return True if the player has won, else return False"""
    def checkWin(self, player):
        
        combos = ([0, 1, 2], [3, 4, 5], [6, 7, 8],
                  [0, 3, 6], [1, 4, 7], [2, 5, 8],
                  [0, 4, 8], [2, 4, 6])

        for combo in combos:
            if all(self.board[i] == player for i in combo):
                return True
        return False
#Return True if the game is over, else return False"""
    def gameOver(self):
       
        return all(cell != " " for cell in self.board)
#Minimax algorithm with depth for evaluating the moves"""
    def minimax(self, depth, isMaximizingPlayer):
      
        if self.checkWin("X"):
            return 10 - depth
        elif self.checkWin("O"):
            return depth - 10
        elif self.gameOver():
            return 0

        if isMaximizingPlayer:
            bestVal = -float('inf')
            for move in self.availableMoves():
                self.makeMove(move, "X")
                bestVal = max(bestVal, self.minimax(depth + 1, not isMaximizingPlayer))
                self.makeMove(move, " ")
            return bestVal
        else:
            bestVal = float('inf')
            for move in self.availableMoves():
                self.makeMove(move, "O")
                bestVal = min(bestVal, self.minimax(depth + 1, not isMaximizingPlayer))
                self.makeMove(move, " ")
            return bestVal
    #Finds the best move using the minimax algorithm
    def findBestMove(self):
   
        bestMove = -1
        bestValue = -float('inf')
        for move in self.availableMoves():
            self.makeMove(move, "X")
            moveValue = self.minimax(0, False)
            self.makeMove(move, " ")

            if moveValue > bestValue:
                bestValue = moveValue
                bestMove = move
        return bestMove


# Actual game
if __name__ == '__main__':
    game = TicTacToe()
    game.show()

    while not game.gameOver():
        person_move = int(input("You are X: Choose number from 1-9: ")) - 1
        game.makeMove(person_move, "X")
        game.show()

        if game.gameOver():
            break

        print("Computer choosing move...")
        ai_move = game.findBestMove()
        game.makeMove(ai_move, "O")
        game.show()
        print(f"Computer played at position {ai_move + 1}")
    print("Game Over. " + game.whoWon() + " Wins")

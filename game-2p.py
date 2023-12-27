class TicTacToe:
    def __init__(self):
        """Initialize with empty board"""
        self.board = [" " for _ in range(9)]

    def show(self):
        """Format and print board"""
        print("""
          {} | {} | {}
         -----------
          {} | {} | {}
         -----------
          {} | {} | {}
        """.format(*self.board))

    def clearBoard(self):
        """Clear the board"""
        self.board = [" " for _ in range(9)]

    def whoWon(self):
        """Return the winner of the game or 'Nobody' if it's a draw"""
        if self.checkWin("X"):
            return "X"
        elif self.checkWin("O"):
            return "O"
        elif self.gameOver():
            return "Nobody"

    def availableMoves(self):
        """Return empty spaces on the board"""
        moves = []
        for i in range(0, len(self.board)):
            if self.board[i] == " ":
                moves.append(i)
        return moves

    def makeMove(self, position, player):
        """Make a move on the board"""
        self.board[position] = player

    def checkWin(self, player):
        """Return True if the player has won, else return False"""
        combos = ([0, 1, 2], [3, 4, 5], [6, 7, 8],
                  [0, 3, 6], [1, 4, 7], [2, 5, 8],
                  [0, 4, 8], [2, 4, 6])

        for combo in combos:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def gameOver(self):
        """Return True if the game is over, else return False"""
        return all(cell != " " for cell in self.board)


# Actual game
if __name__ == '__main__':
    game = TicTacToe()
    game.show()

    current_player = "X"  # 'X' starts the game

    while not game.gameOver():
        person_move = int(input(f"You are {current_player}: Choose number from 1-9: ")) - 1
        
        if game.board[person_move] != " ":
            print("Invalid move! Try again.")
            continue
        
        game.makeMove(person_move, current_player)
        game.show()
        
        if game.checkWin(current_player):  # Check for winner after each move
            print(f"Game Over. {current_player} Wins")
            break
        
        current_player = "O" if current_player == "X" else "X"  # Switch players
        
    if game.whoWon() == "Nobody":
        print("Game Over. It's a draw!")
 



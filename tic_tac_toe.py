class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.rows = [0]*n
        self.cols = [0]*n
        self.diag = 0
        self.anti_diag = 0
        self.board = [[None]*n for _ in range(n)]
        self.N = n
    
    def check_filled_row(self, i, p):
        
        for j in range(self.N):
            if self.board[i][j]!=p:
                return False
            
        return True
            
    def check_filled_col(self, j, p):
        
        for i in range(self.N):
            if self.board[i][j]!=p:
                return False
            
        return True
    
    def check_filled_diag(self, p):
        
        for i in range(self.N):
            if self.board[i][i]!=p:
                return False
            
        return True
    
    def check_filled_antidiag(self, p):
        
        for i in range(self.N):
            if self.board[i][self.N-i-1]!=p:
                return False
            
        return True
            
    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        
        self.rows[row] += 1
        self.cols[col] += 1
        self.board[row][col] = player
        
        if row==col:
            self.diag += 1
            
        if row+col==self.N-1:
            self.anti_diag += 1
        
        if self.rows[row] == self.N:
            winr = self.check_filled_row(row, player)
            if winr:
                return player
        
        if self.cols[col] == self.N:
            winc = self.check_filled_col(col, player)
            if winc:
                return player
        
        if self.diag==self.N:
            wind = self.check_filled_diag(player)
            if wind:
                return player
        
        if self.anti_diag==self.N:
            wina = self.check_filled_antidiag(player)
            if wina:
                return player
            
        return 0

game = TicTacToe(3)
game.move(1,1,2)
game.move(0,2,2)
game.move(2,0,2)

def solve(board):

    m = len(board)
    n = len(board[0])

    def recur(board, i, j, prev_val, new_val):
        if i<0 or j<0 or i>=m or j>=n:
            return 

        if board[i][j]!=prev_val:
            return 

        board[i][j] = new_val

        recur(board, i-1, j, prev_val, new_val)
        recur(board, i, j-1, prev_val, new_val)
        recur(board, i+1, j, prev_val, new_val)
        recur(board, i, j+1, prev_val, new_val)

    for i in range(m):
        for j in range(n):
            if board[i][j]=='O':
                board[i][j] = '*'

    # Take care of boundaries
    for i in range(m):
        if board[i][0]=='*':
            recur(board, i, 0, '*', 'O')

    for i in range(m):
        if board[i][n-1]=='*':
            recur(board, i, n-1, '*', 'O')

    for j in range(n):
        if board[0][j]=='*':
            recur(board, 0, j, '*', 'O')

    for j in range(n):
        if board[m-1][j]=='*':
            recur(board, m-1, j, '*', 'O')

    for i in range(m):
        for j in range(n):
            if board[i][j]=='*':
                board[i][j] = 'X'
    
    return board 
    
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
solve(board)
board

board = [["O"]*3 for _ in range(5)]
solve(board)
board

board = [["X"]*3 for _ in range(5)]
board[1][1] = 'O'
solve(board)
board

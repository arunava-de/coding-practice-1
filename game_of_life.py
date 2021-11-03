def live_nbrs(i, j, m, n, B):
    x = [-1,-1,-1,0,0,+1,+1,+1]
    y = [-1,0,+1,-1,+1,-1,0,+1]
    nbrs = 0

    for k in range(8):
        if i+x[k]>=m or i+x[k]<0 or j+y[k]>=n or j+y[k]<0 or B[i+x[k]][j+y[k]]==0 or B[i+x[k]][j+y[k]]=="was_dead_will_live":
            continue
        nbrs += 1
    return nbrs


def game(board):
    m = len(board)
    n = len(board[0])

    if m==1 and n==1:
        board[0][0] = 0
        return

    for i in range(m):
        for j in range(n):
            nbr_count = live_nbrs(i, j, m, n, board)
            if board[i][j]==1 or str(board[i][j]).startswith("was_living"):
                if nbr_count<2:
                    board[i][j] = "was_living_will_die"
                elif nbr_count in [2,3]:
                    board[i][j] = "was_living_will_live"
                else:
                    board[i][j] = "was_living_will_die"
            else:
                if nbr_count==3:
                    board[i][j] = "was_dead_will_live"

    for i in range(m):
        for j in range(n):
            if board[i][j] in ["was_living_will_live", "was_dead_will_live"]:
                board[i][j] = 1
            elif board[i][j]=="was_living_will_die":
                board[i][j] = 0
    return 
    
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
game(board)
print(board)

board = [[1,1],[1,0]]
game(board)
print(board)

board = [[1]]
game(board)
print(board)
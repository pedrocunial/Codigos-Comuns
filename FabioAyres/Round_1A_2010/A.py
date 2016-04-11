# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 18:44:59 2016

@author: Fabio
"""

#file_in = "A-test.in"
#file_out = "A-test.out"
#file_in = "A-small-practice.in"
#file_out = "A-small-practice.out"
file_in = "A-large-practice.in"
file_out = "A-large-practice.out"

def print_board(board):
    for line in board:
        print("".join(line))

def check_winner(board, N, K):
    winner = {'R': False, 'B': False}
    
    # Rows.
    for i in range(N):
        for j in range(N - K + 1):
            piece = board[i][j]
            if piece != '.':
                same = True
                for k in range(K):
                    if board[i][j+k] != piece:
                        same = False
                        break
                if same:
                    winner[piece] = True
    
    # Cols.
    for j in range(N):
        for i in range(N - K + 1):
            piece = board[i][j]
            if piece != '.':
                same = True
                for k in range(K):
                    if board[i+k][j] != piece:
                        same = False
                        break
                if same:
                    winner[piece] = True
                    
    # Diag down.
    for i in range(N - K + 1):
        for j in range(N - K + 1):
            piece = board[i][j]
            if piece != '.':
                same = True
                for k in range(K):
                    if board[i+k][j+k] != piece:
                        same = False
                        break
                if same:
                    winner[piece] = True
                    
    # Diag up.
    for i in range(K - 1, N):
        for j in range(N - K + 1):
            piece = board[i][j]
            if piece != '.':
                same = True
                for k in range(K):
                    if board[i-k][j+k] != piece:
                        same = False
                        break
                if same:
                    winner[piece] = True
                    
    if winner['R'] and winner['B']:
        return "Both"
    elif winner['R']:
        return "Red"
    elif winner['B']:
        return "Blue"
    else:
        return "Neither"

def solve(N, K, board):
    for i in range(N):
        line = []
        for j in range(N):
            if board[i][j] != '.':
                line.append(board[i][j])
        board[i] = (N - len(line))*['.'] + line
        
    return check_winner(board, N, K)

with open(file_in, "r") as fin, open(file_out, "w") as fout:
    T = int(fin.readline().strip())
    for case in range(1, T + 1):
        N, K = [int(x) for x in fin.readline().strip().split()]
        board = []
        for i in range(N):
            board.append([c for c in fin.readline().strip()])
        print("Case #{0}: {1}".format(case, solve(N, K, board)))
        fout.write("Case #{0}: {1}\n".format(case, solve(N, K, board)))

        
        
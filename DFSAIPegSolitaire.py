# solving Peg Solitaire using DFS algorithm
# created by saeedinejad and rex in Jan 25, 2021
import datetime
import copy

# constants
PEG = '.'
HOLE = '-'
BLANK = 'X'

# setup the bard
def setupBoard():
    row = [PEG for x in range(7)]
    board = [row[:] for y in range(7)]
    invalid = [(0, 0), (0, 1), (1, 0), (1, 1),
               (5, 0), (5, 1), (6, 0), (6, 1),
               (0, 5), (0, 6), (1, 5), (1, 6),
               (5, 5), (5, 6), (6, 5), (6, 6)]
    for x, y in invalid:
        board[x][y] = BLANK
    board[3][3] = HOLE
    return board

# check if peg can move -y, +y, -x and +x
def isValidMove(m, x, y, d):
    if not m[x][y] == PEG: return False
    if d == 'LEFT' and y > 1 and m[x][y-1] == PEG and m[x][y-2] == HOLE or \
       d == 'RIGHT' and y < 5 and m[x][y+1] == PEG and m[x][y+2] == HOLE or \
       d == 'UP' and x > 1 and m[x-1][y] == PEG and m[x-2][y] == HOLE or \
       d == 'DOWN' and x < 5 and m[x+1][y] == PEG and m[x+2][y] == HOLE:
       return True
    return False

# move the pegs
def move(m, x, y, d):
    m[x][y] = HOLE
    if d == 'LEFT':
        m[x][y-1] = HOLE
        m[x][y-2] = PEG
    if d == 'RIGHT':
        m[x][y+1] = HOLE
        m[x][y+2] = PEG
    if d == 'UP':
        m[x-1][y] = HOLE
        m[x-2][y] = PEG
    if d == 'DOWN':
        m[x+1][y] = HOLE
        m[x+2][y] = PEG

# return valid moves
def validMoves(m):
    return [(x, y, d)
            for x in range(7)
            for y in range(7)
            for d in ['LEFT', 'RIGHT', 'UP', 'DOWN']
                if isValidMove(m, x, y, d)]


def countPegs(m):
    return len([m[i][j] for i in range(7)
                        for j in range(7)
                            if m[i][j] == PEG])

# check if there is just one peg on board - meaning: solved the game
def solved(m):
    return countPegs(m) == 1


def prettifyList(solution, startTime, endTime):
    print(*solution, sep = "\n")
    print("Total Moves: ", len(solution))
    print ("Start Time = ", startTime)
    print ("End Time = ", endTime)


def play(m, solution):
    if solved(m):
        return True

    to_test = validMoves(m)
    for t in to_test:
        m_copy = copy.deepcopy(m)
        move(m_copy, *t)
        if play(m_copy, solution):
            solution.append(t)
            return True
    return False

startTime = datetime.datetime.now()
board = setupBoard()
solution = []
play(board, solution)
endTime = datetime.datetime.now()
solution.reverse()
prettifyList(solution, startTime, endTime)
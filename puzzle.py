"""
board validation
"""


def row_check(board: list) -> bool:
    """
    Check whether colored cells of each row contains numbers
    from 1 to 9 without repetition
    >>> row_check(["**** ***.","***1 **.*","**  3*.**","* 4 1.***",\
"    .9 5 "," 6 .83  *","3 . 1  **"," .8  2***",". 2  ****"])
    True
    """
    count = 0
    board_edited = [i.replace("*", "").replace(" ", "") for i in board]
    for raw in board_edited:
        if len(raw) != len(set(raw)):
            count += 1
    if count == 0:
        return True
    return False


def column_check(board: list) -> bool:
    """
    Check whether colored cells of each column contains numbers
    from 1 to 9 without repetition
    >>> column_check(["**** ***.","***1 **.*","**  3*.**","* 4 1.***",\
"    .9 5 "," 6 .83  *","3 . 1  **"," .8  2***",". 2  ****"])
    False
    """
    new_board = [""*i for i in range(len(board[0]))]
    num = 0
    while num != len(board[0]):
        for i in range(len(board)):
            new_board[num] += board[i][num]
        num += 1
    return row_check(new_board)


def block_check(board: list) -> bool:
    """
    Check whether each block of cells of the same color contains
    numbers from 1 to 9 without repetition
    >>> block_check(["**** ***.","***1 **.*","**  3*.**","* 4 1.***",\
"    .9 5 "," 6 .83  *","3 . 1  **"," .8  2***",". 2  ****"])
    True
    """
    new_board = [""*i for i in range(len(board[0]))]
    count = len(board)
    while count != 0:
        for i in range(count):
            new_board[-count] += board[i][-count]
        count -= 1
    count1 = len(board[0]) - 1
    while count1 != 0:
        new_board[-count1-1] += board[count1][-count1:]
        count1 -= 1
    return row_check(new_board)


def validate_board(board: list) -> bool:
    """
    Check whether the playing field of the logic puzzle is ready to start the game
    >>> validate_board(["**** ***.","***1 **.*","**  3*.**","* 4 1.***",\
"    .9 5 "," 6 .83  *","3 . 1  **"," .8  2***",". 2  ****"])
    False
    """
    if row_check(board) and column_check(board) and block_check(board):
        return True
    return False

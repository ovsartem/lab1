"""
skyscrappers
"""


def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> print("hello")
    hello
    """
    with open(path) as data:
        contents = data.readlines()
    return [i.strip() for i in contents]


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    new_line = input_line[1:-1]
    count = 0
    curr_max = '0'
    for height in new_line:
        if height > curr_max:
            count += 1
            curr_max = height
    if count == pivot:
        return True
    return False


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5',\
'*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215',\
'*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215',\
'*35214*', '*41532*', '*2*1***'])
    False
    """
    count = 0
    for i in range(len(board)):
        if "?" in board[i]:
            count += 1
    if count == 0:
        return True
    else:
        return False


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215',\
'*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215',\
'*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215',\
'*35214*', '*41532*', '*2*1***'])
    False
    """
    count = 0
    edited = [i.replace("*", "").replace("", " ") for i in board]
    for i in range(1, len(board)-1):
        board[i] = board[i][1:-1]
        if len(board[i]) != len(set(board[i])):
            count += 1
    if count == 0:
        return True
    else:
        return False
    return edited


def line_conf(line):
    counter = 0
    count = 0
    if line[0] != "*":
        left_pivot = int(line[0])
    if line[-1] != "*":
        right_pivot = int(line[-1])
    for_left = line[1:-1]
    for_right = for_left[::-1]

    curr_max = '0'

    # left_to_right
    if line[0] != "*":
        for height in for_left:
            if height > curr_max:
                count += 1
                curr_max = height

        if count != left_pivot:
            counter += 1
    # right to left
    count1 = 0
    curr_max1 = '0'
    if line[-1] != "*":
        for height in for_right:
            if height > curr_max1:
                count1 += 1
                curr_max1 = height
        if count1 != right_pivot:
            counter += 1
    return counter == 0


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)
    Return True if all horizontal hints are satisfiable,
    i.e., for line 412453* , hint is 4, and 1245 are the four buildings
    that could be observed from the hint looking to the right.
    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215',\
'*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215',\
'*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215',\
'*35214*', '*41532*', '*2*1***'])
    False
    """
    for i in range(1, len(board) - 1):
        if line_conf(board[i]) == False:
            return False
    return True


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height)
    and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*',\
'*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*',\
'*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*',\
'*41532*', '*2*1***'])
    False
    """
    idx = 0
    edited = ["" for i in range(len(board))]
    while idx != len(board):
        for i in range(len(board[0])):
            edited[idx] += board[i][idx]
        idx += 1
    return check_horizontal_visibility(edited) and check_uniqueness_in_rows(edited)


def check_skyscrapers(input_path: str) -> bool:
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    >>> print("hello")
    hello
    """
    if check_not_finished_board(input_path)\
            and check_uniqueness_in_rows(input_path)\
            and check_horizontal_visibility(input_path)\
            and check_columns(input_path):
        return True
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()

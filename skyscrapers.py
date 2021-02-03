"""
skyscrappers
"""


def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("check.txt")
    ['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """
    with open(path) as f:
        contents = f.readlines()
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
    count = 0
    for i in range(0, pivot):
        if int(input_line[pivot]) <= int(input_line[i]):
            count += 1
    if count == 0:
        return True
    return False


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*', '*41532*', '*2*1***'])
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

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', '*35214*', '*41532*', '*2*1***'])
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


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)
    Return True if all horizontal hints are satisfiable,
    i.e., for line 412453* , hint is 4, and 1245 are the four buildings
    that could be observed from the hint looking to the right.
    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for idx, line in enumerate(board):
        if idx != 0 and line[0] != '*':
            count_towers = int(line[0])

            last_biggest = 0
            count_seen = 0
            for ind in range(1, len(line)):
                if line[ind] != '*' and int(line[ind]) > last_biggest:
                    last_biggest = int(line[ind])
                    count_seen += 1

            if count_towers != count_seen:
                return False

    return True


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    idx = 0
    edited = [""*i for i in range(len(board))]
    while idx != len(board):
        for i in range(len(board[0])):
            edited[idx] += board[i][idx]
        idx += 1
    return check_uniqueness_in_rows(edited)


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    >>> check_skyscrapers("check.txt")
    True
    """
    if check_not_finished_board(read_input(input_path)) and check_uniqueness_in_rows(read_input(input_path))\
            and check_horizontal_visibility(read_input(input_path)) and check_columns(read_input(input_path)):
        return True
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()

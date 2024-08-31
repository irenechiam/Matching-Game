#Part 1: Pretty Print
def pretty_print(board):
    """Creating a table with its index in the top and left side of the grid. 
       The input, which is the nested lists, would be printed as a grid"""
    num_row = len(board)
    num_col = len(board[0])

    # Creating a grid without indexes
    grid = []
    for x in range(num_row):
        grid.append([])
        for y in range(num_col):
            grid[x].append(f'{board[x][y]:<3}')   
    
    # Creating the top index 
    col_index = []
    for col in range(num_col):
        col_index.append(f'{col:<3}')
    col_index = (''.join(col_index))
    print('   ' + col_index)
   
    # Making a line of -
    print(' ' * 3 + '-' * (num_col * 3))

    # Creating rows and show the grid
    for row in range(num_row):
        row_list = (''.join(grid[row]))
        print(f'{row:>2}' + '|' + row_list)
    print()

#Part 2: Validate Input 
DIR_UP = "u"
DIR_DOWN = "d"
DIR_LEFT = "l"
DIR_RIGHT = "r"
BLANK_PIECE = "Z"

def validate_input(board, position, direction):
    '''Validating whether the input board, position and direction follows the 
        6 rules below and returns True if they follow, or False if otherwise'''
    num_row = len(board)
    num_col = len(board[0])
    # 2 or more columns and rows validation 
    if num_row < 2 and num_col < 2:
        return False
    
    # each row has the same length
    for row in range(num_row):
        if len(board[row]) == num_col:
            continue
        else:
            return False 
        
    # Every board value is capital (.isupper())
    for row in range(num_row):
        for col in range(num_col):
            if board[row][col].isupper():
                continue 
            else:
                return False 
    
    # The position has to be in the board and no - row or column value 
    if (position[0] > num_row or position[0] < 0 and position[1] > num_col 
        or position[1] < 0):
        return False
    
    # The direction contains one of permitted directions
    if direction not in 'udlr':
        return False 
    
    # Number of each color has to be multiple of 4
    tally = {}
    for row_list in board:
        for letter in row_list:
            if letter in tally:
                tally[letter] += 1 
            else:
                tally[letter] = 1
    for (letter, num) in tally.items():
        if num % 4 == 0:
            continue
        else:
            return False 
    return True 

#Part 3: Legal Moves 
DIR_UP = "u"
DIR_DOWN = "d"
DIR_LEFT = "l"
DIR_RIGHT = "r"
BLANK_PIECE = "Z"

def get_second_position(board, position, direction):
    '''Getting the row and col value of the second position, 
        by using the input position and direction and returns another set of 
        row and col value'''
    row, col = position
    if direction == DIR_UP:
        pos = row - 1, col
    elif direction == DIR_DOWN:
        pos = row + 1, col
    elif direction == DIR_LEFT:
        pos = row, col - 1
    elif direction == DIR_RIGHT:
        pos = row, col + 1
    return pos

def get_adjacent_pos(board, position, direction):
    '''Makes a list of all of the adjacent set of row and col values, using the
        position value and direction'''
    row, col = position
    top_val = row - 1, col
    down_val = row + 1, col
    left_val = row, col - 1
    right_val = row, col + 1
    
    if direction == DIR_UP:
        adj_pos = [top_val, left_val, right_val]
    elif direction == DIR_DOWN:
        adj_pos = [down_val, left_val, right_val]
    elif direction == DIR_LEFT:
        adj_pos = [left_val, top_val, down_val]
    elif direction == DIR_RIGHT:
        adj_pos = [right_val, top_val, down_val]
    return adj_pos

def check_pos(board, position):
    '''Checking whether the input position is inside the board and returns a 
        boolean value '''
    num_row = len(board) - 1
    num_col = len(board[0]) - 1
    row, col = position
    if row < 0 or row > num_row or col < 0 or col > num_col:
        return False 
    else: 
        return True 
    
def check(board, position1, position2):
    '''To check if both pieces are in the board, using the row and col values of
        both pieces and output a boolean value'''
    num_row = len(board) - 1
    num_col = len(board[0]) - 1
    row, col = position1
    row2, col2 = position2
    if (row < 0 or row > num_row or col < 0 or col > num_col or row2 < 0 
        or row2 > num_row or col2 < 0 or col2 > num_col):
        return False
    else:
        return True 
    
def new_board(board, position1, position2):
    '''Creating a new board with the swapped pieces, with both row and col 
        values of both pieces and returns the new board '''
    row, col=  position1
    row2, col2 = position2
    board[row][col], board[row2][col2] = board[row2][col2], board[row][col]
    return board 

def check_color(board, position1, position2, direction):
    '''Getting all the adjacent set of row and col values of buth positions and 
        comparing whether they are the same color'''
    row, col = position1
    row2, col2 = position2
    
    if direction == DIR_UP:
        adj_pos1 = get_adjacent_pos(board, position1, DIR_UP)
        adj_pos2 = get_adjacent_pos(board, position2, DIR_DOWN)
    elif direction == DIR_DOWN:
        adj_pos1 = get_adjacent_pos(board, position1, DIR_DOWN)
        adj_pos2 = get_adjacent_pos(board, position2, DIR_UP)
    elif direction == DIR_LEFT:
        adj_pos1 = get_adjacent_pos(board, position1, DIR_LEFT)
        adj_pos2 = get_adjacent_pos(board, position2, DIR_RIGHT)
    elif direction == DIR_RIGHT:
        adj_pos1 = get_adjacent_pos(board, position1, DIR_RIGHT)
        adj_pos2 = get_adjacent_pos(board, position2, DIR_LEFT)
    
    # Checking whether the 3 adjacent colors are the same color as position 
    for neighbour in adj_pos1:
        n_row, n_col = neighbour
        if not check_pos(board, neighbour):
            continue 
        if board[n_row][n_col] == board[row][col]:
            return True
        
    for neighbour2 in adj_pos2:
        n_row2, n_col2 = neighbour2
        if not check_pos(board, neighbour2):
            continue 
        if board[n_row2][n_col2] == board[row2][col2]:
            return True       
    return False
 
def legal_move(board, position, direction):
    '''Returns True if the 2 pieces are in the board and at least one of pieces 
        have a same adjacent color, Returns False if otherwise'''
    row, col = position
    position2 = get_second_position(board, position, direction)
    row2, col2 = position2
    in_board = check(board, position, position2)
    if in_board:
        if board[row][col] == 'Z' or board[row2][col2] == 'Z':
            return False 
        board = new_board(board, position, position2) 
        return check_color(board, position2, position, direction)
    else:
        return False 
    
#Part 4: Make Move
DIR_UP = "u"
DIR_DOWN = "d"
DIR_LEFT = "l"
DIR_RIGHT = "r"
BLANK_PIECE = "Z"

def get_second_position(board, position, direction):
    '''Getting the row and col value of the second position, 
        by using the input position and direction and returns another set of 
        row and col value'''
    row, col = position
    if direction == DIR_UP:
        return row - 1, col
    elif direction == DIR_DOWN:
        return row + 1, col
    elif direction == DIR_LEFT:
        return row, col - 1
    elif direction == DIR_RIGHT:
        return row, col + 1

def new_board(board, position1, position2):
    '''Creating a new board with the swapped pieces, with both row and col 
        values of both pieces and returns the new board '''
    row, col=  position1
    row2, col2 = position2
    board[row][col], board[row2][col2] = board[row2][col2], board[row][col]
    return board 

def change_board(board): 
    '''Check whether there is a 2x2 square of the same color, replace it with 
        'Z' and shift the arrangements up and left using the input board and 
        returns a new board'''
    num_row = len(board) - 1
    num_col = len(board[0]) - 1
    for row in range(num_row):
        for col in range(num_col):
            if (board[row][col] == board[row][col + 1] == board[row + 1][col]
               == board[row + 1][col + 1]):
                board[row][col] = 'Z'
                board[row][col + 1] = 'Z'
                board[row + 1][col] = 'Z'
                board[row + 1][col + 1] = 'Z'
                board = shift_up(board)
                board = shift_left(board)
            else:
                continue 
    return board 

def shift_up(board):
    '''Shifts the arrangements upwards if there is a 'Z' on top of the current 
        color with the input board and returns a new board with all elements 
        shifted upwards'''
    num_row = len(board) - 1
    num_col = len(board[0]) 
    
    # The loop starts at the largest index, so we loop from bottom to top
    for row in range(num_row, 0, -1):
        for col in range(num_col):
            if board[row - 1][col] == 'Z':
                board[row][col], board[row - 1][col] = board[row - 1][col], \
                    board[row][col]
    return board 

def shift_left(board):
    '''Shifts the arrangements to the left if there is a 'Z' on the left of 
        the current color with the input board and returns a new board with all 
        elements shifted to the left'''
    num_row = len(board)
    num_col = len(board[0]) - 1
    
    # The loops starts from the first row and the last col
    for row in range(num_row):
        for col in range(num_col, 0, -1):
            if board[row][col - 1] == 'Z':
                board[row][col], board[row][col - 1] = board[row][col - 1], \
                    board[row][col]
    return board

def make_move(board, position, direction):
    '''Returns the new board after the direction is taken place at position, 
        eliminates any 2x2 square(s) of the same color shifts the elements 
        upwards and to the left'''
        
    row, col = position
    position2 = get_second_position(board, position, direction)
    board = new_board(board, position, position2)
    board = change_board(board)
    return board
    

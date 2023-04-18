import math
import sys
import heapq

# Helper functions to aid in your implementation. Can edit/remove
#############################################################################
######## Piece
#############################################################################
class Piece:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name



class King(Piece):
    name = "King"

    def __init__(self, x, y):
        super().__init__(x,y,self.name)

    
    '''
    Takes in a State object, checks the possible moves the King can take
    and checks if the coordinate at that grid is walkable ( >0 )
    Then returns list possible action outcomes (x,y) from this state
    @Returns list of tuple of numbers (x,y)

    '''
    def actions(self, grid, rows, cols, other_piece_locations):
        acts = []
        x = self.x
        y = self.y

        
        #Gets possible locations, given the board limits and obstacles 
        #(Does not remove locations with pieces or threatened locations)
        #NorthWest
        if x-1 >= 0 and y-1 >= 0: #e.g this checks board limits
            if grid[x-1][y-1] > 0: #this checks if its not an obstacle 
                acts.append((x-1,y-1))

        #North
        if x-1 >= 0:
            if grid[x-1][y] > 0:
                acts.append((x-1, y))

        #NorthEast
        if x-1 >= 0 and y+1 < cols:
            if grid[x-1][y+1] > 0:
                acts.append((x-1, y+1))

        #West
        if y-1 >= 0:
            if grid[x][y-1] > 0:
                acts.append((x, y-1))

        #East
        if y+1 < cols:
            if grid[x][y+1] > 0:
                acts.append((x, y+1))
                
        #SouthWest
        if x+1 < rows and y-1 >= 0:
            if grid[x+1][y-1] > 0:
                acts.append((x+1, y-1))

        #South
        if x+1 < rows:
            if grid[x+1][y] > 0:
                acts.append((x+1, y))

        #SouthEast
        if x+1 < rows and y+1 < cols:
            if grid[x+1][y+1] > 0:
                acts.append((x+1,y+1))

        #Only here we remove locations which are occupied by other pieces
        #Remove actions which step on other-piece locations
        for each in acts:
            if each in other_piece_locations:
                acts.remove(each)
        
        return acts


class Knight(Piece):
    name = "Knight"

    def __init__(self, x, y):
        super().__init__(x,y ,self.name)

    '''
    Returns a list of action locations, which the knight can move to from its current location,
    that are unoccupied by any other pieces and not an obstacle
    This also works to find out the threat locations of a piece
    '''
    def actions(self, grid, rows, cols, other_piece_locations):
        acts = []
        x = self.x
        y = self.y

        #|-
        #|
        if y+1 < cols and x-2 >= 0:
            if grid[x-2][y+1] > 0:
                acts.append((x-2, y+1))
            

        #---
        #|
        if y+2 < cols and x-1 >= 0:
            if grid[x-1][y+2] > 0:
                acts.append((x-1, y+2))

        #|
        #---
        
        if y+2 < cols and x+1 < rows:
            if grid[x+1][y+2] > 0:
                acts.append((x+1, y+2))


        #|
        #|-
        if y+1 < cols and x+2 < rows:
            if grid[x+2][y+1] > 0:
                acts.append((x+2, y+1))

        # |
        #-|
        if y-1 >= 0 and x+2 < rows:
            if grid[x+2][y-1] > 0:
                acts.append((x+2, y-1))

        #   |
        #---
        if y-2 >= 0 and x+1 < rows:
            if grid[x+1][y-2] > 0:
                acts.append((x+1, y-2))


        #-|
        # |
        if y-1 >= 0 and x-2 >= 0:
            if grid[x-2][y-1] > 0:
                acts.append((x-2, y-1))
            

        #---
        #|
        if y-2 >= 0 and x-1 >= 0:
            if grid[x-1][y-2] > 0:
                acts.append((x-1, y-2))

        #Remove actions which step on other-piece locations
        for each in acts:
            if each in other_piece_locations:
                acts.remove(each)

        return acts

class Rook(Piece):
    name = "Rook"

    #Lists the possible moves, specifically changes in the x,y directions (reference pt top left of board)
    # the numbers correspond to the limit of how much the direction val can be changed
    #e.g queen will then be able to move the entire board

    #Rook movement
    #       ^
    #       |
    #  <--- R --->
    #       |
    #       v


    def __init__(self, x, y):
        super().__init__(x,y ,self.name)

    
        '''
    Takes in a State object, checks the possible moves the King can take
    and checks if the coordinate at that grid is walkable ( >0 )
    Then returns list possible action outcomes (x,y) from this state
    @Returns list of tuple of numbers (x,y)

    '''
    def actions(self, grid, rows, cols, other_piece_locations):
        acts = []
        x = self.x
        y = self.y

        #North
        x_avail = x
        for i in range(1, x_avail+1):
            if grid[x-i][y] > 0 and (x-i, y) not in other_piece_locations:
                #if the spot is movable -> no obstacle and no piece blocking
                acts.append((x-i,y))
            else:
                #we have to break here due to obstacle or piece block
                break

        #East
        y_avail = cols - y - 1
        for i in range(1, y_avail+1):
            if grid[x][y+i] > 0 and (x, y+i) not in other_piece_locations:
                #if the spot is movable -> no obstacle and no piece blocking
                acts.append((x,y+i))
            else:
                #we have to break here due to obstacle or piece block
                break

        #South
        x_avail = rows - x - 1
        for i in range(1, x_avail+1):
            if grid[x+i][y] > 0 and (x+i, y) not in other_piece_locations:
                #if the spot is movable -> no obstacle and no piece blocking
                acts.append((x+i,y))
            else:
                #we have to break here due to obstacle or piece block
                break


        #West
        y_avail = y
        for i in range(1, y_avail+1):
            if grid[x][y-i] > 0 and (x, y-i) not in other_piece_locations:
                #if the spot is movable -> no obstacle and no piece blocking
                acts.append((x,y-i))
            else:
                #we have to break here due to obstacle or piece block
                break

        #(redundant)
        #Remove actions which step on other-piece locations
        # for each in acts:
        #     if each in other_piece_locations:
        #         acts.remove(each)
        
        return acts

class Bishop(Piece):
    name = "Bishop"

    #Lists the possible moves, specifically changes in the x,y directions (reference pt top left of board)
    # the numbers correspond to the limit of how much the direction val can be changed
    #e.g queen will then be able to move the entire board

    #Bishop movement
    #   ^       ^
    #    \     /
    #       R
    #    /     \
    #   v       v


    def __init__(self, x, y):
        super().__init__(x,y,self.name)

    
    '''
    Takes in a State object, checks the possible moves the King can take
    and checks if the coordinate at that grid is walkable ( >0 )
    Then returns list possible action outcomes (x,y) from this state
    @Returns list of tuple of numbers (x,y)

    '''
    def actions(self, grid, rows, cols, other_piece_locations):
        acts = []
        x = self.x
        y = self.y


        #NorthWest
        x_avail = x
        y_avail = y
        while x_avail - 1 >= 0 and y_avail - 1 >= 0:
            if grid[x_avail-1][y_avail-1] > 0 and ((x_avail-1, y_avail-1) not in other_piece_locations):
                #if the spot is movable -> no obstacle and no piece blocking
                acts.append((x_avail-1, y_avail-1))
                x_avail -= 1
                y_avail -= 1
            else:
                break

        
        #NorthEast
        x_avail = x
        y_avail = y
        while x_avail - 1 >= 0 and y_avail + 1 < cols:
            if grid[x_avail-1][y_avail+1] > 0 and ((x_avail-1, y_avail+1) not in other_piece_locations):
                #if the spot is movable -> no obstacle and no piece blocking
                
                acts.append((x_avail-1, y_avail+1))



                x_avail -= 1
                y_avail += 1
            else:
                break


        #SouthEast
        x_avail = x
        y_avail = y
        while x_avail + 1 < rows and y_avail + 1 < cols:
            if grid[x_avail+1][y_avail+1] > 0 and ((x_avail+1, y_avail+1) not in other_piece_locations):
                #if the spot is movable -> no obstacle and no piece blocking
                acts.append((x_avail+1,y_avail+1))
                x_avail += 1
                y_avail += 1
            else:
                break

        
        #SouthWest
        x_avail = x
        y_avail = y
        while x_avail + 1 < rows and y_avail - 1 >= 0:
            if grid[x_avail+1][y_avail-1] > 0 and ((x_avail+1, y_avail-1) not in other_piece_locations):
                #if the spot is movable -> no obstacle and no piece blocking
                acts.append((x_avail+1, y_avail-1))
                x_avail += 1
                y_avail -= 1
            else:
                break


        #(redundant)
        #Remove actions which step on other-piece locations
        # for each in acts:
        #     if each in other_piece_locations:
        #         acts.remove(each)
        
        return acts

class Queen(Piece):
    name = "Queen"
    def __init__(self, x, y):
        super().__init__(x,y,self.name)
        self.bishop_part = Bishop(x,y)
        self.rook_part = Rook(x,y)

    def actions(self, grid, rows, cols, other_piece_locations):
        acts = []
        acts.extend(self.bishop_part.actions(grid, rows, cols, other_piece_locations))
        acts.extend(self.rook_part.actions(grid, rows, cols, other_piece_locations))
        return acts

class Ferz(Piece):
    name = "Ferz"
    def __init__(self, x, y):
        super().__init__(x,y,self.name)


    '''
    Takes in a State object, checks the possible moves the King can take
    and checks if the coordinate at that grid is walkable ( >0 )
    Then returns list possible action outcomes (x,y) from this state
    @Returns list of tuple of numbers (x,y)

    '''
    def actions(self, grid, rows, cols, other_piece_locations):
        acts = []
        x = self.x
        y = self.y

        
        #NorthWest
        if x-1 >= 0 and y-1 >= 0:
            if grid[x-1][y-1] > 0:
                acts.append((x-1,y-1))

        #NorthEast
        if x-1 >= 0 and y+1 < cols:
            if grid[x-1][y+1] > 0:
                acts.append((x-1, y+1))

        
        #SouthWest
        if x+1 < rows and y-1 >= 0:
            if grid[x+1][y-1] > 0:
                acts.append((x+1, y-1))


        #SouthEast
        if x+1 < rows and y+1 < cols:
            if grid[x+1][y+1] > 0:
                acts.append((x+1,y+1))

        #Remove actions which step on other-piece locations
        for each in acts:
            if each in other_piece_locations:
                acts.remove(each)
        
        return acts

class Princess(Piece):
    name = "Princess"
    def __init__(self, x, y):
        super().__init__(x,y,self.name)
        self.bishop_part = Bishop(x,y)
        self.knight_part = Knight(x,y)

    def actions(self, grid, rows, cols, other_piece_locations):
        acts = []
        acts.extend(self.bishop_part.actions(grid, rows, cols, other_piece_locations))
        acts.extend(self.knight_part.actions(grid, rows, cols, other_piece_locations))
        return acts

class Empress(Piece):
    name = "Empress"
    def __init__(self, x, y):
        super().__init__(x,y,self.name)
        self.rook_part = Rook(x,y)
        self.knight_part = Knight(x,y)

    def actions(self, grid, rows, cols, other_piece_locations):
        acts = []
        acts.extend(self.rook_part.actions(grid, rows, cols, other_piece_locations))
        acts.extend(self.knight_part.actions(grid, rows, cols, other_piece_locations))
        return acts




#############################################################################
######## Board
#############################################################################
class Board:
    enemy_pieces = []
    enemy_locations = []
    
    def __init__(self, rows, cols, grid, goals, enemies):
        self.rows = rows
        self.cols = cols
        self.grid = grid
        self.goals = goals
        

        
        #Add and create enemy pieces to board
        for each in enemies:
            self.enemy_pieces.append(create_piece(each))
            self.enemy_locations.append(each[1])
    

    def is_goal(self, x,y): #state ADT: (x,y)
        if (x,y) in self.goals:
            return True
        else:
            return False

    '''
    Gets all of the threatened locations based on the pieces added
    Will not be accurate if no pieces added to the board.pieces yet
    '''
    def get_threatened_locations(self):
        threatened_locations = []
        for piece in self.enemy_pieces:
            #Get available actions of each piece, given that they know
            #where all the other pieces are.
            threatened_locations.extend(
                piece.actions(self.grid, self.rows, self.cols, self.enemy_locations))
            
        
        return threatened_locations 
    
 

#############################################################################
######## State
#############################################################################
class State:
    
    #State should be representing King's position
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost
        
    
    def get_state_format(self):
        #change back to x,y
        return (col_to_txt(self.y), (self.x))
    
    def get_state_number_format(self):
        return ((self.x), (self.y))
    



class Node:
    count = 0
    def __init__(self, state, prev):
        self.state = state
        self.previous_node = prev
        self.id = Node.count
        Node.count += 1

        if prev:
            self.path_cost = state.cost + prev.path_cost
        else:
            self.path_cost = 0
    
    '''
    Returns the position of the state
    '''
    def get_state_position_formatted(self):
        return self.state.get_state_format()
    
    def get_state_number_formatted(self):
        return self.state.get_state_number_format()

    def __str__(self) -> str:
        return str(self.get_state_position_formatted())
    
    def __lt__(self, node_1):
        return self.id < node_1.id

    def __le__(self, node_1):
        return self.id < node_1.id or node_1.id == self.id
    
    
########################## Helper Functions ############

'''
Creates an instance of a piece and returns it. 
Returns None if no such piece fits the description
'''
def create_piece(piece):
    piece_desc, location = piece[0], piece[1]
    ### THERE IS BUG WITH XY VALUES PLS RECHECK GRID AND ETC
    if piece_desc == "King":
        return King(x = location[0], y = location[1])
    elif piece_desc == "Rook":
        return Rook(x = location[0], y = location[1])
    elif piece_desc == "Bishop":
        return Bishop(x = location[0], y = location[1])
    elif piece_desc == "Queen":
        return Queen(x = location[0], y = location[1])
    elif piece_desc == "Knight":
        return Knight(x = location[0], y = location[1])
    elif piece_desc == "Ferz":
        return Ferz(x = location[0], y = location[1])
    elif piece_desc == "Princess":
        return Princess(x = location[0], y = location[1])
    elif piece_desc == "Empress":
        return Empress(x = location[0], y = location[1])   
    
    else:
        return None


'''
Returns String of x val, i.e the column label of a x-axis index
'''
def col_to_txt(x):
    return str(chr(ord("a") + x))

'''
Return coordinates in grid row,col 
'''
def txt_to_col(coord_tup):
    
    (r, c) = (coord_tup[1], ord(coord_tup[0]) - 97)
    return (r,c)




'''
Return paths in grid row,col format. Used more for printing
'''
def paths_r_c(paths):
    new_paths = []
    for each in paths:
        new_paths.append(txt_to_col(each[0]))
    
    return new_paths


'''
Returns the path walked to get to this node
'''
def get_path(node): #Node ADT: -state: x,y -previous_node
    path = []
    current = node
    
    #Maybe can speed this up
    while current.previous_node:
        move_list = [0,0]
        # move_list.insert(0, current.get_state_position_formatted())
        move_list[1] = (col_to_txt(current.state.y), (current.state.x))
        current = current.previous_node
        move_list[0] = (col_to_txt(current.state.y), (current.state.x))
        path.insert(0, move_list)
    
    return path


'''
Specific to King. Takes in a State object, checks the possible moves the King can take
and checks if the coordinate at that grid is walkable ( >0 )
Then returns list possible action outcomes (x,y) from this state
@Returns list of tuple of numbers (x,y)

'''
def actions(state, grid, rows, cols):
    acts = []
    x = state.x
    y = state.y

    #Moves of a king piece
    #This needs to check, based on the king location state, grid, and enemies, where the king cannot go to
    

    #NorthWest
    if x-1 >= 0 and y-1 >= 0:
        if grid[x-1][y-1] > 0:
            acts.append((x-1,y-1))

    #North
    if x-1 >= 0:
        if grid[x-1][y] > 0:
            acts.append((x-1, y))

    #NorthEast
    if x-1 >= 0 and y+1 < cols:
        if grid[x-1][y+1] > 0:
            acts.append((x-1, y+1))

    #West
    if y-1 >= 0:
        if grid[x][y-1] > 0:
            acts.append((x, y-1))

    #East
    if y+1 < cols:
        if grid[x][y+1] > 0:
            acts.append((x, y+1))
            
    #SouthWest
    if x+1 < rows and y-1 >= 0:
        if grid[x+1][y-1] > 0:
            acts.append((x+1, y-1))

    #South
    if x+1 < rows:
        if grid[x+1][y] > 0:
            acts.append((x+1, y))

    #SouthEast
    if x+1 < rows and y+1 < cols:
        if grid[x+1][y+1] > 0:
            acts.append((x+1,y+1))


    return acts
    

def h_n_nearest_goal(goals, state):
    
    x = state.x
    y = state.y
    newlist = map(lambda g : math.sqrt((g[0] - x)**2 + (g[1] - y)**2), goals)
    # print("newlist: ", list(newlist))
    return min(list(newlist))





#############################################################################
######## Implement Search Algorithm
#############################################################################
def search(rows, cols, grid, enemy_pieces, own_pieces, goals):
    new_board = Board(rows, cols, grid, goals, enemy_pieces)
    
    board_threat_locations = new_board.get_threatened_locations()
    board_enemy_locations = new_board.enemy_locations
    
    #Build a scan of the board, include places that cannot be traversed in this list of no-go zone
    no_go_zone = [] #to fill with threatened locations, locations of enemies, obstacle locations
    no_go_zone.extend(board_threat_locations)
    no_go_zone.extend(board_enemy_locations)

    
    #Creating and adding own pieces
    piece = own_pieces[0] #['King', (20, 0)]

    #Create a new King object
    first_king = create_piece(piece)

    # prin(first_king.x, first_king.y)
    #       row, col
    # pos actually is col->char , row
    
    #Define frontier
    frontier = []
    heapq.heapify(frontier)
    
    reached = {}

    #Create new source node, add it to frontier
    source_node = Node(State(first_king.x,first_king.y, 0), None)
    heapq.heappush(frontier,(source_node.state.cost,source_node))
    
    
    soln_path, opt_cost = [], 0
    while len(frontier) != 0:
        
        current = heapq.heappop(frontier)
        # print("Popped: ", (current[0],current[1]), current[2].id)
        
        #Check if the popped node has a goal state
        if (current[1].state.x, current[1].state.y) in new_board.goals:
            soln_path = get_path(current[1])      
            opt_cost = current[1].path_cost
            break

        #for each action in possible actions from current node
        #action is a tuple of numbers (x,y)
        
        for action in actions(current[1].state, grid, rows, cols):
            action_cost = grid[action[0]][action[1]]

            
            # #If action is available to go, and not in reached, or in reached but the path cost + action cost < pathcost of the previous state at reached
            if action not in no_go_zone and (((action) not in reached) or current[1].path_cost + action_cost < reached[action].path_cost ):
  
                #Create successor with new action
                successor = Node(State(action[0], action[1], action_cost), current[1])
                
                #A* f(n) = g(n) + h(n)

                #try h(n) as euclidean distance to nearest goal
                h_n_val = h_n_nearest_goal(goals, successor.state)
                f_n_val = successor.path_cost + h_n_val
                # f_n_val = successor.path_cost
                heapq.heappush(frontier,(f_n_val, successor))

                #Add successor node to the hashtable of reached
                reached[action] = successor
                
    # print("Explored and reached : ",len(reached))
    # print(soln_path, opt_cost)
       
    return soln_path, opt_cost


#############################################################################
######## Parser function and helper functions
#############################################################################
### DO NOT EDIT/REMOVE THE FUNCTION BELOW###
# Return number of rows, cols, grid containing obstacles and step costs of coordinates, enemy pieces, own piece, and goal positions
def parse(testcase):
    handle = open(testcase, "r")

    get_par = lambda x: x.split(":")[1]
    rows = int(get_par(handle.readline())) # Integer
    cols = int(get_par(handle.readline())) # Integer
    grid = [[1 for j in range(cols)] for i in range(rows)] # Dictionary, label empty spaces as 1 (Default Step Cost)
    enemy_pieces = [] # List
    own_pieces = [] # List
    goals = [] # List

    handle.readline()  # Ignore number of obstacles
    for ch_coord in get_par(handle.readline()).split():  # Init obstacles
        r, c = from_chess_coord(ch_coord)
        grid[r][c] = -1 # Label Obstacle as -1

    handle.readline()  # Ignore Step Cost header
    line = handle.readline()
    while line.startswith("["):
        line = line[1:-2].split(",")
        r, c = from_chess_coord(line[0])
        grid[r][c] = int(line[1]) if grid[r][c] == 1 else grid[r][c] #Reinitialize step cost for coordinates with different costs
        line = handle.readline()
    
    line = handle.readline() # Read Enemy Position
    while line.startswith("["):
        line = line[1:-2]
        piece = add_piece(line)
        enemy_pieces.append(piece)
        line = handle.readline()

    # Read Own King Position
    line = handle.readline()[1:-2]
    piece = add_piece(line)
    own_pieces.append(piece)

    # Read Goal Positions
    for ch_coord in get_par(handle.readline()).split():
        r, c = from_chess_coord(ch_coord)
        goals.append((r, c))
    
    return rows, cols, grid, enemy_pieces, own_pieces, goals

def add_piece( comma_seperated) -> Piece:
    piece, ch_coord = comma_seperated.split(",")
    r, c = from_chess_coord(ch_coord)
    return [piece, (r,c)]

def from_chess_coord( ch_coord):
    return (int(ch_coord[1:]), ord(ch_coord[0]) - 97)
    
### DO NOT EDIT/REMOVE THE FUNCTION HEADER BELOW###
# To return: List of moves and nodes explored
def run_AStar():
    testcase = sys.argv[1]
    rows, cols, grid, enemy_pieces, own_pieces, goals = parse(testcase)
    moves, pathcost = search(rows, cols, grid, enemy_pieces, own_pieces, goals)
    return moves, pathcost


# rows, cols, grid, enemy_pieces, own_pieces, goals = parse("3.txt")

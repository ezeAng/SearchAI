# LocalSearch
A project for CS3243 Introduction to Artificial Intelligence AY2022/2023 Semester 2
Local Search Project where a chess King moves towards a goal coordinate across a board with danger zones.

The 4 algorithms implemented are:
* Breath-First Search
* Depth-First Search
* Uniform Cost Search
* Astar Search 


The problem statement to be solved:
We are given a King chess piece in a game board of varying sizes and each board contains varying number of obstacles as well as enemy game pieces. The positions of the obstacles and enemy chess pieces are given in the input file and they remain static at all times (remain in the same position throughout the gameplay). The enemy chess pieces can threaten its surrounding positions based on the type of chess piece it is. This implies that our King piece cannot venture to the threatened positions due to the enemy chess pieces. Hence, our King piece is not allowed to move to these threatened positions.
Furthermore, our King’s aim is to escape the dungeon and not fight the guards. Hence, our King piece cannot capture (i.e., remove) other enemy pieces on the board and it cannot visit squares inhabited by other pieces (of course, including obstacles).
We are given the starting position of our King and the goal position(s) in the input file. To escape the dungeon, the King has to reach any of the goal position(s).
See the sample input txt files for more information.



In this project, we will create a one-player game variant that utilitises a re-sizable chess board and a subset of the chess pieces, whilst introducing new objectives, obstacles and new pieces to the game. Also, note that we will not be using the pawn1 piece in this project.

In the section below, the movement rules of each piece in the game is introduced. Note that we are only concerned with the movement of each piece and not any other complex rules (e.g., castling)
Game Pieces:

Classic Chess Pieces and Obstacle definition:
• King: The king can move one square in any direction.
• Rook: A rook can move any number of squares along a rank or file, but cannot leap over other pieces.
• Bishop: A bishop can move any number of squares diagonally, but cannot leap over other pieces.

• Queen: A queen combines the power of a rook and bishop and can move any number of squares along a rank, file, or diagonal, but cannot leap over other pieces.
• Knight: A knight moves to any of the closest squares that are not on the same rank, file, or diagonal (thus the move forms an ”L”-shape: two squares vertically and one square hori- zontally, or two squares horizontally and one square vertically). The knight is the only piece that can leap over other pieces.

Obstacle: An obstacle in the game has no moves and it takes up a square in the board. No other pieces can occupy the same position as the obstacle and they cannot leap over the obstacle (except the knight).

Fairy Chess Pieces:
• Ferz: The ferz is a fairy chess piece that may move one square diagonally.
• Princess: The princess is a fairy chess piece that can move like a bishop or a knight. It cannot jump over other pieces when moving as a bishop but may do so when moving as a knight.
• Empress: The empress is a fairy chess piece that can move like a rook or a knight. It cannot jump over other pieces when moving as a rook but may do so when moving as a knight.

Additionally, we introduce different costs on each square of the board. By default, a move to any square costs 1 unit. However, in this project, we may define different costs on different squares and hence moving to a square on the board may cost more than 1 unit.
Specifically, to define costs, each square on the board will be assigned a cost, c. For any move made to that square, that move would thus incur cost c.

Heuristics used:
UCS - path cost travelled
Astar - path cost + euclidean distance to goal



When the run BFS() [DFS() ... etc] function is executed will return a list of valid moves in the following format:
[move1, move2, move3, ..., movelast]
where movei is a list containing two tuples:[Current Position Tuple, Next Position Tuple] and in each position tuple, it will contain 2 elements (x,y) where x is the column index (i.e. a string) and y is the row index (i.e. an integer).
    More specifically, the list of moves should be returned in this format:
[[(x1, y1), (x2, y2)], [(x2, y2), (x3, y3)], ...[(xi, yi), (xj , yj )]]
An example of the function printed and its output is shown below:
print(run BFS())
Output:
[[(′a′, 0), (′b′, 0)], [(′b′, 0), (′c′, 0)], [(′c′, 0), (′d′, 0)], [(′d′, 0), (′e′, 1)], [(′e′, 1), (′d′, 2)]]


Note to user:
* To test the algorithm you may try using an input file and uncommenting the print commands (currently commented-out) in the files 

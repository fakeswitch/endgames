import chess.pgn
import json
# open pgn file as stream
pgn = open(r"C:\Users\George\Desktop\random_projects\chess projects\endgames\allgames_team4545_s1_s32.pgn")

# function to count how many pieces are on the board (from fen)
# takes a stirng fen as imput
# returns int number of pieces found in the fen 
def pieces_on_board(fen):
    pieces = ['p', 'r','n','b','q','k','P','R','N','B','Q', 'K']
    ori_count = len(fen)
    holder = fen
    for p in pieces: holder = holder.replace(p, '')
    return ori_count - len(holder)

# read first game 
first_game = chess.pgn.read_game(pgn)
count = 1
# create list to hold fens when less than or equal to 7 pieces

all_fens = []
# loop until no more games
# check every position of every game 
# save all positions where there are only 7 pieces on the board
while first_game is not None:
    # counter used to show progress of loop
    count += 1
    # set up board to play though the game from pgn
    board = first_game.board()
    WElo = first_game.headers['WhiteElo']
    BElo = first_game.headers['BlackElo']
    last_fen = None
    # run through every move of the game
    for move in first_game.mainline_moves():      
        #check to see if position has 7 or fewer pieces
        pob = pieces_on_board(board.fen())
        if pob <= 7:
            #add fen to list if criteria is met
            all_fens.append([last_fen, WElo, BElo, pob, str(move)])
        #make next move
        board.push(move)
        last_fen = board.fen()
    # read next game, sets up for next iteration of loop
    first_game = chess.pgn.read_game(pgn)
    # display progress of every 1000 games
    if count % 1000 == 0 : print(count) 


jstring = json.dumps(all_fens)
jsonFile = open(r"C:\Users\George\Desktop\random_projects\chess projects\endgames\7_piece_fen.json", "w")
jsonFile.write(jstring)
jsonFile.close()
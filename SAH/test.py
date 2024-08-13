import socket
from stockfish import Stockfish


#! ENGINE INITIALIZATION
STOCKFISH_PATH = "stockfish\stockfish-windows-x86-64-avx2.exe"

stockfish = Stockfish(path=STOCKFISH_PATH, depth=18, parameters={"Threads": 7, "Minimum Thinking Time": 8}) # 18 is the depth of the engine
stockfish.update_engine_parameters({"Hash": 2048})


def find_move_from_fens(stockfish, fen_start, fen_target):
    # Set the initial position
    stockfish.set_fen_position(fen_start)
    
    # Get all legal moves from the initial position
    legal_moves = stockfish.get_top_moves(5)
    
    # Iterate through all legal moves
    for move in legal_moves:
        # Make a temporary move
        stockfish.make_moves_from_current_position([move])
        
        # Check if the new FEN matches the target FEN
        if stockfish.get_fen_position() == fen_target:
            return move  # Return the move that leads to the target FEN
        
        # Reset to the initial position before trying the next move
        stockfish.set_fen_position(fen_start)
    
    return None  # Return None if no move leads to the target FEN

# Example usage
fen_start = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
fen_target = "rnbqkbnr/pppppppp/8/8/8/7P/PPPPPPP1/RNBQKBNR"
move = find_move_from_fens(stockfish, fen_start, fen_target)
if move:
    print(f"The move from the start FEN to the target FEN is: {move}")
else:
    print("No move found that leads to the target FEN.")
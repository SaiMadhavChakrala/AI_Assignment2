import chess
from evaluation_function import evaluate_board

def minimax(env, board, depth, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    legal_moves = list(env.legal_moves)
    best_move = None

    if maximizing_player:
        max_eval = float('-inf')
        for move in legal_moves:
            board.push(move)
            eval, _ = minimax(env, board, depth-1, False)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return max_eval, best_move

    else:
        min_eval = float('inf')
        for move in legal_moves:
            board.push(move)
            eval, _ = minimax(env, board, depth-1, True)
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
        return min_eval, best_move
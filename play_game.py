import gym
import gym_chess
import chess
import chess.svg
import cairosvg
import imageio
from minimax_agent import minimax
from alphabeta_agent import alphabeta
from PIL import Image
import io

def board_to_image(board):
    svg_data = chess.svg.board(board=board)
    png_data = cairosvg.svg2png(bytestring=svg_data)
    return Image.open(io.BytesIO(png_data))

def play_game(algorithm='minimax', depth=2, gif_name='game.gif'):
    env = gym.make('Chess-v0')
    env.reset()

    frames = []
    frames.append(board_to_image(env._board))  

    done = False

    while not done:
        board = env._board
        legal_moves = list(env.legal_moves)

        if algorithm == 'minimax':
            _, move = minimax(env, board, depth, board.turn)
        else:
            _, move = alphabeta(env, board, depth, float('-inf'), float('inf'), board.turn)

        if move not in legal_moves:
            print("No legal move found — random fallback.")
            move = legal_moves[0]

        state, reward, done, info = env.step(move)

        frames.append(board_to_image(env._board))
        # print("Move made. Reward:", reward)

    print("Game Over. Result:", env._board.result())
    env.close()

    frames[0].save(
        gif_name,
        save_all=True,
        append_images=frames[1:],
        duration=800, 
        loop=0
    )

    print(f"Saved game GIF as {gif_name}")

if __name__ == "__main__":
    print("Playing Minimax AI Game")
    play_game('minimax', 2, 'minimax_game.gif')

    print("\nPlaying Alpha-Beta AI Game")
    play_game('alphabeta', 2, 'alphabeta_game.gif')
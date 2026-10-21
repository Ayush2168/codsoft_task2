"""
CodSoft AI Internship - Task 2: Unbeatable Tic-Tac-Toe AI
Uses the Minimax algorithm with Alpha-Beta Pruning.
Human = 'X', AI = 'O'.
"""
import math

WIN_LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
             (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
             (0, 4, 8), (2, 4, 6)]              # diagonals
HUMAN, AI = "X", "O"


def winner(board):
    for a, b, c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_full(board):
    return " " not in board


def available_moves(board):
    return [i for i, v in enumerate(board) if v == " "]


def minimax(board, is_maximizing, alpha, beta, depth=0):
    """Return the score of `board` assuming optimal play.
    AI wins -> positive, human wins -> negative, draw -> 0.
    Depth is used so the AI prefers faster wins and slower losses."""
    w = winner(board)
    if w == AI:
        return 10 - depth
    if w == HUMAN:
        return depth - 10
    if is_full(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for m in available_moves(board):
            board[m] = AI
            best = max(best, minimax(board, False, alpha, beta, depth + 1))
            board[m] = " "
            alpha = max(alpha, best)
            if beta <= alpha:      # alpha-beta cut-off
                break
        return best
    else:
        best = math.inf
        for m in available_moves(board):
            board[m] = HUMAN
            best = min(best, minimax(board, True, alpha, beta, depth + 1))
            board[m] = " "
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best


def best_move(board):
    """Best move for the AI ('O') on the given board."""
    best_score, move = -math.inf, None
    for m in available_moves(board):
        board[m] = AI
        score = minimax(board, False, -math.inf, math.inf, 1)
        board[m] = " "
        if score > best_score:
            best_score, move = score, m
    return move


def print_board(board):
    print()
    for r in range(3):
        print(" " + " | ".join(board[r * 3:r * 3 + 3]))
        if r < 2:
            print("---+---+---")
    print()


def print_guide():
    print("Positions:")
    print(" 1 | 2 | 3\n---+---+---\n 4 | 5 | 6\n---+---+---\n 7 | 8 | 9")


def ask_human_move(board):
    while True:
        raw = input("Your move (1-9): ").strip()
        if raw.isdigit() and 1 <= int(raw) <= 9 and board[int(raw) - 1] == " ":
            return int(raw) - 1
        print("Invalid or occupied cell, try again.")


def play():
    print("=== Tic-Tac-Toe vs Unbeatable AI ===")
    print("You are X, the AI is O.")
    print_guide()
    board = [" "] * 9
    human_turn = input("Do you want to go first? (y/n): ").strip().lower() != "n"

    while True:
        if human_turn:
            board[ask_human_move(board)] = HUMAN
        else:
            print("AI is thinking...")
            board[best_move(board)] = AI
        print_board(board)

        w = winner(board)
        if w:
            print("You win!" if w == HUMAN else "AI wins! Better luck next time.")
            break
        if is_full(board):
            print("It's a draw!")
            break
        human_turn = not human_turn


if __name__ == "__main__":
    while True:
        play()
        if input("Play again? (y/n): ").strip().lower() != "y":
            print("Thanks for playing!")
            break

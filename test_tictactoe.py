"""Proves the AI is unbeatable: explores EVERY possible human strategy
and checks the human never wins."""
from tictactoe import *




def run(human_first):
    def rec(board, human_turn):
        w = winner(board)
        if w:
            return w != HUMAN
        if is_full(board):
            return True
        if human_turn:
            for m in available_moves(board):
                nb = board[:]; nb[m] = HUMAN
                if not rec(nb, False):
                    return False
            return True
        nb = board[:]; nb[best_move(nb)] = AI
        return rec(nb, True)
    return rec([" "] * 9, human_first)


def test_blocks_win():
    b = ["X", "X", " ", " ", "O", " ", " ", " ", " "]
    assert best_move(b) == 2

def test_takes_win():
    b = ["O", "O", " ", "X", "X", " ", " ", " ", " "]
    assert best_move(b) == 2

def test_unbeatable_human_first():
    assert run(True)

def test_unbeatable_ai_first():
    assert run(False)

if __name__ == "__main__":
    for n, f in list(globals().items()):
        if n.startswith("test_"):
            f(); print("PASS", n)

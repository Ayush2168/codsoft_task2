# CodSoft AI Internship – Task 2: Tic-Tac-Toe AI

Play Tic-Tac-Toe against an **unbeatable AI** built with the **Minimax algorithm
with Alpha-Beta Pruning**. You are `X`, the AI is `O`.

## Run
```bash
python tictactoe.py
```

## Test (proves the AI never loses)
```bash
python test_tictactoe.py
```
The test explores *every possible human move sequence* (both when you go first and
when the AI goes first) and checks that the human can never win.

## How it works
- **Minimax**: recursively simulates all future moves. AI (maximizer) picks the move
  with the highest score; the human (minimizer) is assumed to play perfectly.
- **Scores**: AI win = `10 - depth`, human win = `depth - 10`, draw = `0`
  (depth makes the AI prefer quick wins and slow losses).
- **Alpha-Beta Pruning**: skips branches that cannot change the final decision
  (`if beta <= alpha: break`), giving the same result faster.

#codsoft #AI #internship

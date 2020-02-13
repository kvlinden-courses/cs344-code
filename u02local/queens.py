"""
This implements a local-search version of N-Queens for AIMA-Python.
It copies AIMA's goal_test and conflict methods, modifying the others
to support a complete-state, value-maximization formulation.

@author: kvlinden
@version 19dec2012
"""
from search import Problem, hill_climbing, simulated_annealing, exp_schedule
import itertools
import math


class NQueens(Problem):
    """An implementation of NQueens for local search. This is a complete-state
    reformulation of the partial-state AIMA-Python version.

    State representation: 
        [q1, q2, ..., qn] gives the row for each of the n queens.
    Move representation: 
        [column, row]: Move the queen in the given column to the given row.
    """

    def __init__(self, n, initial):
        self.n = n
        self.initial = initial

    def actions(self, state):
        """Actions move the queen in each column to any of the other,
        unfilled row spots.
        """
        actions = []
        for column in range(self.n):
            for row in [x for x in range(self.n) if x != state[column]]:
                actions.append([column, row])
        return actions

    def result(self, state, move):
        """Makes the given move on a copy of the given state."""
        new_state = state[:]
        new_state[move[0]] = move[1]
        return new_state

    def goal_test(self, state):
        """Check to see if there are no conflicts."""
        return not any(self.conflicted(state, state[col], col)
                       for col in range(len(state)))

    def conflicted(self, state, row, col):
        """Check to see if placing a queen at (row, col) would conflict with
        anything.
        """
        return any(self.conflict(row, col, state[c], c)
                   for c in range(col))

    def conflict(self, row1, col1, row2, col2):
        """Check to see if two queens placed in (row1, col1) and (row2, col2)
        respectively would conflict with each other.
        """
        return (row1 == row2  # # same row
                or col1 == col2  # # same column
                or row1 - col1 == row2 - col2  # # same \ diagonal
                or row1 + col1 == row2 + col2)  # # same / diagonal

    def value(self, state):
        """This method computes a value of given state based on the number of
        conflicting pairs of queens. It doesn't follow AIMA-Python's NQueens
        gradient-descent formulation; instead, it counts the number of
        non-conflicting pairs (e.g., top score: 28 for a 8-queen problem;
        worst score: 0).
        """

        # Start with the highest possible score (n combined 2).
        value = math.factorial(self.n) / (2 * math.factorial(self.n - 2))

        # Loop through all pairs, subtracting one for every conflicted pair.
        for pair in itertools.combinations(range(self.n), 2):
            if self.conflict(state[pair[0]], pair[0], state[pair[1]], pair[1]):
                value -= 1
                
        return value


if __name__ == '__main__':

    # Set the board size.
    n = 8
    print('N:\t\t' + str(n))

    # Initialize the board with all queens in the first row.
    board = [0] * n
    print('Start:\t' + str(board))

    # Initialize the NQueens problem
    p = NQueens(n, board)
    print('Value:\t' + str(p.value(board)))

    # Solve the problem using hill climbing.
    hill_solution = hill_climbing(p)
    print('\nHill-climbing:')
    print('\tSolution:\t' + str(hill_solution))
    print('\tValue:\t\t' + str(p.value(hill_solution)))
    print('\tGoal?\t\t' + str(p.goal_test(hill_solution)))

    # Solve the problem using simulated annealing.
    annealing_solution = \
        simulated_annealing(p, exp_schedule(k=20, lam=0.005, limit=10000))
    print('\nSimulated annealing:')
    print('\tSolution:\t' + str(annealing_solution))
    print('\tValue:\t\t' + str(p.value(annealing_solution)))
    print('\tGoal?\t\t' + str(p.goal_test(annealing_solution)))

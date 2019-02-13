"""
This uses a pre-built problem specification for the
Zebra puzzle taken from AIMA's csp.py. See:

    https://en.wikipedia.org/wiki/Zebra_Puzzle

@author: kvlinden
@version 14feb2013
"""
import time

from tools.aima.csp import Zebra, min_conflicts, backtracking_search, AC3
from tools.aima.search import depth_first_graph_search

def print_solution(result):
    """A CSP solution printer copied from csp.py."""
    for h in range(1, 6):
        print('House', h)
        for (var, val) in result.items():
            if val == h: print('\t', var)
    

puzzle = Zebra()

# result = depth_first_graph_search(puzzle)
# result = AC3(puzzle)
result = backtracking_search(puzzle)
# result = min_conflicts(puzzle, max_steps=1000)

if puzzle.goal_test(puzzle.infer_assignment()):
    print("Solution:\n")
    print_solution(result)
else:
    print("failed...")
    print(puzzle.curr_domains)
    puzzle.display(puzzle.infer_assignment())

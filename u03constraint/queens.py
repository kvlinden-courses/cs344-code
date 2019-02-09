"""
Run the various CSP solvers on the nQueens problem.
These calls are mostly copied/adapted from AIMA Python.

@author: kvlinden
@version 14feb2013
"""

from tools.aima.csp import backtracking_search, NQueensCSP, min_conflicts, mrv, \
    forward_checking, AC3
from tools.aima.search import depth_first_graph_search
import logging

# 1. Set up the problem.
n = 4
problem = NQueensCSP(n)

# 2. Solve the problem.
# There is a bug in the DFS code (even for 1-queens), so skip this one.
# solution = depth_first_graph_search(problem)
solution = AC3(problem)
# solution = backtracking_search(problem)
# solution = min_conflicts(problem)

# 3. Print the results.  
# Handle AC3 solutions (boolean values) first, they behave differently.
if type(solution) is bool:
    if solution and problem.goal_test(problem.infer_assignment()):
        print('\nAC3 Solution:')
    else:
        print('\nAC Failure:')
    print('\t', problem.curr_domains)

# Handle other solutions next.
elif problem.goal_test(solution):
    print('\nSolution:', solution)
    problem.display(problem.infer_assignment())
else:
    print('\nFailed - domains: ' + str(problem.curr_domains))
    problem.display(problem.infer_assignment())



"""
This is an AIMA-Python-based solution for the 8-puzzle.

@author: kvlinden
@version 31jan2013
"""

from tools.aima.search import Problem, astar_search, Node, breadth_first_tree_search, \
    iterative_deepening_search
import logging
import time

class EightPuzzle(Problem):
    """This is a Problem sub-class that implements the traditional eights puzzle."""
    
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal
        
    def actions(self, state):
        actions = []
        open = state.find('0')
        if (open > 2):
            actions.append('u')
        if (open < 6):
            actions.append('d')
        if (open % 3 > 0):
            actions.append('l')
        if (open % 3 < 2):
            actions.append('r')
        logging.debug('\tactions:' + str(actions))
        return actions
    
    def result(self, state, action):
        i = state.find('0')
        logging.debug('\tmove:' + str(state) + " " + action)
        if action == 'u':
            return self.swap(state, i, i - 3)
        if action == 'd':
            return self.swap(state, i, i + 3)
        if action == 'l':
            return self.swap(state, i, i - 1)
        if action == 'r':
            return self.swap(state, i, i + 1)
    
    def goal_test(self, state):
        return state == self.goal
    
    def h(self, node):
        """This calls the chosen heuristic."""
        return self.h_manhattan_distance(node)
    
    def h_disabled(self, node):
        """This version of h() is disabled
        (but still admissible because it always underestimates everything).
        """
        return 0
    
    def h_mismatched_tiles(self, node):
        """This version of h() returns the number of mismatched tiles.
        Note that the space (0) is not a tile, so it won't be counted.
        """
        mismatches = 0
        for i in range(9):
            if node.state[i] != '0' and node.state[i] != self.goal[i]:
                mismatches += 1
        return mismatches

    def h_manhattan_distance(self, node):
        """This version of h() returns the sum of manhattan distances of each
        tile from its desired location.
        """
        distance = 0
        for i in range(1,9):
            target = self.goal.find(str(i))
            current = node.state.find(str(i))
            distance += abs((target % 3) - (current % 3)) + abs((target / 3) - (current / 3)) 
        return distance
    
    def swap(self, state, x, y):
        """This method swaps the value in the two given board coordinates."""
        result = state.replace(state[x], '*')
        result = result.replace(state[y], state[x])
        return result.replace('*', state[y])

def print_puzzle(state_string):
    for i in range(3):
        print(state_string[i * 3:i * 3 + 3])

if __name__ == '__main__':
    
    # logging.basicConfig(level=logging.DEBUG)
            
    goal_state = '012345678'
    # Trivial start state
    # initial_state = '012345678' # length 0 (no h(): 0; h(): 0; h'(): 0)
    # Worst-case start state
    # - length 31
    # - no h(): ??; h(): 4949.5; h'(): 134.2)
    # - See http://www.aiai.ed.ac.uk/~gwickler/eightpuzzle-inf.html
    initial_state = '806547231'

    p = EightPuzzle(initial_state, goal_state)

    time1 = time.time()
    solution = astar_search(p).solution()
    time2 = time.time()
    print(solution)
    print('length: ' + str(len(solution)))
    print('time: %0.3f seconds' % (time2 - time1))



'''
This is an AIMA-Python-based solution for the missionaries and cannibals problem.

@author: kvlinden
@version Dec 18, 2012
@version Spring, 2018 Ported to Python 3...
'''

from tools.aima.search import Problem, breadth_first_tree_search, depth_first_tree_search, depth_first_graph_search
import string

class Missionaries(Problem):
    '''
    state format: [missionaries on side 0, cannibals on side 0, M on side 1, C on side 1, boat location]
    action format: [missionaries to move, cannibals to move]
    '''
    
    def __init__(self):
        self.initial = self.state_to_string([3, 3, 0, 0, 0])
        self.goal = [0, 0, 3, 3, 1]
       
    def actions(self, state_string):
        state = self.string_to_state(state_string)
        actions = []
        for m in range(3):
            for c in range(3):
                new_move = [m, c]
                new_state = self.create_new_state(state, new_move)
                if new_state != None:
                    actions.append(new_move)
        return actions
    
    def result(self, state_string, move):
        state = self.string_to_state(state_string)
        return self.state_to_string(self.create_new_state(state, move))
    
    def goal_test(self, state_string):
        state = self.string_to_state(state_string)
        for i in range(len(state)):
            if state[i] != self.goal[i]:
                return False
        return True

    # There is likely a more clever way to solve this using index arithmetic.
    def create_new_state(self, state, move):
        '''This method creates a new state based on the current state and the given move. If no such move is possible,
        i.e., because there aren't enough missionaries or cannibals on the boat side to fill the move or if the resulting
        state is illegal, then return None.'''
        
        # The boat can carry from 1-2 people, no more, no less.
        if (move[0] + move[1] == 0) or (move[0] + move[1] > 2):
            return None
        
        # Make a new state for the move based on the location of the boat the availability of missionaries and cannibals on that side.
        # Note that the boat passenger mix is always legal because one group can't out-number the other.
        if (state[4] == 0) and (state[i] >= move[i] for i in range(2)):
            # The boat is on the left.
            return self.legal_state([state[0] - move[0], state[1] - move[1], state[2] + move[0], state[3] + move[1], 1])
        elif (state[i + 2] >= move[i] for i in range(2)):
            # The boat is on the right.
            return self.legal_state([state[0] + move[0], state[1] + move[1], state[2] - move[0], state[3] - move[1], 0])
        else:
            return None
        
    def legal_state(self, state):
        '''This method returns the state if the cannibals do not out-number the missionaries, None otherwise.'''
        if (state[0] >= state[1] or state[0] == 0) and (state[2] >= state[3] or state[2] == 0):
            return state
        else:
            return None
    
    # Utility functions that convert to and from hashable state representations
    def string_to_state(self, state_string):
        # In Python 3, map() returns a map object, not the list we need.
        # So, convert it to a list.
        return list(map(int, state_string.split(',')))
    def state_to_string(self, state):
        return ','.join(map(str, state))
        
        
p = Missionaries()
solution = breadth_first_tree_search(p).solution()
print(solution)
print("length: " + str(len(solution)))
    

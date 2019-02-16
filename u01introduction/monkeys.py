"""
This code is (mostly) copied from the GPS code by dhconnelly,
    https://github.com/dhconnelly/paip-python.

For the monkey/banana problem, see:
    https://en.wikipedia.org/wiki/Monkey_and_banana_problem

@author: kvlinden
@version 25jan2013
"""

from gps import gps


# Formulate the problem states and actions.
problem = {

    'initial': ['at door', 'on floor', 'has ball', 'hungry', 'chair at door'],
    'goal': ['not hungry'],

    'actions': [
        {
            'action': 'climb on chair',
            'preconds': ['chair at middle room', 'at middle room', 'on floor'],
            'add': ['at bananas', 'on chair'],
            'delete': ['at middle room', 'on floor']
        },
        {
            'action': 'push chair from door to middle room',
            'preconds': ['chair at door', 'at door'],
            'add': ['chair at middle room', 'at middle room'],
            'delete': ['chair at door', 'at door']
        },
        {
            'action': 'walk from door to middle room',
            'preconds': ['at door', 'on floor'],
            'add': ['at middle room'],
            'delete': ['at door']
        },
        {
            'action': 'grasp bananas',
            'preconds': ['at bananas', 'empty handed'],
            'add': ['has bananas'],
            'delete': ['empty handed']
        },
        {
            'action': 'drop ball',
            'preconds': ['has ball'],
            'add': ['empty handed'],
            'delete': ['has ball']
        },
        {
            'action': 'eat bananas',
            'preconds': ['has bananas'],
            'add': ['empty handed', 'not hungry'],
            'delete': ['has bananas', 'hungry']
        }
    ]
}

if __name__ == '__main__':

    # Use GPS to solve the problem formulated above.
    actionSequence = gps(
        problem['initial'],
        problem['goal'],
        problem['actions']
    )

    # Print the solution, if there is one.
    if actionSequence is not None:
        for action in actionSequence:
            print(action)
    else:
        print('plan failure...')

'''
This code is (mostly) copied from the GPS code by dhconnelly,
https://github.com/dhconnelly/paip-python.

@author: kvlinden
@version 25jan2013
'''

from tools.tools.paip.gps import gps

# Define the domain start state, goal states and operations.
start = ["at door", "on floor", "has ball", "hungry", "chair at door"]
goal = ["not hungry"]
operations = [
    {
        "action": "climb on chair",
        "preconds": ["chair at middle room", "at middle room", "on floor"],
        "add": ["at bananas", "on chair"],
        "delete": ["at middle room", "on floor"]
    },
    {
        "action": "push chair from door to middle room",
        "preconds": ["chair at door", "at door"],
        "add": ["chair at middle room", "at middle room"],
        "delete": ["chair at door", "at door"]
    },
    {
        "action": "walk from door to middle room",
        "preconds": ["at door", "on floor"],
        "add": ["at middle room"],
        "delete": ["at door"]
    },
    {
        "action": "grasp bananas",
        "preconds": ["at bananas", "empty handed"],
        "add": ["has bananas"],
        "delete": ["empty handed"]
    },
    {
        "action": "drop ball",
        "preconds": ["has ball"],
        "add": ["empty handed"],
        "delete": ["has ball"]
    },
    {
        "action": "eat bananas",
        "preconds": ["has bananas"],
        "add": ["empty handed", "not hungry"],
        "delete": ["has bananas", "hungry"]
    }
]

# Execute the monkeys and bananas problem and print the results.
for action in gps(start, goal, operations):
    print(action)

'''
This code uses the uninformed search algorithms from AIMA-Python to solve search problems in the Romanian domain.

@author: kvlinden
@version Dec 17, 2012
@version Spring, 2018 Ported to Python 3...
'''

from numpy import math

from tools.aima.search import UndirectedGraph, GraphProblem, depth_first_graph_search, \
    breadth_first_tree_search, uniform_cost_search, iterative_deepening_search, \
    astar_search, greedy_best_first_graph_search, best_first_graph_search
from tools.aima.utils import name, print_table


romania = UndirectedGraph(dict(
    arad=dict(zerind=75, sibiu=140, timisoara=118),
    bucharest=dict(urziceni=85, pitesti=101, giurgiu=90, fagaras=211),
    craiova=dict(dobreta=120, rimnicuvilcea=146, pitesti=138),
    dobreta=dict(mehadia=75),
    eforie=dict(hirsova=86),
    fagaras=dict(sibiu=99),
    hirsova=dict(urziceni=98),
    iasi=dict(vaslui=92, neamt=87),
    lugoj=dict(timisoara=111, mehadia=70),
    oradea=dict(zerind=71, sibiu=151),
    pitesti=dict(rimnicuvilcea=97),
    rimnicuvilcea=dict(sibiu=80),
    urziceni=dict(vaslui=142)))

romania.locations = dict(
    arad=(91, 492), 
    bucharest=(400, 327), 
    craiova=(253, 288), 
    dobreta=(165, 299),
    eforie=(562, 293), 
    fagaras=(305, 449), 
    giurgiu=(375, 270), 
    hirsova=(534, 350),
    iasi=(473, 506), 
    lugoj=(165, 379), 
    mehadia=(168, 339), 
    neamt=(406, 537),
    oradea=(131, 571), 
    pitesti=(320, 368), 
    rimnicuvilcea=(233, 410), 
    sibiu=(207, 457),
    timisoara=(94, 410), 
    urziceni=(456, 350), 
    vaslui=(509, 444), 
    zerind=(108, 531))

def compare_searchers(problem, searchers):
   def apply_search(problem, searcher):
       result = searcher(problem)
       return [name(searcher), str(result.solution()), str(result.path_cost)]
   print_table([apply_search(problem, s) for s in searchers])

algorithms = [
    depth_first_graph_search,
    breadth_first_tree_search,
    uniform_cost_search,
    iterative_deepening_search
]
compare_searchers(GraphProblem('arad', 'bucharest', romania), algorithms)


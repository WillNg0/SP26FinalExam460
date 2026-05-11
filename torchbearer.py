"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: William Ngo
Student ID:   130818451

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """
    ans = '''
    - A single shortest-path run from S is not enough because there are distinct locations where the Torchbearer must visit before going to the exit. The relic chamber order must be determined to acquire the least cost route.
    - After all the inter-location costs are known, the least fuel-cost route between relic chambers must be decided.
    - This requires a search over orders because the least-cost route must be determined among different valid relic chamber routes. 
    '''
    return ans


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """
    nodes = [spawn, exit_node]
    nodes.extend(relics)
    return nodes


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """
    dist = {}
    pq = []
    
    for v in graph:
        dist[v] = float('inf')
    dist[source] = 0

    heapq.heappush(pq, (0, source))

    while pq:
        cost, node = heapq.heappop(pq)

        if cost > dist[node]:
            continue

        for neighbor, c in graph[node]:
            if dist[node] + c < dist[neighbor]:
                dist[neighbor] = dist[node] + c
                heapq.heappush(pq, (dist[neighbor], neighbor))

    return dist


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """
    p_d = {}
    
    p_d[spawn] = run_dijkstra(graph, spawn)        

    for source in relics:
        p_d[source] = run_dijkstra(graph, source)

    p_d[exit_node] = run_dijkstra(graph, exit_node)

    return p_d



# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    ans = '''
    - For every node v that has already been finalized in S, dist[v] gives the least cost path from x to v and no better paths exist.
    - For the nodes u that have not been finalized in S, dist[u] gives the current least cost path from x to u based on the finalized nodes in S. 
    - Initialization: At the start, the source node is initialized with distance 0 and no other nodes have been processed yet, so their distances are initialized to infinity. 
    - Maintenance: The graph consists of nonnegative edge weights, meaning that a better path cannot be discovered after a path has been finalized with the minimum distance.
    - Termination: The shortest path from the source node to all reachable nodes have been discovered and finalized. 
    - Since Dijkstra produces the correct shortest distance from the source node, an optimal route can be decided by seeing which route produces the minimum cost among different valid routes. 
    '''
    return ans


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    ans = '''
    - The failure mode: Picking the cheapest next node available
    - Counter-example setup:
     | From \ To | B   | C   | D   | T   |
     |-----------|-----|-----|-----|-----|
     | S         | 2   | 3   | 1   | --  |
     | B         | --  | 1   | 100 | 2   |
     | C         | 3   | --  | 3   | 2   |
     | D         | 3   | 2   | --  | 100 |
    - What greedy picks: S -> D -> C -> B -> T \t total fuel = 1 + 2 + 3 + 2 = 8
    - What optimal picks: S -> D -> B -> C -> T \t total fuel = 1 + 3 + 1 + 2 = 7
    - Why greedy loses: Greedy chooses the cheapest option available, but does not consider how its decisions can affect later paths. Later paths can be cheaper than current cheapest path.
    - The algorithm must explore the order to visit the relic chambers that results in the minimum total fuel cost. 
    '''
    return ans


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    pass


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()

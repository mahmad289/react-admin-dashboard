# Pseudo code for Graph Traversal in Python
#
# This file contains pseudo code (not runnable) that describes the structure
# of a graph and the two most common traversal algorithms:
#   - Breadth-First Search (BFS)
#   - Depth-First Search (DFS), both iterative and recursive
#
# The graph is represented as an adjacency list:
#     graph = { node: [neighbor1, neighbor2, ...], ... }


# CLASS Graph
#     ATTRIBUTES:
#         adjacency   # dictionary mapping node -> list of neighbor nodes
#         directed    # boolean flag (True if directed, False if undirected)
#
#     FUNCTION __init__(directed = False):
#         SET self.adjacency = empty dictionary
#         SET self.directed = directed
#
#     FUNCTION add_node(node):
#         IF node NOT IN self.adjacency:
#             SET self.adjacency[node] = empty list
#
#     FUNCTION add_edge(u, v):
#         CALL self.add_node(u)
#         CALL self.add_node(v)
#         APPEND v TO self.adjacency[u]
#         IF NOT self.directed:
#             APPEND u TO self.adjacency[v]
#
#     FUNCTION neighbors(node):
#         IF node IN self.adjacency:
#             RETURN self.adjacency[node]
#         RETURN empty list


# ---------------------------------------------------------------------------
# BREADTH-FIRST SEARCH (BFS)
# ---------------------------------------------------------------------------
# Explores the graph level by level starting from a source node.
# Uses a FIFO queue.
#
# FUNCTION bfs(graph, start):
#     CREATE visited = empty set
#     CREATE order   = empty list           # traversal order (result)
#     CREATE queue   = empty FIFO queue
#
#     ENQUEUE start INTO queue
#     ADD start TO visited
#
#     WHILE queue IS NOT empty:
#         SET node = DEQUEUE from queue
#         APPEND node TO order
#
#         FOR EACH neighbor IN graph.neighbors(node):
#             IF neighbor NOT IN visited:
#                 ADD neighbor TO visited
#                 ENQUEUE neighbor INTO queue
#
#     RETURN order


# ---------------------------------------------------------------------------
# DEPTH-FIRST SEARCH (DFS) — ITERATIVE
# ---------------------------------------------------------------------------
# Explores as deep as possible before backtracking.
# Uses a LIFO stack.
#
# FUNCTION dfs_iterative(graph, start):
#     CREATE visited = empty set
#     CREATE order   = empty list
#     CREATE stack   = empty LIFO stack
#
#     PUSH start ONTO stack
#
#     WHILE stack IS NOT empty:
#         SET node = POP from stack
#         IF node IN visited:
#             CONTINUE
#         ADD node TO visited
#         APPEND node TO order
#
#         FOR EACH neighbor IN REVERSED(graph.neighbors(node)):
#             IF neighbor NOT IN visited:
#                 PUSH neighbor ONTO stack
#
#     RETURN order


# ---------------------------------------------------------------------------
# DEPTH-FIRST SEARCH (DFS) — RECURSIVE
# ---------------------------------------------------------------------------
# FUNCTION dfs_recursive(graph, start):
#     CREATE visited = empty set
#     CREATE order   = empty list
#     CALL _dfs_visit(graph, start, visited, order)
#     RETURN order
#
# FUNCTION _dfs_visit(graph, node, visited, order):
#     ADD node TO visited
#     APPEND node TO order
#     FOR EACH neighbor IN graph.neighbors(node):
#         IF neighbor NOT IN visited:
#             CALL _dfs_visit(graph, neighbor, visited, order)


# ---------------------------------------------------------------------------
# SHORTEST PATH (unweighted) VIA BFS
# ---------------------------------------------------------------------------
# Returns the shortest path (fewest edges) from start to goal, or None.
#
# FUNCTION shortest_path_bfs(graph, start, goal):
#     IF start == goal:
#         RETURN [start]
#
#     CREATE visited = set containing start
#     CREATE queue   = empty FIFO queue
#     ENQUEUE (start, [start]) INTO queue   # (current_node, path_so_far)
#
#     WHILE queue IS NOT empty:
#         SET (node, path) = DEQUEUE from queue
#
#         FOR EACH neighbor IN graph.neighbors(node):
#             IF neighbor == goal:
#                 RETURN path + [neighbor]
#             IF neighbor NOT IN visited:
#                 ADD neighbor TO visited
#                 ENQUEUE (neighbor, path + [neighbor]) INTO queue
#
#     RETURN None    # goal not reachable


# ---------------------------------------------------------------------------
# CONNECTED COMPONENTS (undirected graph)
# ---------------------------------------------------------------------------
# FUNCTION connected_components(graph):
#     CREATE visited    = empty set
#     CREATE components = empty list
#
#     FOR EACH node IN graph.adjacency:
#         IF node NOT IN visited:
#             SET component = bfs(graph, node)
#             ADD ALL nodes IN component TO visited
#             APPEND component TO components
#
#     RETURN components


# ---------------------------------------------------------------------------
# EXAMPLE USAGE (pseudo code)
# ---------------------------------------------------------------------------
#     CREATE g = Graph(directed = False)
#     g.add_edge("A", "B")
#     g.add_edge("A", "C")
#     g.add_edge("B", "D")
#     g.add_edge("C", "E")
#     g.add_edge("E", "F")
#
#     PRINT bfs(g, "A")                    # e.g. [A, B, C, D, E, F]
#     PRINT dfs_iterative(g, "A")          # e.g. [A, B, D, C, E, F]
#     PRINT dfs_recursive(g, "A")          # e.g. [A, B, D, C, E, F]
#     PRINT shortest_path_bfs(g, "A", "F") # e.g. [A, C, E, F]
#     PRINT connected_components(g)        # e.g. [[A, B, C, D, E, F]]

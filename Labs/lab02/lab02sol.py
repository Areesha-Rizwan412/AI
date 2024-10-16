from collections import deque



def bfs(graph, start):
    queue = deque([start])
    visited = set()
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)


def dfs(graph, start):
    stack = deque([start])
    visited = set()
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)



def dls(node, goal, depth, graph, visited):
    if depth == 0 and node == goal:
        return True
    if depth > 0:
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dls(neighbor, goal, depth - 1, graph, visited):
                    return True
        visited.remove(node)
    return False


def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth):
        visited = set()
        if dls(start, goal, depth, graph, visited):
            print(f"Goal '{goal}' found at depth {depth}")
            return True
    print("Goal not found")
    return False


def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []
    }
    print("BFS: ")
    bfs(graph, 'A')
    print()

    print("DFS: ")
    dfs(graph, 'A')
    print()
    print("IDDFS: ")
    iddfs(graph, 'A', 'F', 3)


if __name__ == '__main__':
    main()

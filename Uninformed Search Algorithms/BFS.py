class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, u, v):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        self.adjacency_list[u].append(v)

    def bfs(self, start):
        if start not in self.adjacency_list:
            return []

        visited = {node: False for node in self.adjacency_list}
        queue = []
        queue_append = queue.append
        queue_pop = queue.pop

        queue_append(start)
        visited[start] = True
        result = [start]

        while queue:
            node = queue_pop(0)
            neighbors = self.adjacency_list.get(node, [])
            for neighbor in neighbors:
                if not visited[neighbor]:
                    queue_append(neighbor)
                    visited[neighbor] = True
                    result.append(neighbor)

        for node in self.adjacency_list:
            if not visited[node]:
                queue_append(node)
                visited[node] = True
                while queue:
                    node = queue_pop(0)
                    neighbors = self.adjacency_list.get(node, [])
                    for neighbor in neighbors:
                        if not visited[neighbor]:
                            queue_append(neighbor)
                            visited[neighbor] = True
                            result.append(neighbor)

        return result

# Get graph edges from user input
g = Graph()
edges = int(input("Enter the number of edges: "))
for i in range(edges):
    u, v = map(int, input(f"Enter edge {i + 1} (u v): ").split())
    g.add_edge(u, v)

start_node = int(input("Enter the starting node for BFS: "))
bfs_result = g.bfs(start_node)
print(f"BFS traversal starting from node {start_node}: {bfs_result}")

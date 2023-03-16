class Graph:
    def __init__(self, num):
        self.num = num
        # Adjancency matrix
        self.graph = [[0 for column in range(num)] 
                    for row in range(num)]

    def add_edge(self, node1, node2, weight):
        self.graph[node1][node2] = weight
        self.graph[node2][node1] = weight

    # Uses node 0 as root always
    def spanning_tree(self):
        inf = 999999
        # Selected nodes, so some arent repeated
        selected = [False for node in range(self.num)]
        # Matrix of the resulting MST
        result = [[0 for column in range(self.num)] 
                    for row in range(self.num)]
        
        indx = 0
        print("Original graph weights: ")
        for i in range(self.num):
            print("Node " + str(i) + ": " + str(self.graph[i]))

        while(False in selected):
            minimum = inf
            start = 0
            end = 0
            for i in range(self.num):
                # Look for node conections if part of tree
                if selected[i]:
                    for j in range(self.num):
                        # Avoid cycles
                        if (not selected[j] and self.graph[i][j]>0):  
                            # Minimum path calculation and setting
                            if self.graph[i][j] < minimum:
                                minimum = self.graph[i][j]
                                start, end = i, j

            # Mark node as selected
            selected[end] = True
            # Editing the adjacency matrix
            result[start][end] = minimum
            
            if minimum == inf:
                result[start][end] = 0

            indx += 1            
            result[end][start] = result[start][end]

        # Print the result
        print("New graph connections: ")
        for i in range(len(result)):
            for j in range(0+i, len(result)):
                if result[i][j] != 0:
                    print("%d - %d: %d" % (i, j, result[i][j]))

# Implement graph with node 0 as root, build connections from there
graph = Graph(6)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 4, 3)
graph.add_edge(1, 4, 1)
graph.add_edge(1, 2, 3)
graph.add_edge(4, 3, 6)
graph.add_edge(2, 3, 2)
graph.add_edge(3, 5, 3)

graph.spanning_tree()

import pandas as pd

# A structure to represent a graph using Kruskal's algorithm
class Kruskal:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # function to add an edge to the graph
    def addEdge(self, u, v, w, id):
        self.graph.append([u, v, w, id])

    # utility function to find set of an element i
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # function that carries out union of two sets of x and y
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of high rank tree
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        # If ranks are same, make one as root and increment its rank by one
        else :
            parent[yroot] = xroot
            rank[xroot] += 1

    # function to construct MST using Kruskal's algorithm
    def KruskalMST(self):
        result = []  # to store the resultant MST
        total_weight = 0  # to store the total weight of the MST
        i, e = 0, 0  # indices for sorted edges

        # sort all edges in non-decreasing order of their weight
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        # create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # number of edges to be taken is equal to V-1
        while e < self.V - 1:
            u, v, w, id = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # if including this edge does not cause cycle, include it in result and increment the index of result for next edge
            if x != y:
                e = e + 1
                result.append(id)
                total_weight += w  # add the weight of the edge to the total weight
                self.union(parent, rank, x, y)

        print('The total weight of the minimum spanning tree:', total_weight)
        return total_weight, sorted(result)
  # sort the result in alphabetical order

# read the graph data from the CSV file
df = pd.read_csv('benchmark_3.csv', delimiter='\t')

# create a mapping of vertex labels to integers
vertices = {vertex: i for i, vertex in enumerate(pd.concat([df['Vertex1'], df['Vertex2']]).unique())}

# create a graph
g = Kruskal(len(vertices))

# add edges to the graph
for index, row in df.iterrows():
    g.addEdge(vertices[row['Vertex1']], vertices[row['Vertex2']], row['weight'], row['id'])

# find the minimum spanning tree and print the edge labels
total_weight, mst = g.KruskalMST()
print(','.join(mst))

# write the output to a text file
with open('output.txt', 'w') as f:
  f.write('The total weight of the minimum spanning tree: ' + str(total_weight) +'\n')
  f.write(','.join(mst) )
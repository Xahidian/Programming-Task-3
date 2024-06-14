# Programming Task 3

## Graph Search Algorithm
### Course: IT00CD89-3005 Graph Algorithms 5

-------
**Submitted By:**
**MD Hasibul Haque Zahid (2302302)** 
**Nabil Arman Ayon (2302291)**

-------

### Implementation
This Python script implements Kruskal’s algorithm to find the minimum spanning tree of a graph. The graph data is read from a CSV file and the total weight of the minimum spanning tree is printed, along with the edge labels.

### Algorithm working process
This code is implementing Kruskal’s algorithm to find the minimum spanning tree (MST) of a graph. Here’s a step-by-step breakdown:

1. Importing Required Libraries: The code begins by importing the pandas library, which is used for data manipulation and analysis.
2. Defining the Graph Class: The Kruskal class is defined to represent a weighted, undirected graph. The class has methods to add edges to the graph and to find the MST using Kruskal’s algorithm.
3. Adding Edges: The addEdge method is used to add an edge to the graph. An edge is represented as a list of four elements: two vertices (u and v), the weight of the edge (w), and the ID of the edge (id).
4. Finding the Parent of a Vertex: The find method is a utility function to find the set of an element i (in this case, a vertex). It uses path compression, which flattens the structure of the tree by making every node point to the root whenever find is used on it.
5. Union of Two Sets: The union method carries out the union of two sets x and y. It uses union by rank, which attaches the smaller tree (in terms of rank) as a subtree of the root node of the larger tree.
6.  Kruskal’s Algorithm: The KruskalMST method constructs the MST using Kruskal’s algorithm. It sorts all the edges in non-decreasing order of their weight. It then picks the smallest edge that does not form a cycle with the MST formed so far. It does this until there are (V-1) edges in the MST, where V is the number of vertices.
7. Reading the Graph Data: The graph data is read from a CSV file using pandas. The CSV file should have four columns: “Vertex1”, “Vertex2”, “weight”, and “id”.
8. Creating a Graph: A Kruskal object is created, and edges are added to it using the data from the CSV file.
9. Finding the MST: Finally, the KruskalMST method is called on the graph object to find the MST. The method prints the total weight of the MST and returns a list of the IDs of the edges in the MST.

### Testing Process
The script was tested using a dataset named "(benchmark_3.csv)". The output of the script was a list of edge IDs that form the minimum spanning tree (MST) of the graph, and the total weight of the MST.

The correctness of the output was verified manually by:

1. Checking that the output edges do not form a cycle.
2. Confirming that all vertices are included in the MST.
3. Ensuring that the total weight of the MST is the smallest possible.
4. The output of the script was e1011,e15,e25,e36,e46,e58,e611,e67,e810,e89 and The total weight of the minimum spanning tree: 395. This matches the expected given output, indicating that the script is working correctly.

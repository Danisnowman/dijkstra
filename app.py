import ast
from collections import deque, namedtuple

inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')

graph_arr= []

# First we read our nodes:
graph_file=open('graph.txt','r')

# Second we translate from the txt format to a namedtuples
for lista in graph_file.readlines():
    # For that we'll need to replace the 'new lines'
    str_1 = lista.replace("\n", "")
    # Then evaluate the ()'s to make each of them a namedtuple
    str_2 = ast.literal_eval(str_1)
    # Finally we append it to our list/array of namedtuples
    graph_arr.append(str_2)
graph_file.close()

class Menu:
    # This function will be used to choose the initial and last node.
    def choose_node(self):
        self.initial_node = input("Choose your initial node: ")   
        self.last_node = input("Choose your last node: ")

    # This function will automatically send the initial and last node to dijkstra's algorithm and print the shortest route.
    def print_route(self):
        route = graph.dijkstra(str(self.initial_node), str(self.last_node))
        print(f"The shortest route is: '{route}'.")

    # This is the main menu
    def start(self):
        option = input("Is the graph... \n0) Non-Directed\n1) Directed\n\nYour option: ")
        if option == "1":
            # 'both_ends' is set to False because, given that the graph is directed, we cannot use both ends
            both_ends = False 
            print("Your graph is directed.\n\n")
            # We choose initial and last nodes with the following function
            self.choose_node()
            # We print the best route
            self.print_route()
           
        elif option == "0":
            # 'both_ends' is set to True because, given that the graph is non-directed, we can and will use both ends
            both_ends = True
            print("Your graph is non-directed.\n\n")
            # We choose initial and last nodes with the following function
            self.choose_node()
            # We print the best route
            self.print_route()
        
        else:
            # if 'option' is outside of the menu it raises an error:
            print(f"The option you entered '{option}' is invalid!\nPlease try again!\n")
            # if said error is raised then it reverts back to the main menu
            start()
        return both_ends
        

# We define each edge
def make_edge(start, end, cost=1):
    return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
     # The following will check if the data is in the right format
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError(f"Wrong edges data: '{wrong_edges}''")

        self.edges = [make_edge(*edge) for edge in edges]   

    @property
    def vertices(self):
        return set(
            # this piece of magic turns ([1,2], [3,4]) into [1, 2, 3, 4]
            # the set above makes it's elements unique.
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError("Edge {n1} {n2} already exists")

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        assert source in self.vertices, f"Such source '{source}' node doesn't exist"
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return path


graph = Graph(graph_arr)
menu = Menu()
menu.start()
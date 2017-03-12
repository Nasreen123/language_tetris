import networkx as nx

"""
GRAPH FUNCTIONS

add_node: INPUT: graph, new node OUTPUT: graph with node add_edge

add_collision: INPUT: graph, 2 nodes OUTPUT: graph with an edge added between the 2 nodes

search_graph: INPUT: graph, sentences OUTPUT: nodes that form a sentence (first sentence it finds)
*** later should it remove longer sentence?

remove_nodes: INPUT: graph, nodes to remove OUTPUT: updated graph
"""

def add_node(graph, block):
    graph.add_node(block)
    return graph

def add_collision(graph, block1, block2):
    graph.add_edge(block1, block2)
    return graph

def look_through_neighbors(graph, neighbors, i, sentence):
    i += 1

    if len(neighbors) == 0: #input list empty (no matching neighbors for previous node)
        return 0

    elif len(neighbors) > 0 and i == len(sentence): #nodes in input list (representing last word) -> send one back
        return [neighbors[0]]

    elif len(neighbors) > 0: #input list not empty, there are matching neighbors
        # for each neighbor, get its neighbors which match the next word
        # call look through on those
        for neighbor in neighbors:
            matching_neighbors = [node for node in graph.neighbors(neighbor) if node.word == sentence[i]]
            match = look_through_neighbors(graph, matching_neighbors, i, sentence)
            if type(match) == list:
                match.append(neighbor)
                return match

def search_graph(graph, sentences):
    for sentence in sentences:
        i = 0
        start_nodes = [node for node in graph.nodes() if node.word == sentence[i]]
        match = look_through_neighbors(graph, start_nodes, i, sentence)
        print 'match ', match
        if match:
            print 'SENTENCE FORMED!'
            for item in match:
                print item.word
            return match

def remove_nodes(graph, nodes):
    graph.remove_nodes_from(nodes)
    return graph

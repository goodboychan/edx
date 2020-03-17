# -*- coding: utf-8 -*-
"""
Created on Tue May 30 22:52:54 2017

@author: kcsgo
"""

# Video 4.3.2
import networkx as nx

G = nx.Graph()
# Add one node
G.add_node(1)
# Add multiple nodes
G.add_nodes_from([2, 3])

G.add_nodes_from(["u", "v"])

G.nodes()

# Add one edge
G.add_edge(1, 2)
G.add_edge("u", "v")
# Add multiple edges
G.add_edges_from([(1,3), (1,4), (1,5), (1,6 )])
G.add_edge("u", "v")

G.edges()

# Remove node
G.remove_node(2)

G.nodes()
# Remove multiple node
G.remove_nodes_from([4,5])

G.nodes()

G.remove_edge(1,3)

G.edges()

G.remove_edges_from([(1,2), ("u", "v")])

G.edges()

G.number_of_nodes()
G.number_of_edges()

# Video 4.3.3
# Karate club graph
import matplotlib.pyplot as plt

G = nx.karate_club_graph()
nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray")
plt.savefig("karate_graph.pdf")

G.degree()[33]

G.degree(33)

# Video 4.3.4
from scipy.stats import bernoulli

bernoulli.rvs(p=0.2)

# Implement ER graph
N = 20
p = 0.2

# create empty graph
# add all N nodes in the graph
# loop over all pairs of nodes
    # add an edge with prob p
  
def er_graph(N, p):
    """
    Generate an ER graph.
    """
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 < node2 and bernoulli.rvs(p=p):
                G.add_edge(node1, node2)
    return G
            
G.number_of_nodes()
nx.draw(er_graph(50, 0.08), node_size=40, node_color="gray")
plt.savefig("er1.pdf")

nx.draw(er_graph(10, 1))

# Video 4.3.5
def plot_degree_distribution(G):
    plt.hist(list(G.degree().values()), histtype="step")
    plt.xlabel("Degree $k$")
    plt.ylabel("$P(k)$")
    plt.title("Degree distribution")
    
G = er_graph(50, 0.08)
plot_degree_distribution(G)
plt.savefig("hist1.pdf")

G = er_graph(500, 0.08)
plot_degree_distribution(G)
plt.savefig("hist2.pdf")

G1 = er_graph(500, 0.08)
plot_degree_distribution(G1)
G2 = er_graph(500, 0.08)
plot_degree_distribution(G2)
G3 = er_graph(500, 0.08)
plot_degree_distribution(G3)
plt.savefig("hist3.pdf")

# Video 4.3.6
import numpy as np
A1 = np.loadtxt("adj_allVillageRelationships_vilno_1.csv", delimiter=",")
A2 = np.loadtxt("adj_allVillageRelationships_vilno_2.csv", delimiter=",")

G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

# Calculate mean degree
def basic_net_stats(G):
    print("Number of nodes: %d" % G.number_of_nodes())
    print("Number of edges: %d" % G.number_of_edges())
    print("Average degree: %.2f" % np.mean(list(G.degree().values())))
    
basic_net_stats(G1)
basic_net_stats(G2)

# Plot the histogram of degree
plot_degree_distribution(G1)
plot_degree_distribution(G2)
plt.savefig("village_hist.pdf")

# Video 4.3.7
gen = nx.connected_component_subgraphs(G1)

g = gen.__next__()
type(g)

g.number_of_nodes()

len(gen.__next__())

len(G1)
G1.number_of_nodes()

G1_LCC = max(nx.connected_component_subgraphs(G1), key=len)
G2_LCC = max(nx.connected_component_subgraphs(G2), key=len)

len(G1_LCC)
len(G2_LCC)

G1_LCC.number_of_nodes() / G1.number_of_nodes()
G2_LCC.number_of_nodes() / G2.number_of_nodes()

plt.figure()
nx.draw(G1_LCC, node_color="red", edge_color="gray", node_size=20)
plt.savefig("village1.pdf")

plt.figure()
nx.draw(G2_LCC, node_color="green", edge_color="gray", node_size=20)
plt.savefig("village2.pdf")

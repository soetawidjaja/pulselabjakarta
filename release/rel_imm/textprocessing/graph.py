#!/usr/bin/python

import os, sys
import networkx as nx
import matplotlib.pyplot as plt

if len(sys.argv) <> 3:
   sys.stderr.write('[usage] %s (input) (threshold-1)\n')
   #sys.stderr.write('[usage] %s (input) (threshold-1) (threshold-2)\n')
   sys.stderr.write('\t (input): from to weight\n')
   sys.stderr.write('\t (threshold-1): to discard an edge if its weight is below this\n')
   #sys.stderr.write('\t (threahold-2): if a weight is greater than this, its edge is a large edge,\n')
   exit()

PARAM_input = sys.argv[1]
PARAM_weight_cut = int(sys.argv[2])
#PARAM_weight_threshold = int(sys.argv[3])

DG = nx.DiGraph()
edges = []
colors = []
for line in open(PARAM_input):
   es = line.split()
   edge  = (es[0], es[1], int(es[2]))
   if edge[2] > PARAM_weight_cut:
      edges.append(edge)
      colors.append(edge[2])

DG.add_weighted_edges_from(edges)
G = nx.Graph(DG)
#pos=nx.random_layout(G)
#pos=nx.circular_layout(G) 
pos=nx.spring_layout(G)
#pos=nx.spectral_layout(G)
#pos=nx.shell_layout(G)

'''
two type classification
'''
'''
elarge=[(u,v) for (u,v,d) in DG.edges(data=True) if d['weight'] > PARAM_weight_threshold]
esmall=[(u,v) for (u,v,d) in DG.edges(data=True) if d['weight'] <=PARAM_weight_threshold]
# nodes
nx.draw_networkx_nodes(G,pos,node_size=700)
# edges
nx.draw_networkx_edges(G,pos,edgelist=elarge,width=2,edge_color='r')
nx.draw_networkx_edges(G,pos,edgelist=esmall,width=2,alpha=0.5,edge_color='b',style='dashed')
# labels
nx.draw_networkx_labels(G,pos,font_size=25,font_family='sans-serif')
'''

#nx.draw(G,pos,node_color='#A0CBE2',node_size=7,edge_color=colors,width=4,edge_cmap=plt.cm.Blues,with_labels=False)
#nx.draw_networkx_labels(G,pos,font_size=20)#,font_family='sans-serif')

nx.draw(G,pos,node_color='#A0CBE2',node_size=7,edge_color='gray',width=1,with_labels=False)
#nx.draw_networkx_labels(G,pos,font_size=10)#,font_family='sans-serif')

plt.axis('off')
plt.savefig("weighted_graph.png") # save as png
plt.show()

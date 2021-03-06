import networkx as nx
import collections
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
from networkx.algorithms.isomorphism import GraphMatcher
from networkx.algorithms import tournament
import os
import warnings
warnings.simplefilter("ignore")
# ----------------------makebig----------------------------------------------------------------------------------------------
def makeBig(glist):
    garr = []
    # Iter through list of graphs
    for g in glist:
        # find possible edges for the graph g
        filtered = []
        for nod in g.nodes():
            for nod2 in g.nodes():
                if nx.shortest_path_length(g, nod, nod2) == 2:
                    filtered.append((nod, nod2))
        # Go through the list of possible filtered edges
        for tup in filtered:
            ga = g.copy()
            ga.add_edge(*tup)
            # Check if graph g is isomorphic to any of the previous graphs so far
            appen = True
            gm_k4_check = GraphMatcher(ga, nx.complete_graph(4))
            if not nx.check_planarity(ga)[0]:
                appen = False
            elif gm_k4_check.subgraph_is_isomorphic():
                appen = False
            else:
                for el in garr:
                    if nx.is_isomorphic(el, ga):
                        appen = False
            for a1 in ga.nodes():
                for b1 in ga.nodes():
                    if a1<b1:
                        c = ga.copy()
                        cut = list(nx.articulation_points(c))
                        if c.has_edge(a1, b1):
                            c.remove_node(a1)
                            c.remove_node(b1)
                            if a1 in cut and b1 in cut or a1 not in cut and b1 not in cut:
                                if nx.number_connected_components(c)>2:
                                    appen =False
            r5 = []
            for n1 in ga.nodes():
                e = ga.copy()
                if ga.degree(n1)>=4:
                    f = e.subgraph([n for n in e.neighbors(n1)])
                    try:
                        r4 = (list(nx.find_cycle(f, orientation='ignore')))
                        if len(r4)!=len(f) and len(r4)>=4:
                            appen= False
                        else:
                            r5.append(list(nx.find_cycle(f, orientation='ignore')))
                    except:
                        pass
            j1=0
            for i1 in r5:
                j1=j1+1
                for i2 in r5[j1:]:
                    if collections.Counter(i1)==collections.Counter(i2):
                        appen=False

                        
            if ga.size()>3*init-7:
                appen=False
            
            if appen:
                garr.append(ga)
    return garr



# ---------------------main---------------------------------------------------------------------------------------------------
init=9

g= nx.path_graph(init)
try:
    os.mkdir("RFP3")
except:
    pass
try:
    os.mkdir("RFP3/Len={}".format(init))
except:
    pass
ra=1
nex=[g]
while(nex):
    sum=0
    for x in nex:
        appen=True
        ga=x.copy()
        if appen:
            sum+=1
            plt.figure(ra)
            nx.draw_planar(x,labels=None, font_size=12, font_color='k', font_family='sans-serif', font_weight='normal', alpha=1.0, bbox=None, ax=None)
            plt.savefig('RFP3/Len={}/i{}.png'.format(init,ra))
            # plt.show()
            print(x.edges)
            ra+=1
    print('Inner Graphs for size = {}: '.format(len(x.edges)),sum)
    nex=makeBig(nex)


# -------------end-------------------------------------------------------------------------------------------------------------------
























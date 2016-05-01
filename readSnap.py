# -*- coding: utf-8 -*-
import random
import networkx as nx
import pylab


def readFromSnapTxt(filename):
    # DONE - Do not modify.
    trainingSet = []
    linelist = ()
    # Read in file
    for line in open(filename,'r'):
        if '#' in line:
            continue
            #print line
        #print line
        line = line.strip('\n')
        linelist = line.split('\t')
        #linetup = tuple(linelist)
        trainingSet.append(linelist)    

    return trainingSet
 
#########################################################################################################################################       
#Working on this:
def createNetwork(trainingSet):
    #print trainingSet
    G=nx.MultiDiGraph()     #empty graph structure (a “null graph”) with no nodes and no edges.
    for path in trainingSet:
        orig =  path[0]
        dest = path[1]
        
        #applying dijkstra's:
        distance = random.randrange(1, 15, 1)
        # Add route as an edge to the graph
        G.add_edge(orig, dest, distance=(distance))
        
        
        H=nx.path_graph(82166)
        G.add_nodes_from(range(0,82167))
        #G.add_edges_from(H.path)
        #G.add_edges_from(*path)
        #G.add_edges_from(H.path)

        #print(G.nodes())        
        #print(G.edges())
        #print(G.number_of_nodes())
            
    #G = nx.Graph()
    #G.add_nodes_from(range(0,6))
    #G.add_edge(1, 2, weight=3)
    #G.add_edge(2, 3, weight=5)
    #print(G.nodes())        
    #print(G.edges())
    
###########################################################
                    
    #pylab is a Graph plotting library that we used                                
                                                                    
    pos=nx.spring_layout(G)
    # version 1
    pylab.figure(1)
    nx.draw(G,pos)
    # use default edge labels
    nx.draw_networkx_edge_labels(G,pos)
    
    # version 2
    pylab.figure(2)
    nx.draw(G,pos)
    # specifiy edge labels explicitly
    edge_labels=dict([((u,v,),d['weight'])
                for u,v,d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
    
    # show graphs
    pylab.show()


#######################################################################################################################################################
def main():   
    
    newSet = []
    
    newSet = readFromSnapTxt("Slashdot0902.txt")
    
    print "Data Read... "
    
    #After the Data has been read, the createNetwork creates a network using networkx.   
    createNetwork(newSet)
    
main()
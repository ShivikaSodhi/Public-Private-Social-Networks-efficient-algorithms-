import networkx as nx
G=nx.Graph()

#H=nx.path_graph(10)
#G.add_nodes_from(H)

#take entries from a file;
#convert them into a dictionary
#use that dictionary

alist  = []
for line in open("nodes.txt",'r'):
        if '#' in line:
            continue
        line = line.strip('\n')
        linelist = line.split(',')
        alist.append(line)
        
E = [(1,2),(1,3)]        
        
G.add_nodes_from(alist)
G.add_edges_from(E)

print(G.nodes())

print(G.edges())


print(G.number_of_nodes())

pos=nx.fruchterman_reingold_layout(G) 
type(pos)
    
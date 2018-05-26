import networkx as nx

G=nx.DiGraph()

def add_edge(v1, v2):
    G.add_edge(v1, v2)

def add_node(n):
    G.add_node(n)

if __name__ == '__main__':
    data_file = input()

    with open(data_file) as f:
        data = f.readlines()

    for i in range(int(data[0])):
        if len(data[i+1]) > 3:
            try:
                v1, v2 = data[i+1].split(',')
                add_edge(int(v1), int(v2))
            except:
                pass
        elif len(data[i+1]) == 1:
            add_node(int(data[i+1]))
        else:
            print("Invalid data input")

    source_nodes = [node for node, indegree in G.in_degree(G.nodes()) if indegree == 0]
    dest_nodes = [node for node, outdegree in G.out_degree(G.nodes()) if outdegree == 0]

    for source in source_nodes:
        for dest in dest_nodes:
            for path in nx.all_simple_paths(G, source=source, target=dest):
                print('->'.join(str(i) for i in path))
    print('\n'.join(str(i) for i in list(nx.isolates(G))))

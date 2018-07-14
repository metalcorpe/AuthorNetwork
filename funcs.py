import numpy as np
import networkx as nx
import matplotlib.pyplot as plt



def file_import(file):
    """Imports the Author Network file that must contain the source_id, target_id, timestamp"""
    with open(file, 'r') as fileobject:
        id_table = [[int(x) for x in line.split()] for line in fileobject]
    return np.array(id_table)

class AuthNet:

    def __init__(self, file, debug = False, n = 10):
        self.file = file
        self.debug = debug
        self.id_table = file_import(file)
        self.n = n

    def time_min(self):
        """Q1 min"""
        """Minimum Timestamp"""
        return min(self.id_table[:,2])

    def time_max(self):
        """Q1 max"""
        """Maximum Timestamp"""
        return max(self.id_table[:,2])

    def t_j(self, j = 3):
        """"""
        return self.time_min() + j * int((self.dt()/self.n))

    def t_j_array(self,j = 3):
        return min(np.where((self.id_table[:, 2] >= self.t_j(j=j-1)) & (self.id_table[:, 2] <= self.t_j(j=j))))

    def V(self, j = 3):
        ass = self.t_j_array(j=j)
        return np.unique(self.id_table[ass,0:1])


    def E(self, j = 3):
        ass = self.t_j_array(j=j)
        return self.id_table[min(ass):max(ass),(0,1)]

    def dt(self):
        return self.time_max() - self.time_min()


    def id_size(self):
        """Size of ID Array"""
        return len(self.id_table)

    def lin_space(self):
        """Q2"""
        """Linear Timestamp Space"""
        # if n is not None:
        #     self.n = n
        if self.n < 1 and self.debug == True:
            raise print('Bad n value:', self.n)
        return np.linspace(self.time_min(), self.time_max(), self.n)

    def histogram(self):
        """Q3"""
        """Plot the Timestamp Histogram"""
        plt.hist(self.id_table[:, 2], self.lin_space())
        plt.show()

    def Gi(self, j = 3):
        # """Sl 1: TODO Assume that the timestamps are shorted"""
        # """1<=j<=N"""
        # if j not in range(1,self.n) and self.debug == True:
        #     raise print('Bad j value:', j)

        G = nx.DiGraph()
        # G.add_nodes_from(self.V(j=j).tolist())
        G.add_edges_from(self.E(j=j))
        return G

        # return np.arange(self.lin_space()[j-1],self.lin_space()[j])

    def g_graph(self):
        options = {
            'node_color': 'red',
            'node_size': 10,
            'width': 1,
        }
        nx.draw(self.Gi(j=3), **options)
        plt.show()

    def degr_central(self):
        nx.algorithms.centrality.degree_centrality(self.Gi(j=3))
        plt.show()


if __name__=="__main__":
    """Main Function"""
    # imported_table = file_import("sx-stackoverflow_test.txt")
    # print(imported_table)
    net=AuthNet("sx-stackoverflow_test.txt")
    # net.id_size()
    # print(net.id_table[:,2])
    # print(net.lin_space())
    # print(net.time_min(), net.time_max())
    # print(net.id_size())
    # print(net.lin_space())
    # a = net.time_min()
    # net.histogram()
    # net.id_table[:,
    # print()
    # net.G(j=1)
    # print(net.degr_central())

    a = nx.degree_centrality(net.Gi())
    b = nx.in_degree_centrality(net.Gi())
    c = nx.out_degree_centrality(net.Gi())
    d = nx.closeness_centrality(net.Gi())
    e = nx.betweenness_centrality(net.Gi())
    f = nx.eigenvector_centrality(net.Gi())
    g = nx.katz_centrality(net.Gi())
    # for v in net.Gi().nodes():
        # print("%0.2d %5.3f" % (v, d[v]))
    # nx.draw(net.Gi())
    # plt.show()
    net.g_graph()
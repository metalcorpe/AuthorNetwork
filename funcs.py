import numpy as np

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
        import matplotlib.pyplot as plt
        plt.hist(self.id_table[:, 2], self.lin_space())
        plt.show()

    def gi(self, j = 1):
        """Sl 1: TODO Assume that the timestamps are shorted"""
        """1<=j<=N"""
        if j not in range(1,self.n) and self.debug == True:
            raise print('Bad j value:', j)
        return np.arange(self.lin_space()[j-1],self.lin_space()[j])




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
    # net.gi()
    # print(np.max(net.id_table,0))
    # net.histogram()
    # a = np.empty([1,4],dtype=int)
    # print(a)
    # for j in range(1, net.n):
    #     # print(j)
    #     for x in range(1, net.id_size()):
    #         # print(x)
    #         if net.id_table[x,2] in np.arange(net.lin_space()[j-1],net.lin_space()[j]):
    #             print(net.id_table[x,:])
    #             a = np.append(a, [j, net.id_table[x,:] ], axis=0)
    # #
    # #
    # # p = [q.index(v) if net.id_table[:,x] in range(1,2) else pass for x in range(0, net.id_size())]

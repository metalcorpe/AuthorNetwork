import numpy as np

def file_import(file):
    """Imports the Author Network file that must contain the source_id, target_id, timestamp"""
    with open(file, 'r') as fileobject:
        id_table = [[int(x) for x in line.split()] for line in fileobject]

    return np.array(id_table)


# class min_max:
class AuthNet:

    def __init__(self, file, debug = False, N = 10):
        self.file = file
        self.debug = debug
        self.id_table = file_import(file)
        self.N = N

    def time_min(self):
        """Minimum Timestamp"""
        return min(self.id_table[:,2])

    def time_max(self):
        """Maximum Timestamp"""
        return max(self.id_table[:,2])

    def id_size(self):
        """Size of ID Array"""
        return len(self.id_table)

    def lin_space(self):
        """Linera Timestamp Space"""
        try:
            lin = np.linspace(self.time_min(), self.time_max(), self.N)
        except:
            raise
        return lin

    def histogram(self):
        import matplotlib.pyplot as plt
        plt.hist(net.id_table[:, 2], net.lin_space())
        plt.show()



    # def hisgram(self):
    #
    #
    #     n,x, patches = plt.hist(self.id_table[:][2], self.N, density=True, facecolor='g', alpha=0.75)
    #     return n,x,patches



if __name__=="__main__":
    # imported_table = file_import("sx-stackoverflow_test.txt")
    # print(imported_table)
    net=AuthNet("sx-stackoverflow_test.txt")

    # print(net.id_table[:,2])
    # print(net.lin_space())
    # print(net.time_min(), net.time_max())
    # print(net.id_size())
    # print(net.lin_space())
    # a = net.hisgram()

    net.histogram()
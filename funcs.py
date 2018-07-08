def file_import(file):
    """Imports the Author Network file that must contain the source_id, target_id, timestamp"""
    with open(file, 'r') as fileobject:
        id_table = [[int(x) for x in line.split()] for line in fileobject]

    return id_table


# class min_max:
class AuthNet:

    def __init__(self, file, debug = False, N = 10):
        self.file = file
        self.debug = debug
        self.id_table = file_import(file)
        self.N = N


    def min(self):
        return min(self.id_table[:][3])

    def max(self):
        return max(self.id_table[:][3])

    def lin_space(self):
        from numpy import linspace
        try:
            lin = linspace(self.min(), self.max(), self.N)
        except:
            raise
        return lin

if __name__=="__main__":
    # imported_table = file_import("sx-stackoverflow_test.txt")
    # print(imported_table)
    net=AuthNet("sx-stackoverflow_test.txt")

    # print(net.min(), net.max())
    print(net.lin_space())
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

    def time_min(self):
        """Minimum Timestamp"""
        return min(self.id_table[:][3])

    def time_max(self):
        """Maximum Timestamp"""
        return max(self.id_table[:][3])

    def id_size(self):
        """Size of ID Array"""
        return len(self.id_table)

    def lin_space(self):
        """Linera Timestamp Space"""
        from numpy import linspace
        try:
            lin = linspace(self.time_min(), self.time_max(), self.N)
        except:
            raise
        return lin

if __name__=="__main__":
    # imported_table = file_import("sx-stackoverflow_test.txt")
    # print(imported_table)
    net=AuthNet("sx-stackoverflow_test.txt")

    # print(net.time_min(), net.time_max())
    print(net.id_size())
    print(net.lin_space())
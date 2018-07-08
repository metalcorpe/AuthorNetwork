def file_import(file):
    """Imports the Author Network file that must contain the source_id, target_id, timestamp"""
    with open(file, 'r') as fileobject:
        id_table = [[int(x) for x in line.split()] for line in fileobject]

    return id_table


# class min_max:
class AuthNet():

    def __init__(self, file):
        self.file = file
        self.id_table = file_import(file)

    def min(self):
        return min(self.id_table[:][3])

    def max(self):
        return max(self.id_table[:][3])



if __name__=="__main__":
    # imported_table = file_import("sx-stackoverflow_test.txt")
    # print(imported_table)
    min = AuthNet("sx-stackoverflow_test.txt").min()
    max = AuthNet("sx-stackoverflow_test.txt").max()
    print(min, max)
with open("sx-stackoverflow_test.txt", 'r') as fileobject:
    # for line in fileobject:
        # print(line)
        source_id = [[int(x) for x in line.split()] for line in fileobject]

        # source_id = line.strip().split(' ')
        print(source_id)
        print(source_id[0][0] + source_id[1][0])
        exit()
            # , target_id, timestamp


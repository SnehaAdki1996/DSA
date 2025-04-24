def survivedRobotsHealths(positions, healths, directions):
    index_map = {p:i for i,p in enumerate(positions)}
    positions.sort()
    stack = []
    print(index_map)
    print(positions)
    for i in positions:
        actual_pos = index_map[i]
        if directions[actual_pos] == 'R':
            stack.append(actual_pos)
        else:
            print(stack,i,directions)
            # print( directions[stack[-1]])
            while stack and healths[actual_pos]:
                p2 = stack.pop()
                if healths[actual_pos] > healths[p2]:
                    healths[p2] = 0
                    healths[actual_pos] = healths[actual_pos] - 1

                elif healths[actual_pos] < healths[p2]:
                    healths[actual_pos] = 0
                    healths[p2] = healths[p2] - 1
                    stack.append(healths[p2])
                else:
                    healths[actual_pos] = healths[p2] = 2

            

    print([h for h in healths if h>0 ])


positions = [3,5,2,6]
healths = [10,10,15,12]
directions = "RLRL"
survivedRobotsHealths(positions, healths, directions)
import time
import pickle
# NOTE: Running with actual input from AoC will take approx ~13 mins
with open("2024\day06\\text_input.txt", 'r') as file:
    map = [list(line.strip("\n")) for line in file]
    
def find_the_guard(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "^":
                return (i, j)
            
    return (i, j)

def find_distinct_positions(map):
    i, j = find_the_guard(map)
    new_map = pickle.loads(pickle.dumps(map))
    walking_dir = (-1, 0)
    started = time.time()
    
    while i in range(len(new_map)) and j in range(len(new_map[i])):
        if time.time() - started < 0.5:
            new_pos = (i+walking_dir[0], j+walking_dir[1])
            
            if new_pos[0] < 0 or new_pos[0] >= len(new_map):
                break
            if new_pos[1] < 0 or new_pos[1] >= len(new_map[0]):
                break
            
            if new_map[new_pos[0]][new_pos[1]] != '#' and new_map[new_pos[0]][new_pos[1]] != "O":
                new_map[new_pos[0]][new_pos[1]] = new_map[i][j]
                new_map[i][j] = 'X'
                i = new_pos[0]
                j = new_pos[1]
            else:
                match new_map[i][j]:
                    case "^":
                        new_map[i][j] = ">"
                        walking_dir = (0, 1)
                    case ">":
                        new_map[i][j] = "v"
                        walking_dir = (1, 0)
                    case "v":
                        new_map[i][j] = "<"
                        walking_dir = (0, -1)
                    case "<":
                        new_map[i][j] = "^"
                        walking_dir = (-1, 0)
        else:
            return (-1, [])
    
    new_map[i][j] = 'X'
    return (sum([line.count('X') for line in new_map]), new_map)

def find_ways_to_loop(map):
    _, new_map = find_distinct_positions(map)
    count_loops = 0
    
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] != "^" and map[i][j] != "#" and new_map[i][j] == "X":
                test_map = pickle.loads(pickle.dumps(map))
                test_map[i][j] = "O"
                
                if find_distinct_positions(test_map)[0] == -1:
                    count_loops += 1
                    
    return count_loops

print("The number of distinct positions is:", find_distinct_positions(map)[0])
print("The number of obstruction positions is:", find_ways_to_loop(map))
with open("2024\day04\\test_input.txt", 'r') as file:
    wordsearch = [line.strip("\n") for line in file]
    
XMAS = "XMAS"
directions = [
    [0, -1],    # RIGHT
    [0, 1],     # LEFT
    [-1, 0],    # UP
    [1, 0],     # DOWN
    [-1, -1],   # UP-LEFT
    [-1, 1],    # UP-RIGHT
    [1, -1],    # DOWN-lEFT
    [1, 1]      # DOWN-RIGHT
]

diag_directions = [
    ([-1, -1], [1, 1]),      # UP-LEFT & DOWN-RIGHT
    ([-1, 1], [1, -1])    # UP-RIGHT & DOWN-lEFT
]

def search_part1 (wordsearch):
    count_part1 = 0
    
    for i in range(len(wordsearch)):
        for j in range(len(wordsearch[i])):
            if wordsearch[i][j] == 'X':
                for direction in directions:
                    if find_XMAS(wordsearch, 0, (i, j), direction):
                        count_part1 += 1
                        
    return count_part1

def search_part2 (wordsearch):
    count_part2 = 0
    
    for i in range(len(wordsearch)):
        for j in range(len(wordsearch)):
            if wordsearch[i][j] == 'A' and find_cross(wordsearch, (i, j)):
                count_part2 += 1
                
    return count_part2

def find_XMAS (wordsearch, xmas_index, coords, dir):
    i, j = coords
    
    if xmas_index == 4:
        return True
    
    if i < 0 or i >= len(wordsearch):
        return False
    
    if j < 0 or j >= len(wordsearch[0]):
        return False
    
    if wordsearch[i][j] != XMAS[xmas_index]:
        return False
    
    return find_XMAS(wordsearch, xmas_index + 1, (i + dir[0], j + dir[1]), dir)

def find_cross (wordsearch, coords):
    i, j = coords
    
    for cross in diag_directions:
        i_1 = i + cross[0][0]
        j_1 = j + cross[0][1]
        i_2 = i + cross[1][0]
        j_2 = j + cross[1][1]
        
        if i_1 < 0 or i_1 >= len(wordsearch) or i_2 < 0 or i_2 >= len(wordsearch):
            return False
        
        if j_1 < 0 or j_1 >= len(wordsearch) or j_2 < 0 or j_2 >= len(wordsearch):
            return False
        
        coord_1 = wordsearch[i_1][j_1]
        coord_2 = wordsearch[i_2][j_2]
        char_tuple = (coord_1, coord_2)
        
        if char_tuple != ('M', 'S') and char_tuple != ('S', 'M'):
            return False
        
    return True
        
        
print(search_part1(wordsearch))
print(search_part2(wordsearch))
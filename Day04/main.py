def maxtrify():
    matrix = []
    with open('input.txt', 'r') as file:
        for line in file:
            matrix.append(list(line.strip()))
    return matrix

def isValid(x, y, n, m):
    return x >= 0 and x < n and y >= 0 and y < m

def findWordInDirection(matrix, word, n, m, x, y, dirX, dirY, index):
    if index == len(word):
        return True
    
    if isValid(x, y, n, m) and word[index] == matrix[x][y]:
        return findWordInDirection(matrix, word, n, m, x + dirX, y + dirY, dirX, dirY, index + 1)


def solve1(matrix, word):
    res = 0
    n = len(matrix)
    m = len(matrix[0])

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == word[0]:
                for dirX, dirY in directions:
                    if findWordInDirection(matrix, word, n, m, i, j, dirX, dirY, 0):
                        res += 1

    print(res)
      
                
def main():
    matrix = maxtrify()
    word = 'XMAS'
    solve1(matrix, word)

main()
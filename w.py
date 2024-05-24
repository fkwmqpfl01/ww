def dfs(matrix, visited, x, y):
    # 상하좌우 네 방향으로 이동하기 위한 좌표 변화량
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = [(x, y)]
    size = 0
    
    while stack:
        cx, cy = stack.pop()
        if 0 <= cx < len(matrix) and 0 <= cy < len(matrix[0]) and not visited[cx][cy] and matrix[cx][cy] == '1':
            visited[cx][cy] = True
            size += 1
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                stack.append((nx, ny))
    
    return size

def find_largest_region(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    max_size = 0
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1' and not visited[i][j]:
                size = dfs(matrix, visited, i, j)
                max_size = max(max_size, size)
    
    return max_size

# 입력 데이터 처리
input_data = [
    "110010",
    "110010",
    "000100",
    "001000",
    "110000",
    "111000"
]

# 문자열 데이터를 리스트로 변환
matrix = [list(line) for line in input_data]

# 가장 큰 영역의 크기를 계산
largest_region_size = find_largest_region(matrix)
print("가장 큰 영역의 크기:", largest_region_size)
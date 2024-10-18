def solution(arr):
    def dfs(x,y, size):
        initial = arr[x][y]
        for i in range(x,x+size):
            for j in range(y,y+size):
                if arr[i][j]!= initial:
                    half = size//2 # 다른 값이 있으면 4개의 작은 영역으로 분할
                    top_left = dfs(x,y,half)
                    top_right = dfs(x,y+half, half)
                    bottom_left = dfs(x+half, y, half)
                    bottom_right = dfs(x+half, y+half, half)
                    return [top_left[0] + top_right[0] + bottom_left[0] + bottom_right[0],
                            top_left[1] + top_right[1] + bottom_left[1] + bottom_right[1]]
        return [1,0] if initial ==0 else [0,1]
    result = dfs(0, 0, len(arr))
    
    return result
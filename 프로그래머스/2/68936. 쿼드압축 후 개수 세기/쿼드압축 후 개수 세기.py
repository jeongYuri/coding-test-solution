def solution(arr):
    answer = [0,0]
    def compress(x,y,n):
        first = arr[x][y]
        same = True
        for i in range(x,x+n):
            for j in range(y,y+n):
                if arr[i][j]!=first:
                    same = False
                    break
            if not same:
                break
        if same:
            answer[first]+=1
            return
        half = n//2
        compress(x, y, half)
        compress(x, y + half, half)
        compress(x + half, y, half)
        compress(x + half, y + half, half)
            
    compress(0, 0, len(arr))
    return answer
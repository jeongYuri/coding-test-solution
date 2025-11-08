def solution(board, moves):
    answer = 0
    st = []
    for move in moves:
        col = move-1
        for row in range(len(board)):
            if board[row][col]!=0:
                doll = board[row][col]
                board[row][col] = 0
                
                if st and st[-1]==doll:
                    st.pop()
                    answer+=2
                else:
                    st.append(doll)
                break
                    
    return answer
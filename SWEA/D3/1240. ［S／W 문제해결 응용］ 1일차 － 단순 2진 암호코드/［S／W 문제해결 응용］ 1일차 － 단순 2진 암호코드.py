from collections import deque

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    pan = []
    for i in range(n):
        line = input().strip()
        pan.append(line)

    text = deque()
    for i in range(n):
        for j in range(m-1, -1, -1):
            if pan[i][j] == '1':
                for k in range(j, j-56, -1):
                    text.appendleft(pan[i][k])
                break
        if len(text) != 0:
            break

    string = ''
    code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    decode = []
    for i in range(1, 57):
        string += text[i-1]
        if i % 7 == 0:
            for j in range(10):
                if string == code[j]:
                    decode.append(j)
                    break
            string = ''

    odd, even = 0, 0
    result, answer = 0, 0
    for i in range(1, len(decode) + 1):
        if i % 2 == 1:
            odd += decode[i-1]
        else:
            even += decode[i-1]
    result = odd * 3 + even
    if result % 10 == 0:
        answer = sum(decode)
    else:
        answer = 0

    print(f'#{tc} {answer}')
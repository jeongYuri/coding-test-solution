import sys
input = sys.stdin.readline

while True:
    try:
        line = input().strip()  
        if not line: 
            break
        n, s = map(int, line.split())
        print(s // (n + 1))
    except EOFError:
        break
    except ValueError:
        continue

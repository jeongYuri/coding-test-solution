import sys
input = sys.stdin.readline

def find(remain):
    n = 0
    pt = 0
    while pt<len(remain):
        n +=1
        current_n = str(n)
        for char in current_n:
            if pt<len(remain) and char == remain[pt]:
                pt +=1
            if pt == len(remain):
                return n


word = input().strip()
print(find(word))
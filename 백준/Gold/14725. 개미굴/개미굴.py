import sys
input = sys.stdin.readline
from collections import defaultdict
n = int(input())
trie= lambda : defaultdict(trie)
root = trie()

for _ in range(n):
    arr = input().split()
    k = int(arr[0])
    cur =root  #루트에서 시작
    for word in arr[1:]:
        cur = cur[word]
def dfs(node, depth):
    for key in sorted(node.keys()):
        print("--"*depth+key)
        dfs(node[key],depth+1)
dfs(root,0)


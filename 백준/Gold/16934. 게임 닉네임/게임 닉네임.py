import sys
input = sys.stdin.readline
from collections import defaultdict

def insert_trie(root, word):
    node = root
    for ch in word:
        if ch not in node:
            node[ch] = {}
        node = node[ch]
    node['$'] = node.get('$', 0) + 1

n = int(input())
users = list(input().strip() for _ in range(n))
tries = {}
cnt = defaultdict(int)

for s in users:
    node = tries
    unique = None

    for i, ch in enumerate(s):
        if ch not in node:
            unique = s[:i+1]
            break
        node = node[ch]
    if unique is not None:
        print(unique)
        cnt[s]+=1
        insert_trie(tries,s)
    else:
        cnt[s]+=1
        x= cnt[s]
        if x==1:
            alias = s
        else:
            alias =  s+str(x)
        print(alias)
        insert_trie(tries,s)

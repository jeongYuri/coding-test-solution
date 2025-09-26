import sys

sys.setrecursionlimit(2000)
input = sys.stdin.readline

n, m = map(int, input().split())
data = [input().strip().split() for _ in range(n + m)]

q = int(input())
queries = [input().strip() for _ in range(q)]

fs = {"main": {'sub': {}, 'files': set()}}

for parent, name, isFolder in data:
    if parent not in fs:
        fs[parent] = {'sub': {}, 'files': set()}

    if isFolder == '1':
        if name not in fs:
            fs[name] = {'sub': {}, 'files': set()}
        fs[parent]['sub'][name] = name
    else:

        fs[parent]['files'].add(name)

def count_files(folder_name):

    node = fs[folder_name]

    types = set(node['files'])
    total = len(node['files'])

    for sub_folder_name in node['sub']:
        t, c = count_files(sub_folder_name)
        types |= t
        total += c

    return types, total

for path in queries:
    parts = path.split('/')
    final_folder_name = parts[-1]
    if final_folder_name in fs:
        types, total = count_files(final_folder_name)
        print(len(types), total)
    else:
        print(0, 0)
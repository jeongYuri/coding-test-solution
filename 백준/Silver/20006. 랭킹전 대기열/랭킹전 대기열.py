import sys
input = sys.stdin.readline

p,m = map(int,input().split())
player = []

for _ in range(p):
    level,n = input().split()
    player.append((int(level),n))

room = []
for level, name in player:
    placed = False
    for r in room:
        if len(r["players"]) < m and r["base"] - 10 <= level <= r["base"] + 10:
            r["players"].append((level, name))
            placed = True
            break
    if not placed:
        room.append({
            "base":level,
            "players":[(level, name)]
        })
for rom in room:
    if len(rom["players"]) == m:
        print("Started!")
    else:
        print("Waiting!")
    for lv, nm in sorted(rom["players"], key=lambda x: x[1]):
        print(lv, nm)
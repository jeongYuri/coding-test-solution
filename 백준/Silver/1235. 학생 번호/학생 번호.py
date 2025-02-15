import sys
input = sys.stdin.readline

n = int(input())
students = [input().strip() for _ in range(n)]

end = 1
while True:
    res = set()
    for student in students:
        res.add(student[-end:])#끝에서부터 end길이만큼
    if len(res) ==n:
        print(end)
        break

    end+=1



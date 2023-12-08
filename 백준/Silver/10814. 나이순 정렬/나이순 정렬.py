import sys
input = sys.stdin.readline

n = int(input())
people = []

for i in range(n):
    age, name = input().split()
    people.append((int(age), name, i))

people.sort(key=lambda member: (member[0], member[2]))

for person in people:
    print(person[0], person[1])
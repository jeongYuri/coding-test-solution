def custom_sort(member):
    return (member[0], member[2])

n = int(input())
people = []

for i in range(n):
    age, name = input().split()
    people.append((int(age), name, i))

people.sort(key=custom_sort)

for person in people:
    print(person[0], person[1])
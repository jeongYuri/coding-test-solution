import sys
input = sys.stdin.readline

school = int(input())
pc = int(input())
study = int(input())
home = int(input())
hour = (school+pc+study+home)//60
minute = (school+pc+study+home)%60
print(hour)
print(minute)
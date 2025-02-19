import sys

bill_values = {
    "Franklin": 100,
    "Grant": 50,
    "Jackson": 20,
    "Hamilton": 10,
    "Lincoln": 5,
    "Washington": 1
}

n = int(sys.stdin.readline().strip())  

for _ in range(n):
    bills = sys.stdin.readline().strip().split() 
    total = sum(bill_values[bill] for bill in bills)  
    print(f"${total}")  

import sys
input = sys.stdin.readline

L = int(input())     
N = int(input())     

expected = [0] * (N + 1)  
actual = [0] * (N + 1)    
cake = [0] * (L + 1)      

for i in range(1, N + 1):
    P, K = map(int, input().split())
    expected[i] = K - P + 1

    for j in range(P, K + 1):
        if cake[j] == 0:
            cake[j] = i
            actual[i] += 1

max_expected = max(expected)
expected_idx = expected.index(max_expected)

max_actual = max(actual)
actual_idx = actual.index(max_actual)

print(expected_idx)
print(actual_idx)

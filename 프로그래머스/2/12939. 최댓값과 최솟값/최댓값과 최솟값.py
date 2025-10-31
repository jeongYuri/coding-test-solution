def solution(s):
    arr = list(map(int, s.split()))
    mins = min(arr)
    maxs = max(arr)
    ans = ' '.join(map(str, [mins, maxs]))
    return ans
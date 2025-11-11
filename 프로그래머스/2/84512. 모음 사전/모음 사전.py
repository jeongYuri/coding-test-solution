from itertools import product
def solution(word):
    words = []
    for i in range(1,6):
        for p in product("AEIOU",repeat = i):
            words.append(''.join(p))
    words.sort()
    return words.index(word)+1
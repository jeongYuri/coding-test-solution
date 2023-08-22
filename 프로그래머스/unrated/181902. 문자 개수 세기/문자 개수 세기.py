from collections import Counter

def solution(my_string):
    counter = Counter(my_string)
    result = []
    
    for char in range(ord('A'), ord('Z') + 1):
        result.append(counter.get(chr(char), 0))
    
    for char in range(ord('a'), ord('z') + 1):
        result.append(counter.get(chr(char), 0))
    
    return result
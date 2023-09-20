def solution(cacheSize, cities):
    import collections
    time = 0
    cache = collections.deque(maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            time +=1
        else:
            cache.append(city)
            time +=5
    return time
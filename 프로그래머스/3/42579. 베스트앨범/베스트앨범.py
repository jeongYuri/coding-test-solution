def solution(genres, plays):
    answer = []
    count = {}
    music = {}
    for i in range(len(genres)):
        key = genres[i]
        value = plays[i]
        if key not in music:
            count[key]=value
            music[key] = [(i,value)]
        else:
            count[key]+=value
            music[key].append((i,value))
    sorted_genre = sorted(count.keys(),key= lambda x:count[x], reverse=True)
    
    for sg in sorted_genre:
        song = music[sg]
        song = sorted(song,key = lambda x:(-x[1],x[0]))
        
        for i in range(min(2,len(song))):
            answer.append(song[i][0])
    return answer
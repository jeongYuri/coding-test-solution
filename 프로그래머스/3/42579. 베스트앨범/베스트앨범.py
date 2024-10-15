from collections import defaultdict
def solution(genres, plays):
    ans = []
    cnt = defaultdict(int)
    music = defaultdict(list)
    for i ,(genre,play) in enumerate(zip(genres, plays)):
        cnt[genre] += play
        music[genre].append((i,play))
    sorted_g = sorted(cnt.keys(),key = lambda x:cnt[x],reverse = True)
    for sg in sorted_g:
        song = music[sg]
        song = sorted(song,key = lambda x:(-x[1],x[0]))
        for i in range(min(2,len(song))):
            ans.append(song[i][0])
    return ans
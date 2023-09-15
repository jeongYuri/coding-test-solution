def solution(n, words):
    al = [words[0][0]]    
    for i, w in enumerate(words):
        if w not in al and al[-1][-1] == w[0] : 
            al.append(w)
        else:
            return [i%n+1, i//n+1]
    return [0,0]
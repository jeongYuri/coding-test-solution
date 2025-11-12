def solution(genres, plays):
    genre_to_songs = {}     
    genre_total_plays = {}  
    answer = []             

    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genre_to_songs:
            genre_to_songs[genre] = [(idx, play)]
        else:
            genre_to_songs[genre].append((idx, play))

        if genre not in genre_total_plays:
            genre_total_plays[genre] = play
        else:
            genre_total_plays[genre] += play

    for genre, _ in sorted(genre_total_plays.items(), key=lambda x: x[1], reverse=True):
        top_songs = sorted(genre_to_songs[genre], key=lambda x: (-x[1], x[0]))[:2]
        for song_index, _ in top_songs:
            answer.append(song_index)

    return answer

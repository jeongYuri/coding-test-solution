def solution(info, n, m):  
    states = set([(0, 0)])  

    for a_trace, b_trace in info:
        next_states = set()

        for a_total, b_total in states:
            if a_total + a_trace < n:
                next_states.add((a_total + a_trace, b_total))
            if b_total + b_trace < m:
                next_states.add((a_total, b_total + b_trace))

        if next_states:
            states = next_states
        else:
            return -1 

    return min(a_total for a_total, _ in states)

def solution(s):
    def is_valid(string):
        st = []
        for w in string:
            if not st:              
                st.append(w)
                continue

            if (st[-1] == '(' and w == ')') or \
               (st[-1] == '{' and w == '}') or \
               (st[-1] == '[' and w == ']'):
                st.pop()
            else:
                st.append(w)

        return len(st) == 0  

    answer = 0
    for i in range(len(s)):        
        rotated = s[i:] + s[:i]
        if is_valid(rotated):
            answer += 1
    return answer

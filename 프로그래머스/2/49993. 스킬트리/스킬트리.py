def solution(skill, skill_trees):
    cnt = 0
    for tree in skill_trees:
        st = list(reversed(skill))
        valid = True
        
        for s in tree:
            if s in skill:
                if s==st[-1]:
                    st.pop()
                else:
                    valid = False
                    break
        if valid: cnt+=1
    return cnt
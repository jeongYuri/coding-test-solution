def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    start_time = h1*3600+m1*60+s1
    end_time = h2*3600+m2*60+s2
    
    if start_time ==0 * 3600 or start_time == 12*3600:
        answer+=1
    
    while start_time<end_time:
        h_angle = start_time/120%360
        m_angle = start_time/10%360
        s_angle = start_time*6%360
        
        h_next = 360 if (start_time+1)/120%360==0 else(start_time+1)/120%360
        m_next = 360 if (start_time+1)/10%360==0 else(start_time+1)/10%360
        s_next = 360 if (start_time+1)*6%360==0 else(start_time+1)*6%360
        
        if s_angle<h_angle and s_next>= h_next:
            answer+=1
        if s_angle<m_angle and s_next>=m_next:
            answer+=1
        if s_next==h_next or h_next==m_next :
            answer-=1
        start_time+=1
    return answer
            
        
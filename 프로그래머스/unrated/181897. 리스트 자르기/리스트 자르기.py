def solution(n, slicer, num_list):
        for _ in slicer:
            a,b,c=slicer[0],slicer[1],slicer[2]
            if n==1:
                return num_list[0:b+1] 
            elif n==2:
                return num_list[a:]
            elif n==3:
                return num_list[a:b+1]
            else:
                return num_list[a:b+1:c]

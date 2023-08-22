def solution(strArr):
    answer = 0
    text_dict = {}
    for text in strArr:
        length = len(text)
        if length in text_dict:
            text_dict[length]+=1
        else:
            text_dict[length]=1
    max_count = max(text_dict.values())
    return max_count
        
  
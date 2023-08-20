import re
def solution(myStr):
    parts = re.split("[abc]",myStr)
    answer = [part for part in parts if part!=""]
    if not answer:
        return ["EMPTY"]
    return answer
from itertools import permutations

def solution(expression):
    susic = []
    temp = ""
    for i in expression:
        if i.isdigit():
            temp += i
        else:
            if temp:
                susic.append(int(temp))  
                temp = ""
            susic.append(i)  
    if temp:
        susic.append(int(temp))  

    def calculate(priority, susic):
        for op in priority:  
            stack = []
            i = 0
            while i < len(susic):
                if susic[i] == op:  
                    prev = stack.pop()  
                    next_val = susic[i + 1]  
                    if op == '+':
                        stack.append(prev + next_val)
                    elif op == '-':
                        stack.append(prev - next_val)
                    elif op == '*':
                        stack.append(prev * next_val)
                    i += 1 
                else:
                    stack.append(susic[i])  
                i += 1
            susic = stack  
        return abs(susic[0])  

    operations = ['+', '-', '*']
    priorities = permutations(operations)
    max_res = 0
    for priority in priorities:
        res = calculate(priority, susic[:])  
        max_res = max(max_res, res)
    
    return max_res


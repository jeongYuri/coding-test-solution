def solution(todo_list, finished):
    answer=[]
    dict_todo = { x:y for x, y in zip(todo_list,finished)}
    for key, value in dict_todo.items():
        if not value: 
            answer.append(key)        
    return answer

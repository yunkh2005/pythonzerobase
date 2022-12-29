def solution(array, commands):
    answer = []
    for index in range(len(commands)):
        i = commands[index][0]
        j = commands[index][1]
        k = commands[index][2]
        
        copy = sorted(array[i-1:j])
        answer.append(copy[k-1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))
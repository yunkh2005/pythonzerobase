def solution(participant, completion):
    if len(participant) == 1:
        return []
    
    i = 0
    while len(participant) != 1:
        if participant[i] in completion:
            completion.pop(completion.index(participant[i]))
            participant.pop(participant.index(participant[i]))
        else:
            i += 1

    return participant[0]

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant, completion))

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))
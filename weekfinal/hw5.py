def solution(words, queries):
    result = [0 for _ in range(len(queries))]
    for i in range(len(queries)):
        check = False
        for j in range(len(words)):
            if len(queries[i]) != len(words[j]):
                continue
            else:
                for k in range(len(queries[i])):
                    if queries[i][k] == '?':
                        continue
                    elif queries[i][k] == words[j][k]:
                        check = True
                    else:
                        check = False
                
                if check:
                    result[i] += 1
    
    return result

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))     # [3, 2, 4, 1, 0]
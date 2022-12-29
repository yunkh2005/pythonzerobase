words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
result = [0 for _ in range(len(queries))]

for i in range(len(queries)):
    check = False
    for j in range(len(words)):
        if len(queries[i]) != len(words[j]):
            continue
        else:
            #print(i, queries[i], j, words[j])
            print(queries[i], words[i])
            for k in range(len(queries[i])):
                if queries[i][k] == '?':
                    continue
                elif queries[i][k] == words[j][k]:
                    print(True)
                    check = True
                else:
                    print(False)
                    check = False
            
            if check:
                result[i] += 1
                print(result[i])
print(*result)


def solution(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0

    
    return 1

print(solution("hit", "cog", ["hot","dot","dog","lot","log","cog"]))        # 5
print(solution("hit", "cog", ["hot","dot","dog","lot","log"]))              # 0
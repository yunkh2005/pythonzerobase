'''
과제 4

2개의 단어 beginWord와 endWord, 
그리고 여러개의 단어 wordList가 주어졌을 때, 
beginWord에서 endWord로 변환하기 위해 필요한 
가장 적은 변환 횟수를 구하시오.

변환 조건
- 단어는 wordList에 있는 단어로만 변환할 수 있다.
- 단어를 변환할 때에는 한번에 하나씩의 문자만 바꿀 수 있다.

문제 조건
- endWord로의 변환이 불가한 경우에는 0을 출력하시오.
- 문제에 등장하는 모든 단어의 길이는 같으며, 알파벳 소문자로만 이루어져 있다.
- wordList에는 겹치는 단어가 없다.
- beginWord와 endWord는 같은 단어로 주어지지 않는다.

예시 입력1
입력:
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]
출력: 5
설명: 가장 짧은 변환 방법은 "hit" -> "hot" -> "dot" -> "dog" -> "cog"이다.

예시 입력2
입력:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
출력: 0
설명: endWord인 "cog"가 wordList에 없으므로, endWord로 변환할 수 있는 방법이 없다.
'''

def isAdj(s1, s2):
    count = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            count += 1
        if count > 1:
            return False
    return count == 1

    
def solution(beginWord, endWord, wordList):
      adjMap = {w: list(filter(lambda ww: isAdj(w, ww), wordList)) for w in wordList}
      adjList = list(filter(lambda w: isAdj(beginWord, w), wordList))
      visited = set()
      queue = list(map(lambda x: (1, x), adjList))

      while len(queue) > 0:
          count, word = queue.pop()

          if word == endWord:
              return count + 1

          if word not in visited:
              visited.add(word)
              queue = list(map(lambda x: (count + 1, x), adjMap[word])) + queue

      return 0

print(solution("hit", "cog", ["hot","dot","dog","lot","log","cog"]))        # 5
print(solution("hit", "cog", ["hot","dot","dog","lot","log"]))              # 0
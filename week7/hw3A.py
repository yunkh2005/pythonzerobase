'''
과제 3

문자열 s1, s2, s3가 주어졌을 때, 
문자열 s3가 문자열 s1과 s2를 교차로 배치하여 만들어질 수 있는지 여부를 출력하라.

예시 입력1
입력: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
출력: True

예시 입력2
입력: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
출력: False
'''

def solution(s1, s2, s3):
    found = False

    def dfs(str1, str2, str3):
        nonlocal found
        n, m = len(str1), len(str2)

        if found is True:
            return

        if str3 == s3:
            found = True
            return

        if n > 0 and str1[0] == s3[len(str3)]:
            dfs(str1[1:], str2, str3 + str1[0])

        if m > 0 and str2[0] == s3[len(str3)]:
            dfs(str1, str2[1:], str3 + str2[0])

    dfs(s1, s2, '')
    return found

print(solution("aabcc", "dbbca", "aadbbcbcac"))     # True
print(solution("aabcc", "dbbca", "aadbbbaccc"))     # False
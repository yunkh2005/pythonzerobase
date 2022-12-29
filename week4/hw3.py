def solution(a):
    str = []
    for i in range(len(a) - 1):
        print("a[i]:", a[i], "a[i+1]:", a[i+1])
        if len(a[i]) >= len(a[i + 1]):          # 앞 문자열이 더 길 때
            for j in range(len(a[i + 1])):      # 더 짧은 뒷 문자열 길이만큼 비교
                print("1 a[i][j]:", a[i][j], "a[i+1][j]:", a[i+1][j])
                if a[i][j] == a[i + 1][j]:      # 문자가 같으면
                    print("+", a[i][j])
                    str.append(a[i][j])         # str 리스트에 저장
                    print("1 str:", str)
                else:                           # 문자가 같지 않으면
                    break                       # for_j 반복문 종료

        else:                                   # 뒷 문자열이 더 길 때
            for j in range(len(a[i])):          # 더 짧은 앞 문자열 길이만큼 비교
                print("2 a[i][j]:", a[i][j], "a[i+1][j]:", a[i+1][j])
                if a[i][j] == a[i + 1][j]:      # 문자가 같으면
                    print("+", a[i][j])
                    str.append(a[i][j])         # str 리스트에 저장
                    print("2 str: ", str)
                else:                           # 문자가 같지 않으면
                    break                       # for_j 반복문 종료

        str = list(set(str))                              # str 리스트 중복 제거
    same_str = ''.join(str)                     # str안 요소들 한 문자열로 합치기

    # same_str이 a의 요소들에 모두 들어있는지
    # for i in a:
    #     if same_str not in i:
    #         return 0

    print(str)
    return len(str)

# Test code
print(solution(['abcd', 'abce', 'abchg', 'abcfwqw', 'abcdfg'])) # 3
print(solution(['abcd', 'gbce', 'abchg', 'abcfwqw', 'abcdfg'])) # 0
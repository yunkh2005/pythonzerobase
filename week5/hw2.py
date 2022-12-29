def gcdString(A, B):
    if not A or not B:
        return A if A else B
    elif len(A) < len(B):
        return gcdString(B, A)
    elif A[:len(B)] == B:
        return gcdString(A[len(B):], B)
    else:
        return ''

A = 'ababcde'
B = 'ababcde'
print(gcdString(A, B))      # 'ababcde'

A = 'ababababab'
B = 'abab'
print(gcdString(A, B))      # 'ab'

A = 'abababab'
B = 'abab'
print(gcdString(A, B))      # 'abab'

A = 'fast'
B = 'campus'
print(gcdString(A, B))      # ''
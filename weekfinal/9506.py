T = 0
divisors = []

while True:
    T = int(input())
    N = 0
    divisors.clear()

    if T == -1:
        break

    while N != T:
        N += 1
        if T % N == 0:
            divisors.append(N)
    
    if sum(divisors[:len(divisors)-1]) == T:
        print(T, "= ", end='')
        for i in range(len(divisors) - 2):
            print(divisors[i], "+ ", end='')
        print(divisors[-2])
    else:
        print(T, "is NOT perfect.")
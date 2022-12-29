def int_sum(*args):
    try:
        for n in args:
            sum += n
    except:
        print('error')
    
    return sum

result = int_sum(1, 2, 3)
print(result)
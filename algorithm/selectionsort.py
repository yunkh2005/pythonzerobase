import random

def selection(data):
    for i in range(len(data)-1):
        low = i
        for j in range(i+1, len(data)):
            if data[low] > data[j]:
                low = j
        data[low], data[i] = data[i], data[low]
    
    return data

data_list = random.sample(range(100), 10)
print("before", data_list)
print("after", selection(data_list))

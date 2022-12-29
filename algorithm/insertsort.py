import random

def insert(data):
    for i in range(len(data) - 1):
        for j in range(i+1, 0,-1):
            if data[j] < data[j-1]:
                data[j], data[j-1] = data[j-1], data[j]
            else:
                break

    return data

data_list = random.sample(range(100), 10)
print ("before",data_list)
print ("after", insert(data_list))
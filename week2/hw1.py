f = open('./week2/a.csv', 'r')
content = f.read()

num = map(int, list(content.split(',')))
print(sum(num))

f.close()
def searchMatrix(matrix, target):
    return False if all(target not in i for i in matrix) else True

#Test Code
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
print(searchMatrix(matrix, target))     # True
target = 13
print(searchMatrix(matrix, target))     # False
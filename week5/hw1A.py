'''
과제 1
이진 탐색법은 정렬된 자료를 탐색하는 데에 사용할 수 있다. 
이진탐색을 이용하여 인덱스가 낮을 수록 더 작은 값으로 정렬된 2차원 리스트에서 `target`을 찾으면 True를 반환하고, 
`target`을 찾을 수 없으면 False를 반환하는 프로그램을 작성하시오.

def searchMatrix(matrix, target):
    pass

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
'''

def searchMatrix(matrix, target):
  def searchRow(sub_matrix):
      m = len(sub_matrix)
      if m == 1:
          return sub_matrix[0]
      mid = m // 2
      left = sub_matrix[:mid]
      right = sub_matrix[mid+1:]
      if sub_matrix[mid][0] <= target <= sub_matrix[mid][-1]:
          return sub_matrix[mid]
      elif sub_matrix[mid][0] > target:
          return searchRow(left)
      else:
          return searchRow(right)
  def searchCol(array):
      n = len(array)
      if n == 0:
          return False
      if n == 1:
          if array[0] == target:
              return True
          else:
              return False
      mid = n // 2
      left = array[:mid]
      right = array[mid+1:]
      if array[mid] == target:
          return True
      elif array[mid] > target:
          return searchCol(left)
      else:
          return searchCol(right)
  array = searchRow(matrix)
  return searchCol(array)
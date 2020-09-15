# import random
# size = [0]
#
# def genSize(M, aveSize):
#   # M the number of objects
#   # aveSize an integer
#   problemList = [M+1]
#   for i in range(M):
#     problemList[i] = random.randint(1, 2*aveSize)
#   return problemList
#
#
# def knap(n, m):
#   # linear storage of size n
#   # m objects linear size of ints
#   # this returns a bool of if the list of sizes can fit in a storage of size n exactly full
#   if n == 0:
#     return True
#   if m == 0:
#     return False
#   if n < 0:
#     return False
#   return knap(n, m - 1) or knap(n - size[m], m - 1)
#
#
# size = [0, 99, 2 , 3, 4, 5, 6, 7, 8, 9, 10]
# print(size)
# print("of above list expected is: False")
# print("algorithm output: " + str(knap(100, len(size) -1)))
#
# size = [0, 99, 1 , 3, 4, 5, 6, 7, 8, 9, 10]
# print(size)
# print("of above list expected is: True")
# print("algorithm output: " + str(knap(100, len(size) -1)))
#
# size = [0, 97, 38 , 3, 4, 5, 6, 7, 8, 9, 10]
# print(size)
# print("of above list expected is: True")
# print("algorithm output: " + str(knap(100, len(size) -1)))
#
#
# def knapDP(n, m):
#   # linear storage of size n
#   # m objects linear size of ints
#   # this returns a bool of if the list of sizes can fit in a storage of size n exactly full
#   cache = [n][m]
#   for i in range(n):
#       for j in range(m)
#           if n == 0:
#             cache[i][j] = True
#             return True
#           elif m == 0:
#             cache[i][j] = False
#           elif n < 0:
#             cache[i][j] = False


def knapMemo(n, m):
  # linear storage of size n
  # m objects linear size of ints
  # this returns a bool of if the list of sizes can fit in a storage of size n exactly full
  global Cache
  if [n][m] in Cache:
    return Cache[n][m]
  if n == 0:
    Cache[n][m] = True
    return True
  elif m == 0:
    Cache[n][m] = False
    return False
  elif n < 0:
    Cache[n][m] = False
    return False
  return knapMemo(n, m - 1) or knapMemo(n - size[m], m - 1)

size = [0, 99, 2 , 3, 4, 5, 6, 7, 8, 9, 10]
print(size)
print("of above list expected is: False")
print("algorithm output: " + str(knapMemo(100, len(size) -1)))

size = [0, 99, 1 , 3, 4, 5, 6, 7, 8, 9, 10]
print(size)
print("of above list expected is: True")
print("algorithm output: " + str(knapMemo(100, len(size) -1)))

size = [0, 97, 38 , 3, 4, 5, 6, 7, 8, 9, 10]
print(size)
print("of above list expected is: True")
print("algorithm output: " + str(knapMemo(100, len(size) -1)))


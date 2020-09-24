import time
import matplotlib.pyplot as plt
import random
from scipy import stats
import numpy as np
import string

path = ""
fileName = "covid_DNA.fasta"

import numpy as np
import time
import matplotlib.pyplot as plt

def read_fasta(howMany = 10):
    # The first line in a FASTA record is the title line.
    # Examples:
    # >third sequence record
    # >gi|2765657|emb|Z78532.1|CCZ78532 C.californicum 5.8S rRNA gene
    # returns a list of sequences as tuples (name.)
    with open(path + fileName,  'r') as filePt:
        sequences = []
        fastas = filePt.read().split(">")
        fastas = fastas[1:]
        for i in range(0,howMany):
            seq = fastas[i].split("\n")
            seq_name = seq[0]
            fasta_seq = "".join(seq[1:])
            sequences.append((seq_name,fasta_seq))
        return sequences

##Calculates the time taken by each function call and generates graph
def timeProblems(problemList, function, init = None, fit = 'exponential'):
  #problemList is a list of tuples [(size, arguments),...] ordered smallest to biggest
  #runs and times the function with each arguments a
  #generates a graph of run time as a function of problem size
  # fit may be 'exponential' then the time as a function of problem size is assumed
  #     to of the form time = c * a^n and the function solves for c and a
  #     where a is the base of the exponential function and c is a multiplicative factor
  # fit my be 'polynomial' then the time as a function of problem size is assumed
  #     to of the form time = c * n ^ b and the function solves for c and b
  #     where b is the power of n (the degree of the polynomial) and c is a multiplicative fac* tor
    timeLine = []
    values = []
    for (size, args) in problemList:
      start_time = time.time()
      function(*args) #use the * to unpack the tuple into arguments to the function
      elapsed = (time.time() - start_time)*1000.0
      if elapsed > 0.0:
        timeLine.append(elapsed)
        values.append(size)
    ##Generating the plot between time taken by each function call with n as variable and n
    plt.plot(values, timeLine, 'g')
    plt.xlabel("Problem size")
    plt.yscale('log')
    if fit == 'polynomial':
      plt.xscale('log')
    plt.ylabel("time in milliseconds")
    plt.rcParams["figure.figsize"] = [16,9]
    plt.show()
    if fit == 'exponential': #fit a straight line to n and log time
        slope, intercept, _, _, _ = stats.linregress([values], [np.log(t) for t in timeLine])
        print("time = %.6f * %.3f ^ n" % (np.exp(intercept), np.exp(slope)))
    elif fit == 'polynomial': # fit a straight line to log n and log time
        slope, intercept, _, _, _ = stats.linregress([np.log(v) for v in values], [np.log(t) for t in timeLine])
        print("time = %.6f * n ^ %.3f" % (np.exp(intercept), slope))


seq = read_fasta(3)
(name0, seq0) = seq[0]
(name1, seq1) = seq[1]

maxi = [[5,-1,-2,-1,-3],[-1,5,-3,-2,-4],[-2, -3, 5, -2, -2],[-1,-2,-2,5,-1],[-3,-4,-2,-1,5]]

def matchR(A, B):
    #uses recursion to solve the string matching problem
    # mod the strings to put a blank in front so that n and m represent both
    # the number of characters in the string AND the index into the string
    n = len(A)
    m = len(B)
    A = '_' + A
    B = '_' + B
    return match(n, m, A, B)

def match(n, m, A, B):
  # one of the strings is empty
  if n == 0:
    return m
  if m == 0:
    return n
  # three cases
  return min(match(n-1, m, A, B) + 1, #delete from A
             match(n, m-1, A, B) + 1, #delete from B
             match(n-1,m-1, A, B) + int(A[n] != B[m])) #substitute

def printAlign(A, B):
    n = len(A)
    m = len(B)
    A = '_' + A
    B = '_' + B
    alignment = traceback(n, m, A, B)
    alignment.reverse()
    for oneAlign in alignment:
      print(oneAlign)

def traceback(n, m, A, B):
  # n is in A, m is in B
  # base case
  # nothing to do, return empty
  if n == 0 and m == 0:
    return []
  # no characters in A, so add a delete from A and continue
  if n == 0:
    # delete from A
    return ["%s - %s" % ('_', B[m])] + traceback(n, m-1, A, B)
  # no characters in B, so delete from B and continue
  if m == 0:
    # delete from B
    return ["%s - %s" % (A[n], '_')] + traceback(n-1, m, A, B)
  # Need to determine which alignment sub solution was used for the optimal solution
  sol = cache[(n, m)]
  # we know that sol must equal one of the sub solutions
  if sol == cache[(n-1, m)] + 1: #delete from B
     return ["%s - %s" % (A[n], '_')] + traceback(n-1, m, A, B)
  if sol == cache[(n, m-1)] + 1: #delete from A
     return ["%s - %s" % ('_', B[m])] + traceback(n, m-1, A, B)
  # must have matched the characters, check the characters
  if A[n] != B[m]: # substitution
     return ["%s x %s" % (A[n], B[m])] + traceback(n-1, m-1, A, B)
  # exact match
  return ["%s = %s" % (A[n], B[m])] + traceback(n-1, m-1, A, B)

def matchDP(A, B):
    #takes two strings and returns the minimum edit distance between them
    global cache
    cache = {}
    n = len(A)
    m = len(B)
    # mod the strings to put a blank in front
    A = '_' + A
    B = '_' + B
    # fill in the base cases
    for i in range(0, m+1):
      cache[(0, i)] = i
    for j in range(0, n+1):
      cache[(j, 0)] = j
    # loop though all problems from smallest to biggest
    # what about the 0 0 case?
    for i in range(1, m+1):
      for j in range(1, n+1):
        # need to change the indexs into the array!
        # so from n in recursion to j and from m in recursion to i
        cache[(j, i)] = min(cache[(j-1, i)] + 1, cache[(j, i-1)] + 1, cache[(j-1,i-1)] + int(A[j] != B[i]))
    return cache[(n, m)]

def genStr(n, chars = None):
  if chars is None:
    chars = string.ascii_lowercase
  return  ''.join(random.choice(chars) for i in range(n))

def generateProblems(start, end, increment):
  # generates problems described as (size, (randstring, randstring))
  return [(i, (genStr(i), genStr(i))) for i in range(start, end, increment)]

#TEST correctness of code
A = 'ACGGAGAGAATC'
B = 'TGGAGAGAATTC'

#match to fill in the cache
# edit = matchDP(A, B)
# printAlign(A, B)

seq = read_fasta(3)
(name0, seq0) = seq[0]
(name1, seq1) = seq[1]

edit = matchDP(seq0, seq1)
printAlign(seq0, seq1)


# Pass = True
# for i in range(0, 10):
#   A = genStr(10, ['a', 'b', 'c'])
#   B = genStr(10, ['a', 'b', 'c'])
#   Pass = Pass and matchR(A,B) == matchDP(A,B)
# if Pass:
#   print("Pass")
# else:
#   print('Fail')


# TEST THE TIMING OF THE CODE
#test the recursive version on small problems
smallProblems = generateProblems(2, 12, 1)
# timeProblems(smallProblems, matchR, fit = 'exponential')

bigProblems = generateProblems(2, 2002, 100)
#since we expect the DP algorithm to be polynomial
timeProblems(bigProblems, matchDP, fit = 'polynomial')

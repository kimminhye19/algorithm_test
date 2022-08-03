def exchange (n, S):
  for i in range(1,n):
    for j in range(i+1, n+1):
      if (S[j] < S[i]):
        S[i], S[j] = S[j], S[i]
    print(S)

S = [-1, 10, 8, 23, 1]
print(S)
exchange(len(S)-1, S)
print(S)


def matrixmult (n, A, B):
  n = len(A)
  C = [[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      for k in range(n):
        C[i][j] += A[i][k] * B[k][j]
  return C

A = [[2,3],[4,1]]
B = [[5,7],[6,8]]
C = matrixmult(len(A),A,B)
print(C)
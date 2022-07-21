'''
做题，三个长度为N的数组A，B，C，正整数，无序。
求 A[i] + B[j] + C[k] = 64的(i , j, k )的组合总数。要求时间O(N), 空间O(1)
'''
def find(A,B,C):
    countA = [0] * 65
    countB = [0] * 65
    countC = [0] * 65
    n = len(A)
    for i in range(n):
        if A[i] <= 64:
            countA[A[i]] += 1
        if B[i] <= 64:
            countB[B[i]] += 1
        if C[i] <= 64:
            countC[C[i]] += 1
    res = 0
    for i in range(65):
        for j in range(65 - i):
            res += countA[i] * countB[j] * countC[64-i-j]
    return res

if __name__ == '__main__':
    A = [64,1]
    B = [0,1]
    C = [0,1]
    print(find(A,B,C))
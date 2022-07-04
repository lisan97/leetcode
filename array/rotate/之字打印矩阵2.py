"""
n = 4

1  2  6  7
3  5  8  13
4  9  12 14
10 11 15 16

"""
def z_print(n):
    matrix = [[0] * n for _ in range(n)]
    down_x, down_y = 0, 0  #下边界
    right_x,right_y = 0, 0 #右边界
    up = True
    num = 1
    while right_x < n:
        num = corner_print(matrix,down_x,down_y,right_x,right_y,up,num)
        #当下边界到底时开始往右移动
        if down_x < n-1:
            down_x += 1
        else:
            down_y += 1
        #当右边界到最右时开始往下移动
        if right_y < n-1:
            right_y += 1
        else:
            right_x += 1
        up = not up
    return matrix

def corner_print(matrix,down_x,down_y,right_x,right_y,up,num):
    #斜向上遍历
    if up:
        while down_x > right_x - 1:
            matrix[down_x][down_y] = num
            down_x -= 1
            down_y += 1
            num += 1
    #斜向下遍历
    else:
        while right_x < down_x + 1:
            matrix[right_x][right_y] = num
            right_x += 1
            right_y -= 1
            num += 1
    return num

if __name__ == '__main__':
    n = 4
    matrix = z_print(n)
    print(matrix)
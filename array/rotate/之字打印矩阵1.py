'''
给你一个matrix
输出之字打印的结果
'''

def z_print(matrix):
    down_x,down_y = 0,0
    right_x,right_y= 0,0
    m = len(matrix)
    n = len(matrix[0])
    up = True
    res = []
    while right_x < m:
        corner_print(matrix,down_x,down_y,right_x,right_y,up,res)
        if down_x < m - 1:
            down_x += 1
        else:
            down_y += 1
        if right_y < n - 1:
            right_y += 1
        else:
            right_x += 1
        up = not up
    return res

def corner_print(matrix,down_x,down_y,right_x,right_y,up,res):
    if up:
        while down_x > right_x - 1:
            res.append(matrix[down_x][down_y])
            down_x -= 1
            down_y += 1
    else:
        while right_x < down_x + 1:
            res.append(matrix[right_x][right_y])
            right_x += 1
            right_y -= 1

if __name__ == '__main__':
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(z_print(matrix))
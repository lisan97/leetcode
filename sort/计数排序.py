def counting_sort(array):
    if len(array) < 2:
        return array
    max_num = max(array)
    min_num = min(array)
    count = [0] * (max_num - min_num + 1)  # 万一最大值和最小值差太多，会比较浪费空间复杂度，优化：从min_value开始构建结数列表
    for num in array:
        count[num - min_num] += 1
    i = 0
    for j in range(len(count)):
        while count[j] > 0:
            array[i] = j + min_num
            count[j] -= 1
            i += 1
    return array

if __name__ == '__main__':
    array = [1,1,1,7,4,3,3,8]
    print(counting_sort(array))
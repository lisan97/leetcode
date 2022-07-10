import math

def cal_ang(point_1, point_2, point_3):
    """
    根据三点坐标计算夹角
    :param point_1: 点1坐标
    :param point_2: 点2坐标
    :param point_3: 点3坐标
    :return: 返回任意角的夹角值，这里只是返回点2的夹角
    """
    a=math.sqrt((point_2[0]-point_3[0])**2+(point_2[1]-point_3[1])**2)
    b=math.sqrt((point_1[0]-point_3[0])**2+(point_1[1]-point_3[1])**2)
    c=math.sqrt((point_1[0]-point_2[0])**2+(point_1[1]-point_2[1])**2)
    A=math.degrees(math.acos((a*a-b*b-c*c)/(-2*b*c)))
    B=math.degrees(math.acos((b*b-a*a-c*c)/(-2*a*c)))
    C=math.degrees(math.acos((c*c-a*a-b*b)/(-2*a*b)))
    return A,B,C

if __name__ == '__main__':
    print(cal_ang((0, 0), (1, 1), (0, 1)))
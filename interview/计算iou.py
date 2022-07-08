def calculate(rect1,rect2):
    a_x1,a_y1,a_x2,a_y2 = rect1
    b_x1, b_y1, b_x2, b_y2 = rect2
    x = min(a_x2,b_x2) - max(a_x1,b_x1)
    y = min(a_y2,b_y2) - max(a_y1,b_y1)
    if x <= 0 or y <= 0:
        return 0
    else:
        a_area = (a_x2-a_x1) * (b_x2-b_x1)
        b_area = (b_x2-b_x1) * (b_y2-b_y1)
        intersection = x * y
        return intersection / (a_area+b_area-intersection)
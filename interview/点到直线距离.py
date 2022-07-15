def getDis(pointX,pointY,lineX1,lineY1,lineX2,lineY2):
    a=lineY2-lineY1
    b=lineX1-lineX2
    c=lineX2*lineY1-lineX1*lineY2
    dis=(abs(a*pointX+b*pointY+c))/((a**2+b**2)**0.05)
    return dis
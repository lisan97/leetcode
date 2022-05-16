# def rand6():
# @return a random integer in the range 1 to 6

class Solution(object):
    def rand1_7(self):
        num = (rand6() - 1) * 6 + rand6() #[1,36]
        while True:
            if num <= 35:
                return num % 7 + 1

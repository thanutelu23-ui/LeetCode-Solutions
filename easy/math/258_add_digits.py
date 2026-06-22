class Solution(object):
    def addDigits(self, num):
        if num<10:
            return num
        while num>9:
            sum_digits=0
            while num!=0:
                r=num%10
                sum_digits+=r
                num=num//10
            num=sum_digits
        return sum_digits
        
""" This Program will take Decimal Number and convert it in Binary """
class DecBin(object):
    """ This Class will convert Decimal to Binary Number """
    def __init__(self, dec_num):
        self.dec_num = dec_num
    def dec_bin(self):
        """ This method will convert Decimal to Binary """
        b_rem = []
        qut = self.dec_num/2
        while qut >= 1:
            qut = self.dec_num/2
            rem = self.dec_num%2
            self.dec_num = qut
            b_rem.append(rem)
        print "Decimal Number is %s" %("".join(str(i) for i in b_rem[::-1]))

DEC_NUM = DecBin(int(raw_input("Enter Decimal Number : ")))
DEC_NUM.dec_bin()

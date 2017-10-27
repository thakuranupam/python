""" This Program will take Binary Number and convert it in Decimal """
class BinDec(object):
    """ This Class will convert Binary to Decimal Number"""
    def __init__(self, bin_num):
        self.bin_num = bin_num
    def bin_dec(self):
        """ This method will convert Binary to Decimal """
        j = len(self.bin_num) - 1
        dec = 0
        for i in self.bin_num:
            dig = int(i) * 2**j
            dec = dec + dig
            j -= 1
            return dec

BIN_NUM = raw_input("Enter Binary Number : ")
BIN_LIST = BinDec(list(BIN_NUM))
print "Binary Number : ", BIN_NUM, " \nDecimal Number : ", BIN_LIST.bin_dec()

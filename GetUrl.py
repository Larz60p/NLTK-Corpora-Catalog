import urllib.request as ur
import os
from time import sleep


class GetUrl:
    def __init__(self, returndata=False):
        self.returndata = returndata

    def get_url(self, url, ret=False, tofile=None, bin=False):
        rdata = None
        head, tail = os.path.split(url)
        try:
            if tofile:
                if os.path.exists(tofile):
                    os.remove(tofile)
                if bin:
                    with open(tofile, 'wb') as f:
                        rdata = ur.urlopen(url).read()
                        f.write(rdata)
                else:
                    with open(tofile, 'w') as f:
                        rdata = ur.urlopen(url).read().decode('utf8')
                        f.write(rdata)
                sleep(.5)
            if ret:
                return rdata
        except:
            print("Unexpected error:", sys.exc_info()[0])

if __name__ == '__main__':
    url = 'ftp://ftp.nasdaqtrader.com/symboldirectory/phlxListedStrikesWithOptionIds.zip'
    tofile = 'G:\python\stock_market\symbols\data\DailyFiles\\USA\phlxListedStrikesWithOptionIds.zip'
    p = GetUrl()
    p.get_url(url, tofile, bin=True)

import os
from bs4 import BeautifulSoup
import HasInternet as HsInt
import GetUrl as GtUrl
import json
from collections import defaultdict


class CorporaData:
    def __init__(self, url='http://www.nltk.org/nltk_data/', datafname=None):
        self.corpora = defaultdict(lambda: defaultdict(list))
        self.keys = []
        self.fname = datafname
        self.corpus_url = url
        self.has_internet = HsInt.has_connection()
        self.geturl = GtUrl.GetUrl()
        self.data = self.getpage()
        self.make_soup()

    def getpage(self):
        corpdata = None
        if self.has_internet:
            corpdata = self.geturl.get_url(self.corpus_url, ret=True, tofile=self.fname)
        else:
            if os.path.isfile(self.fname):
                with open(self.fname, 'r') as f:
                    corpdata = f.read()
        return corpdata

    def make_soup(self):
        soup = BeautifulSoup(self.data, "html.parser")
        # print(soup.get_text()) # Nothing there but blank lines
        packages = soup.find_all('package')

        innertags = [
            'id', 'name', 'author', 'Languages', 'url', 'checksum', 'size', 'subdir', 'unzip',
            'unzipped_size', 'webpage', 'contact', 'license', 'copyright', 'copyright', 'note',
            'sample']

        for n, package in enumerate(packages):
            recid = 'RecId{}'.format(n)
            for item in innertags:
                value = package.get(item)
                self.corpora[recid][item] = value

        with open("corpora.json", "w") as f:
            j = json.dumps(self.corpora)
            f.write(j)

    def show_corpora(self):
        for rec in self.corpora:
            print('\nRecId: {}'.format(rec))
            for item in self.corpora[rec]:
                if self.corpora[rec][item] is None:
                    continue
                print('    {}: {}'.format(item, self.corpora[rec][item]))

if __name__ == '__main__':
    cc = CorporaData(datafname='CorpusSource.html')
    cc.show_corpora()

'''
The MIT License (MIT)

Copyright (c) 2018 Patrick Olsen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

Author: Patrick Olsen
'''

import sys
import csv
import argparse
from datetime import datetime
from Registry import Registry

class DomStorage(object):

    def __init__(self, hive):
        self.hive = hive
        self.regpath = 'Local Settings\Software\Microsoft\Windows\CurrentVersion\AppContainer\Storage\microsoft.microsoftedge_8wekyb3d8bbwe\Children'
    
    def getPath(self):
        try:
            open_hive = Registry.Registry(self.hive).open(self.regpath)
            return(open_hive)
        
        except Registry.RegistryKeyNotFoundException as e:
            print(e)

    def getChildren(self, children):
        for sks in children.subkeys():
            yield(sks.name())

    def getDoms(self, kids):
        for k in kids:
            domstorage = self.regpath + '\%s\Internet Explorer\DOMStorage' % (k)
            edp_domstorage = self.regpath + '\%s\Internet Explorer\EdpDomStorage' % (k)

            domstorage_subkeys = Registry.Registry(self.hive).open(domstorage).subkeys()
            edpdomstorage_subkeys = Registry.Registry(self.hive).open(edp_domstorage).subkeys()

            yield([domstorage_subkeys, edpdomstorage_subkeys])

    def getURLs(self, urls):
        for url in urls:
            for u in url:
                time = datetime.__str__(u.timestamp())
                url = u.name()
                yield([time, url])

    def getResults(self, results):
        writer = csv.writer(sys.stdout)
        writer.writerow(['timestamp','url'])
        for res in results:
            for r in res:
                writer.writerow([r[0], r[1]])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Microsoft Edge DomStorage parser')
    parser.add_argument('-usr', '--usrclass', required=True, 
        help='Path to UsrClass hive.')
    args = parser.parse_args()

    hive = args.usrclass
    
    children = DomStorage(hive).getPath()
    kids = DomStorage(hive).getChildren(children)

    resultsList = []

    for urls in DomStorage(hive).getDoms(kids):
        results = DomStorage(hive).getURLs(urls)
        resultsList.append(results)

    DomStorage(hive).getResults(resultsList)

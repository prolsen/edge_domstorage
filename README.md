# Microsoft Edge DOMStorage Parser

Print URLs from Microsoft Edge's DOMStorage and EdpDomStorage Entries. The location of the entries are below. The entries come from the UsrClass.dat registry hive.

    Local Settings\Software\Microsoft\Windows\CurrentVersion\AppContainer\Storage\microsoft.microsoftedge_8wekyb3d8bbwe\Children\###\Internet Explorer\DOMStorage

    Local Settings\Software\Microsoft\Windows\CurrentVersion\AppContainer\Storage\microsoft.microsoftedge_8wek yb3d8bbwe\Children\###\Internet Explorer\EdpDomStorage
    
There are multiple "children", hence the ###. The code will iterate through them and return the URLs.

# Help

python .\edge_domstorage.py -h

    usage: edge_domstorage.py [-h] -usr USRCLASS

    Microsoft Edge DomStorage parser
    
    optional arguments:
      -h, --help            show this help message and exit
      -usr USRCLASS, --usrclass USRCLASS
                            Path to UsrClass hive.
# Results

python .\edge_domstorage.py -usr UsrClass.dat

    timestamp,url
    <snip>
    2018-09-05 21:22:27.391993,account.godaddy.com
    2018-09-04 23:17:20.813562,account.microsoft.com
    2018-09-06 16:19:04.114895,account.t-mobile.com
    2018-09-09 01:18:14.652338,accounts.google.com
    2018-09-05 21:44:27.321726,authorize.kobo.com
    2018-09-07 00:35:26.722242,autozone.com
    2018-09-04 23:26:17.854053,betterment.com
    2018-09-09 15:10:27.987114,bing.com
    <snip>

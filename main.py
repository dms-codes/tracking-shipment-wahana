import requests
from bs4 import BeautifulSoup as bs

URL = 'https://www.wahana.com/lacak-kiriman?noresi='
NORESI = '187TNBLM'
NUMCHR = 100
CHAR = '='
r = requests.get(URL+NORESI)
html = r.content
soup = bs(html,'html.parser')
soup_data_tracking = soup.find_all('div', class_='font-size14 font-bold lh-16')
soup_nomor_telp = soup.find_all('div', class_ = 'font-size10 font-light')
status_terakhir = soup.find('div', class_='col-9 col-md-10')
nama_pengirim = soup_data_tracking[0].text.strip()
nama_penerima  = soup_data_tracking[1].text.strip()
asal = soup_data_tracking[2].text.strip()
tujuan = soup_data_tracking[3].text.strip()
print(CHAR*NUMCHR)
print('Tracking Wahana Resi#',NORESI)
print(CHAR*NUMCHR)
print('Pengirim:',nama_pengirim, asal)
print('Penerima:',nama_penerima, tujuan)
print(CHAR*NUMCHR)
print('Status Terakhir:',status_terakhir.text.strip().replace('\n',''))
print(CHAR*NUMCHR)
for i, track in enumerate(soup_data_tracking[-1:4:-1]):
    print(i+1,track.text.strip())
print(CHAR*NUMCHR)

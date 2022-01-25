import requests
from bs4 import BeautifulSoup
print("### BROKEN LINK CHECKER ###")
url = input("### Başında https olarak url adresini giriniz : ")
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
url_list=[]
def url_hunt():
  for link in soup.find_all('a'):
      #print(link.get('href'))
      url_list.append(link.get('href'))

#print(url_list)
def brokenLinkChecker():
  for url in url_list:
      try:
        response = requests.get(url)
        if response.status_code == 200:
            print(url + " Sorun Bulunamadı")
        elif response.status_code == 404:
            print(url +'Kırık Link Tespit Edildi')
      except IOError:
          print(url + ":   Bu bir link değil")
url_hunt()
brokenLinkChecker()
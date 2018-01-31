import requests
from bs4 import BeautifulSoup
import time

art = '''
---------------------------------------------------------------------
___________.__                 ___.   ________                       
\__    ___/|  |__  __ __  _____\_ |__ \______ \   ______  _  ______  
  |    |   |  |  \|  |  \/     \| __ \ |    |  \ /  _ \ \/ \/ /    \ 
  |    |   |   Y  \  |  /  Y Y  \ \_\ \|    `   (  <_> )     /   |  
  |____|   |___|  /____/|__|_|  /___  /_______  /\____/ \/\_/|___|  /
                \/            \/    \/        \/                  \/ 
--------------------------------------------By https://github.com/GmT5
'''
print(art)

class Downloader(object):

    def __init__(self, url, file_name):
        self.file_name = file_name
        self.page = requests.get(url)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
    
    def find_img(self):
        self.link = self.soup.find(itemprop="thumbnailUrl")
        self.imglink = self.link['href']

    def create_img(self):
        self.thumbnail = requests.get(self.imglink)
        self.arq = open('{}.jpg'.format(self.file_name), 'wb')
        self.arq.write(self.thumbnail.content)
        print("Baixado!!")

url = input('URL Do Vídeo: ')
file_name = input('Nome Da Imagem: ')

obj = Downloader(url, file_name)
obj.find_img()
obj.create_img()

time.sleep(2)



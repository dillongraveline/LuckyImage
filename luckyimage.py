import requests
import os
import fire
from bs4 import BeautifulSoup
import shutil

def search(s='cats'):

    download = os.path.expanduser('~')
    download = f'{download}/Downloads/'

    searchterm = s.replace('_','%20')

    image = requests.get(f'https://www.google.com/search?tbm=isch&q={searchterm}')
    content = image.text
    soup = BeautifulSoup(content, 'html.parser')

    imgs = soup.find_all('img')
    list = []
    for image in imgs:
        try:
            list.append(image['src'])
        except:
            pass
    url = list[2]
    image = requests.get(url, stream=True)
    with open(f'{download}/{s}.jpg', 'wb') as f:
        image.raw.decode_content=True
        shutil.copyfileobj(image.raw, f)


if __name__ == '__main__':
    fire.Fire(search)

import ssl
import os

import pandas as pd

from tqdm import tqdm
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup


rooturl = 'http://www.imdb.com'
path = os.path.dirname(os.path.abspath(__file__))


def Sourec_ReadCSV(sourcepath):
    movieIdL = []
    imdbIdL = []
    with open(sourcepath, 'r', newline='') as csvreader:
        filereader = pd.read_csv(csvreader,
                                 usecols=['movieId', 'imdbId'])
    for val in range(len(filereader['movieId'])):
        movieIdL.append(filereader['movieId'][val])
        imdbIdL.append(filereader['imdbId'][val])
    print("Open File Complete")
    return movieIdL, imdbIdL


def main():
    source = os.path.join(path, 'links.csv')
    movieIdL, imdbIdL = Sourec_ReadCSV(source)
    error = []
    for val in tqdm(range(0, len(movieIdL))):
        filename = '{}.jpg'.format(movieIdL[val])
        if not os.path.isfile(os.path.join(path, filename)):
            url = 'http://www.imdb.com/title/tt{}/'.format(imdbIdL[val])
            try:
                soup = BeautifulSoup(urlopen(url), 'html.parser')
                getURL = soup.findAll('div', {'class': 'poster'})
                IMDB = getURL[0].find_all('a', href=True)
                bigImageURL = "{0}{1}".format(rooturl, IMDB[0]['href'])
                soup = BeautifulSoup(urlopen(bigImageURL), 'html.parser')
                getURL = soup.findAll('meta', {'itemprop': 'image'})
                ssl._create_default_https_context = ssl._create_unverified_context
                urlretrieve(getURL[0]['content'], filename)
            except Exception as e:
                error.append(
                    "movieID:{} IMDB:{}".format(movieIdL[val], imdbIdL[val])
                    )
    for msg in error:
        print(msg)


if __name__ == '__main__':
    main()

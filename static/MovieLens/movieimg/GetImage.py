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
    source = os.path.join(path, 'links0.csv')
    movieIdL, imdbIdL = Sourec_ReadCSV(source)
    for val in tqdm(range(len(movieIdL))):
        url = 'http://www.imdb.com/title/tt{}/'.format(imdbIdL[val])
        soup = BeautifulSoup(urlopen(url), 'html.parser')
        getURL = soup.findAll('div', {'class': 'poster'})
        IMDB = getURL[0].find_all('a', href=True)
        bigImageURL = "{0}{1}".format(rooturl, IMDB[0]['href'])
        soup = BeautifulSoup(urlopen(bigImageURL), 'html.parser')
        getURL = soup.findAll('meta', {'itemprop': 'image'})
        ssl._create_default_https_context = ssl._create_unverified_context
        urlretrieve(getURL[0]['content'], '{}.jpg'.format(movieIdL[val]))

if __name__ == '__main__':
    main()

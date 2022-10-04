import bs4
import requests
import wget
import multiprocessing


def parser(i):
    status = 500
    while status != 200:
        number = i

        response = requests.get("https://www.memify.ru/meme/" + str(number))
        status = response.status_code
        if status != 200:
            break
        soup = bs4.BeautifulSoup(response.text, "lxml")
        soup = str(soup.figure.img)
        soup = soup[soup.find('https'):]
        wget.download(soup[:-3], '/Users/peeon/memes2/' + str(number) + '.jpg')


if __name__ == '__main__':
    print("Start")
    with multiprocessing.Pool(multiprocessing.cpu_count()*4) as p:
        p.map(parser, list(range(80000)))







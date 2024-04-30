import feedparser

def addUrl():
    return input('Please input the url to read from: ')

def parseUrl(url):
    print(feedparser.parse(url)['feed'])


def main():
    url = addUrl()
    parseUrl(url)


if __name__ == '__main__':
    main()

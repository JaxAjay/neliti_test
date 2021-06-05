# import codecs
import urllib.request
from bs4 import BeautifulSoup

def word_frequencies(url):
    """
    Downloads the content from the given URL and returns a dict {word -> frequency}
    giving the count of each word on the page. Ignores HTML tags in the response.
    :param url: Full URL of HTML page
    :return: dict {word -> frequency}
    """
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf-8")
    soup = BeautifulSoup(mystr)
    raw_text = soup.get_text()
    removals = ["\n","\r" , "\xa0"]
    for i in removals:
        raw_text = raw_text.replace(i , "")
    text_lis = raw_text.split(" ")
    dic = {}
    for i in text_lis:
        if dic.get(i):
            dic[i]+=1
        else:
            dic[i]=1
    return dic

if __name__ == "__main__":
    url = "https://api.flutter.dev/flutter/material/Chip-class.html"
    result = word_frequencies(url)
    print(result)


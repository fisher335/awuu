# Create your views here.
from django.shortcuts import render_to_response
import urllib2
import random
from bs4 import BeautifulSoup

def get_qiu(r_url):
    req = urllib2.Request(r_url, headers={'User-Agent': 'Mozilla/4.0'})
    res = urllib2.urlopen(req, timeout=60)
    soup = BeautifulSoup(res.read(), from_encoding='utf-8')
    contents= soup.find_all('div', {'class': 'article block untagged mb15'})
    content =random.choice(contents)
    bb =BeautifulSoup(str(content), from_encoding='utf-8')
    text = bb.find('div', {'class': 'content'})
    pic = bb.find('div', {'class': 'thumb'})
    if pic:
        return text.get_text().strip(), pic.a.img['src']
    else:
        return text.get_text().strip(), None


def hello(request):
    # values = request.META.items()
    # values.sort()
    page = random.randint(1, 150)
    r_url = 'http://www.qiushibaike.com/hot/page/' + str(page)
    content, pic = get_qiu(r_url)
    return render_to_response('base.html',{'content': content,'pic': pic})
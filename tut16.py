import random
import urllib.request

def downloadimg(url):
    name = random.randrange(1,1)
    var=str(name)+ ".jpg"
    urllib.request.urlretrieve(url,var)
    
downloadimg("https://www.gannett-cdn.com/presto/2018/08/14/PTAL/6e4fff76-595d-4069-9112-cfe15dbfaa43-IMG_Stadium.jpeg?width=660&height=319&fit=crop&format=pjpg&auto=webp")
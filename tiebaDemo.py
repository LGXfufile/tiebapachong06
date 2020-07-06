import urllib
import urllib.request
from urllib import parse
from lxml import etree

 #1、先讲整体架构；
 #2、构造url;
 #3、爬取页面内容；
#不管爬什么东西，都需要先构建url,然后爬取页面内容；
#获取a标签，然后通过帖子详情，爬取图片；

class Spider(object):
    def __init__(self):
        self.tiebaName = "Python"
        self.beginPage =1
        self.endPage =2
        self.url = "https://tieba.baidu.com/f?"
        self.header = {"ser-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWe\
        bKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        self.filename = 1
    #构造url
    def fanhaoSpider (self):
        for page in range(self.beginPage,self.endPage+1):
            pn = (page-1)*50
            wo = {'pn':pn,'kw':self.tiebaName}

            word = urllib.parse.urlencode(wo)
            myurl = self.url+word;
            self.loadPage(myurl)


    #爬取页面内容：
    def loadPage(self,url):
        req = urllib.request.Request(url,headers=self.header) #构造一个请求
        #爬取页面；
        data = urllib.request.urlopen(req).read()  # type: object

        html = etree.HTML(data)
        links = html.xpath('//div[@class = "threadlist_lz clearfix"]/div/a/@href')
        for link in links:
            link  = "https://tieba.baidu.com"+link
            self.loadImage(link)

    #获取页面详情，获得图片链接；
    def loadImage(self,link):
        req = urllib.request.Request(link,headers=self.header)
        data = urllib.request.urlopen(req).read()
        html = etree.HTML(data)
        links = html.xpath('//img[@class="BDE_Image"]/@src')

        for imageLink in links:
            self.writeImage(imageLink)

    #通过图片所在链接，保存图片到本地；
    def writeImage(self,imagesLink):
        print("第"+str(self.filename)+"张存储完成"+"...")

        image = urllib.request.urlopen(imagesLink).read()

        file = open(r"E:\PythonLearning\image\\"+str(self.filename)+".jpg","wb")

        file.write(image)

        file.close()
        self.filename+=1



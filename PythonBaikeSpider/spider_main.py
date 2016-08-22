# coding:utf8
'''
Created on 2016年8月21日
爬虫总调度程序
@author: Liubin
'''
from PythonBaikeSpider import url_manager, html_downloader, html_parser,\
    html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        #初始化程序需要用到URL管理器、HTML下载器、HTML解析器以及HTML输出文件
        
    
    
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        #向URL管理器中添加待爬取的URL
        #开始爬取循环
        while self.urls.has_new_url():
            try:
                #当URL管理器中有待爬取的URL时
                new_url = self.urls.get_new_url() #获取一个带爬取的URL
#                 print new_url
                print 'craw %d : %s' % (count,new_url)
                html_cont = self.downloader.download(new_url)
#                 print html_cont 
                #下载这个待爬取的URL页面,存在html_cont中
                new_urls, new_data = self.parser.parse(new_url, html_cont) 
#                 print new_urls
#                 print new_data
                #利用html解析器解析页面，并更新URL列表及存储数据
                self.urls.add_new_urls(new_urls) #将URL列表中的链接添加到URL管理器
                self.outputer.collect_data(new_data) #收集数据
                
                if count == 100:
                    break
                count = count + 1
            except:
                print 'craw failed'   
            #异常处理
            
        self.outputer.output_html() #输出爬取的数据
            

if __name__=="__main__":
    root_url = "http://baike.baidu.com/view/15158147.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

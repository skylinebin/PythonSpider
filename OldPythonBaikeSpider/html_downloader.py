# coding:utf8
'''
Created on 2016年8月21日
HTML下载器
只需要实现下载功能
最简单的方法
@author: Liubin
'''
import urllib2


class HtmlDownloader(object):
    
    
    def download(self, url):
        if url is None:
            return None
        
        response = urllib2.urlopen(url)
        
        if response.getcode() != 200:
            return None
        return response.read()
        
    
    
    




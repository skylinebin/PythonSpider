# -*- coding: utf-8 -*-
'''
Created on 2016年8月21日
html 输出部分

Updated 2020年5月19日

输出成html文件
@author: SkylineBin
'''


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
        
    
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
        #收集数据
        
    
    def output_html(self,):
        fout = open('output.html', 'w', encoding="utf-8")
        # 添加 encoding 描述可解决 windows 平台的乱码问题
        
        fout.write("<html>")
        fout.write("<body>")
        # fout.write("<table>")
        
        for data in self.datas:
            # print(data)
            # 输出到 HTML 中
            fout.write("<div>")
            fout.write(("<b> %s </b>" % data['title']).encode('utf-8').decode('utf-8'))
            fout.write("<div>url: %s </div> " % data['url'])
            fout.write(("<p> %s </p>" % data['summary']).encode('utf-8').decode('utf-8'))
            fout.write("</div>")
        
        # fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        
        #输出HTML文件
    
    
    
    




# BluePython
搜集自己些坑  常用的文档 书记  类库 开源项目

## Python  包库

[lfd.uci.edu](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pycurl)
- 常用的非常好的一个Python的库网站
- LFD,非官方版本、32和64位、Windows、二进制文件、科学开源、Python扩展包
克里斯托夫·戈尔克(by Christoph Gohlke)，LFD(荧光动力学实验室），加利福尼亚大学，Irvine,

[Mysql第三方库](http://ftp.ntu.edu.tw/MySQL/Downloads/Connector-Python/)

[PyMySQL](https://github.com/PyMySQL/PyMySQL)

## Pyspider 坑

> **Command "python setup.py egg_info" failed with error code 10 in C:\Users\Lenovo\AppData\Local\Temp\pip-build-kx1veoet\pycurl\**

[第一次安装Pyspider出现的错误](http://blog.csdn.net/qijingpei/article/details/68958040)
* 未安装pycurl（未解决，只是提供一种思路）安装pyspider失败：Command "python setup.py egg_info"failed with error code 10 in.....
* [python3.6安装pyspider出现的问题（pycurl安装失败）和解决方案](http://blog.csdn.net/sinat_33487968/article/details/69421147)
* [如何在Win7中安装Python的.whl扩展包](http://jingyan.baidu.com/article/19020a0a1f9774529d2842b7.html)E:\Python>pip install pycurl-7.43.0-cp36-cp36m-win32.whl

> **这个错误会发生在请求 https 开头的网址，SSL 验证错误，证书有误。
解决方法：使用 self.crawl(url, callback=self.index_page, validate_cert=False)
这个方法基本可以解决问题了。
**

[SSL certificate problem错误的解决方法](http://cuiqingcai.com/2703.html)

[SSL certificate problem: unable to get local issuer certificate错误](http://blog.csdn.net/tzs_1041218129/article/details/52853465)


[scrapy中文教程](http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html)

[pyspider文档](https://www.kancloud.cn/manbuheiniu/pyspider/101633)

[python使用mysql数据库](http://www.cnblogs.com/fnng/p/3565912.html)


[坑pyspidr重新启动项目出现丢失，可能的原因](http://www.cnblogs.com/zhaoxiangding/p/6774883.html)


[在没有webui情况下，如何使用pyspider调试爬虫？](https://segmentfault.com/q/1010000006471179)
*你可以在本地创建一个脚本文件 sample.py 然后使用 pyspider one -i sample.py 进行调试
*http://docs.pyspider.org/en/latest/Command-Line/#one

[https://imlonghao.com/](https://imlonghao.com/)

>**一般来说，一个任务失败了三次，就会显示failed。这个时候在数据表里面的status是3。
status这个字段具体含义如下：
1： 任务失败，需要重新执行的
2： 任务执行成功的
3： 任务失败，并且已经达到最大重试次数的。
所以，可以在爬虫脚本里面手动的从数据库里面把status=3的任务的Url提取出来再去爬取**

[pyspider的mysql数据存储接口](http://blog.csdn.net/u012293522/article/details/44222207)

``` python
#!/usr/bin/env python  
# -*- encoding: utf-8 -*-  
# Created on 2015-03-12  
''''' 
pyspider结果保存到数据库简单样例。 
使用方法： 
    1, 把本文件放到pyspider/pyspider/database/mysql/目录下命名为mysqldb.py; 
    2, 建立相应的表和库; 
    3, 在脚本文件里使用from pyspider.database.mysql.mysqldb import ToMysql引用本代码; 
    4, 重写on_result方法. 
'''  
from six import itervalues  
import MySQLdb  
  
class ToMysql():  
      
    def __init__(self,kwargs):  
        ''''' 
        kwargs = {  'host':'localhost', 
                    'user':'root', 
                    'passwd':'root', 
                    'db':'others', 
                    'charset':'utf8'} 
        '''  
        hosts    = kwargs['host']     
        username = kwargs['user']  
        password = kwargs['passwd']  
        database = kwargs['db']  
        charsets = kwargs['charset']  
          
        self.connection = False  
        try:  
            self.conn = MySQLdb.connect(host = hosts,user = username,passwd = password,db = database,charset = charsets)  
            self.cursor = self.conn.cursor()  
            self.cursor.execute("set names "+charsets)  
            self.connection = True  
        except Exception,e:  
            print "Cannot Connect To Mysql!/n",e  
              
    def escape(self,string):  
        return '%s' % string  
          
    def into(self,tablename=None,**values):  
          
        if self.connection:   
            tablename = self.escape(tablename)    
            if values:  
                _keys = ",".join(self.escape(k) for k in values)  
                _values = ",".join(['%s',]*len(values))  
                sql_query = "insert into %s (%s) values (%s)" % (tablename,_keys,_values)  
            else:  
                sql_query = "replace into %s default values" % tablename  
            try:  
                if values:  
                    self.cursor.execute(sql_query,list(itervalues(values)))  
                else:         
                    self.cursor.execute(sql_query)  
                self.conn.commit()  
                return True  
            except Exception,e:  
                print "An Error Occured: ",e  
                return False  
 
```


## Python 爬虫

[一个爬取易车网汽车数据的爬虫，使用 python scrapy框架。](https://github.com/zhangxu999/yiche)

[Python 编码转换与中文处理](http://www.jianshu.com/p/53bb448fe85b)

[Pyspider框架 —— Python爬虫实战之爬取 V2EX 网站帖子](https://segmentfault.com/a/1190000007360307)

> **response.etree.xpath()
response.encoding = 'utf-8'
response.etree.xpath('//div[@class="post-title"]//h3//a//@href'):
**

[pyspider_Xpath使用列子](https://github.com/binux/pyspider/issues/431)

[pyspider_Xpath使用列子](https://www.bountysource.com/issues/40855857-git-pyspider-version-stop-from-doing-any-activity-at-some-point-of-time)

[网络爬虫项目](https://github.com/FullerHua/gooseeker)
* 采集安居客房产经纪人
* 采集天猫商品信息
* 采集豆瓣小组讨论话题

[python脚本爬取今日头条视频数据](https://github.com/fourbrother/python_toutiaovideo)

[互联网金融爬虫怎么写－第一课 p2p网贷爬虫（XPath入门）](http://youmumzyx.iteye.com/blog/2299724)

[Python爬虫进阶四之PySpider的用法](http://cuiqingcai.com/2652.html)

[Python爬虫实战四之抓取淘宝MM照片](http://cuiqingcai.com/1001.html)



[Python豆瓣图书爬虫:30000本书](http://www.lenggirl.com/mywork/doubanbook30000.html)
* http://www.cnblogs.com/nima/category/726571.html

 
 
[漫谈Pyspider网络爬虫的实践](https://www.figotan.org/2016/08/10/pyspider-as-a-web-crawler-system/?utm_source=tuicool&utm_medium=referral)

1. ~~Scrapy~~
2. [a smart stream-like crawler & etl python library](https://github.com/ferventdesert/etlpy)
3. [爬视频音频神器You-Get](https://you-get.org/)
4. [另一款视频下载神器youtube-dl](https://github.com/rg3/youtube-dl)
5. [youtube-dl图形界面版](https://github.com/MrS0m30n3/youtube-dl-gui)
6. [自动抓取Tumblr指定用户视频分享](https://github.com/Thoxvi/MyCar_python)
7. [crawley](https://github.com/jmg/crawley)
8. [乌云公开漏洞、知识库爬虫和搜索](https://github.com/hanc00l/wooyun_public)
9. [下载指定的 Tumblr 博客中的图片，视频](https://github.com/dixudx/tumblr-crawler)
10. [下载指定的 Tumblr 博客中的图片，视频，玄魂修改版](https://github.com/xuanhun/tumblr-crawler)
11. [DHT网络爬虫](https://github.com/78/ssbc)
12. [豆瓣电影、书籍、小组、相册、东西等爬虫集 writen in Python](https://github.com/dontcontactme/doubanspiders)
13. [如何不用客户端下载 YouKu 视频-YouKu 实现下载 Python3 实现](http://zpz.name/2378/)
14. [一个可配置的、分布式的爬虫框架](https://github.com/yijingping/unicrawler)
15. [cloud-based web crawling platform](https://github.com/scrapinghub)
16. [百度云爬虫-爬取百度云/百度网盘所有的分享文件](https://github.com/x-spiders/baiduyun-spider)
17. [爱丝APP图片爬虫，以及免支付破解VIP看图](https://github.com/x-spiders/aiss-spider)
18. [微信公众号爬虫](https://github.com/bowenpay/wechat-spider)
19. [拉勾网爬虫](https://github.com/whatsGhost/lagou_spider)
20. [百度网盘爬虫（如何爬取百度网盘）](https://www.v2ex.com/t/348731#reply7)
21. [scrapy爬虫图形管理界面 ](https://github.com/DormyMo/SpiderKeeper)
 
 

[磁力种子搜索](http://cli.info/)

[一步一步教你写BT种子嗅探器--原理篇](http://www.jianshu.com/p/5c8e1ef0e0c3)

## TODO 待采集的网站

[妹子图](http://www.meizitu.com/)

[清纯美女](http://www.yjz9.com/tu/qcmn/)

[医院列表](http://www.cnkang.com/yyk/hospital/)

[10条](http://www.10tiao.com/channel/index?type=268&name=python)





## 教程

[Python教程](http://www.yiibai.com/python/)

[Python3教程](http://www.runoob.com/python3/python3-tutorial.html)


[http://www.person168.com/](http://www.person168.com/)

[Python初学者（零基础学习Python、Python入门）书籍、视频、资料、社区推荐](https://github.com/Yixiaohan/codeparkshare)

[Python.ctolib.com](http://www.ctolib.com/python/)

http://blog.sina.com.cn/s/blog_6261fa490102xmir.html

http://www.miaopai.com/u/paike_pxvqtedp1q

http://weibo.com/p/100808354800c4c6b531b950dc159170e9c477?k=电商数据分析免费教学&from=501&_from_=huati_topic


https://github.com/zhisheng17/Python-Projects


http://www.cnblogs.com/panliu/p/4524157.html


https://github.com/Germey/TaobaoMM/blob/master/spider/spider.py

[邮差网](http://mailchina.org/secondClassIndex?firstClassId=1&secondClassId=4)
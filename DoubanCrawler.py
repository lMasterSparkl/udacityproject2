import requests
import expanddouban
import csv
from bs4 import BeautifulSoup
class mv:#定义电影类并对文件间隔进行调整

    def getMovieUrl(category, location):#定义组合网址url函数输入类型 地区返回对应url
        
        url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,{},{}".format(category,location)
        return url
    
    def getmoviehtml(url):
        #定义下载网页并返回html函数 调用了已给出的文件
        #参考网站：https://www.cnblogs.com/111testing/p/6123833.html  http://selenium-python-zh.readthedocs.io/en/latest/getting-started.html

        html = expanddouban.getHtml(url,True,1) #第二个参数为true则通过循环自动点击加载更多选项，第三个参数设置间隔时间默认为2s
        return html
    
    def getMovies(category,location):
        #定义返回电影信息列表的函数 参考网站：https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/

        html_=mv.getmoviehtml(mv.getMovieUrl(category,location))

        soup = BeautifulSoup(html_,"html.parser")

        movie_div=soup.find(class_='list-wp')

        for mation in movie_div.find_all('a'):
            m.append([mation.find(class_='title').get_text(),mation.find(class_='rate').get_text(),category,location,mation.get('href'),mation.find('img').get('src')])
            lastlocation[n]+=1
        return m
    
m=[] #存储某电影六项基本信息的列表 ：电影名称name电影评分rate电影类型category电影地区location电影页面链接info_link电影海报图片链接cover_link

locationsum=['大陆','美国','香港','台湾','日本','韩国','英国','法国','德国','意大利','西班牙','印度','泰国','俄罗斯','伊朗','加拿大','澳大利亚','爱尔兰','瑞典','巴西','丹麦']#地区总列表如有变动直接修改列表即可

lastlocation=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#用来统计某一地区电影数目的列表注意其元素顺序对应地区列表locationsum

baselocation=[]

mvtype=['剧情','悬疑','科幻']#我自己选择的三个电影类型

for i in range(len(mvtype)):#通过嵌套的for循环进行列表数据筛选数据处理以及文件写入操作

    for n in range(len(locationsum)):

        mv.getMovies(mvtype[i],locationsum[n])#通过记录某一种类所有地区的电影信息来进行统计与记录

    baselocation=sorted(lastlocation,reverse=True) #将统计好的列表进行排序 要注意使用sorted方法而不是sort后者会改变原列表而我在这里需要保留原始列表lastlocation的元素顺序方便之后进行地区的选择与输出

    for j in range(3):
        with open('output.txt','a',encoding='utf_8_sig') as output:#将某一种类电影数据处理并记录在output.txt文件中 使用了format函数进行格式化以减少代码行数 用utf-8编码可以避免输出乱码的情况 参考网站：http://www.runoob.com/python/att-string-format.html

            output.write('排名第{0}的地区为{1}，占{2}类别电影总数的{3:.2%}。\n'.format(j+1,locationsum[lastlocation.index(baselocation[j])],mvtype[i],lastlocation[lastlocation.index(baselocation[j])]/sum(lastlocation)))

    with open('movies.csv','a',newline='',encoding='utf_8_sig') as writemv:#用utf-8编码可以避免输出乱码的情况

        csv_write=csv.writer(writemv,dialect='excel')

        csv_write.writerows(m)
        #将m列表中的个人信息写入到movies.csv文件中
    m=[]
    lastlocation=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #将列表m和列表lastlocation进行清零进行下一种类电影的筛选
print('ok')#作为结束语句以及提醒

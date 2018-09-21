from pyquery import PyQuery as pq # 导入解析库
import pymysql # 用于连接并操作MySQL数据库
from multiprocessing import Pool, current_process
import requests
import re
def get_html(url):
    r = requests.get(url)
    return r
def pare_html(content):
    
    my_way = re.compile('class="title".*?>(.*?)</span>.*?"v:average">(.*?)</span>.*?"10.0">.*?<span>(.*?)</span>.*?"inq">(.*?)</span>',re.S)
    titles = re.findall(my_way, content.text)
    
    for titles in titles:
        mydict = {}
        mydict['title']=titles[0]
        mydict['rating'] = titles[1]
        mydict['pn'] = titles[2]
        mydict['rm'] = titles[3]
        
        yield mydict



    
def main():
    for i in range(10):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(i * 25)
        content = get_html(url)
        mydict = pare_html(content) 
        
        
        for num in mydict:
            print(num)
if __name__ == '__main__':
    pool = Pool(1)
    for i in range(10):
        pool.apply_async(main, (i, ))
    pool.close()
    pool.join()
    print('finish')
    
    main()
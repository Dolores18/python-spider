import requests
import re
content = requests.get('https://movie.douban.com/chart').text
# 豆瓣电影排行榜
pattern = re.compile('class="pl2".*?<.*?="(.*?)".*?>(.*?)<span.*?>(.*?)</span>.*?"rating_nums">(.*?)</span>.*?"pl">(.*?)</span>', re.S)
# compile可以在多次使用中提高效率，这里影响不大
results = re.findall(pattern, content)
for result in results:
	url, name1, name2, nums, pl = result

	print(url, name1.replace("/","").strip(), name2.replace("/","").strip(), nums, pl)
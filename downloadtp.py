import urllib.request
import os
import re

def url_open(url):
	req=urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
	response=urllib.request.urlopen(req)
	html=response.read()
	return html

def downloadtp(html):
	p=r'<img class="BDE_Image".*?src="(.*?\.jpg)".*?>'
	tplist=re.findall(p,html)
	try:
		os.mkdir('beautyimg')
	except FileExistsError:
		pass
	os.chdir('beautyimg')
	for each in tplist:
		filename=each.split('/')[-1]
		with open(filename,'wb') as f: #############################这里涨姿势了，存储图片网页如果事先decode解码了也可以，用如下语句一句就可以搞定######################
			img=url_open(each)         ########################urllib.request.urlretrieve(each,filename,None)#######其函数原型为urllib.request.urlretrieve(url, filename=None, reporthook=None, data=None)
			f.write(img)


if __name__=='__main__':
	url='https://tieba.baidu.com/p/3823765471'
	html=url_open(url).decode('utf-8')
	downloadtp(html)
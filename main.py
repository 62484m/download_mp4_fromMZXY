# coding:utf8
import requests


def create_url_list(baseurl, num):
	urllist = []
	for i in range(1, num + 1):
		url = baseurl[:-4] + str(i) + '.mp4'
		urllist.append(url)
	return urllist


def get_mp4(urllist):
	num = 1
	for url in urllist:
		r = requests.get(url)
		file_name = str(num) + ".mp4"
		with open(file_name, "wb") as code:
			code.write(r.content)
			print '%d is done' % num
		num += 1


if __name__ == '__main__':
	# baseurl = 'http://newoss.maiziedu.com/qiniu/hcyh.mp4'
	urllist = create_url_list(baseurl, 10)
	get_mp4(urllist)
	print 'all done'

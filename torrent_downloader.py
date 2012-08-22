# -*- coding: utf-8 -*-
import win32utf8
import codecs
import http.cookiejar, urllib.request
import re, os


cj = http.cookiejar.MozillaCookieJar()
cj.load("./tmp_files/cookie.txt")
for ind, cookie in enumerate(cj):
    print("%d - %s" %(ind, cookie))
print("CJ END")



opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
main_page = opener.open("http://share.dmhy.org/").read()
open("./tmp_files/webtmp.txt", "wb").write(main_page)
os.system("node node_html_tag.js")
filter_data = codecs.open("filter.txt", "r", "utf8").readlines()
filter_list = []
for i in filter_data:
	#print(i)
	tmp = i.split(" ")
	#print(tmp)
	filter_list.append(tmp)

main_page = codecs.open("./tmp_files/parsed_web.txt", "r", "utf8").readlines()
torrent_list = []
while len(main_page):
	i = main_page.pop(0)
	j = main_page.pop(0)
	torrent_list.append((i,j))
#print(torrent_list)
download_list = []
for title,torrent in torrent_list:
	#print(title, torrent)
	for rule in filter_list:
		#print("testing rule:", rule)
		flag = True
		for i in rule: 
			#print("asdf", title, i)
			m = re.search(i, title)
			if not m:
				#print("match", title, i)
				flag = False
				break
		if flag:
			#print(title, "passed", rule)
			download_list.append((title, torrent, rule))
for title,torrent,rule in download_list:
	print(title, torrent, rule) 
	name = "./torrents/" + re.search("hash_id\/([A-Za-z0-9]+)", torrent).group(1) + ".torrent"
	if os.path.exists(name):
		print("File already exists!")
	else:
		torrent_data = opener.open("http://share.dmhy.org" + torrent).read()
		open(name, "wb").write(torrent_data)
		print("Downloaded 1 torrent file.")





#torrent = opener.open("http://share.dmhy.org/topics/down/date/1344799839/hash_id/6b9c8696cff2b60f94f0cf635619bacc5da77960").read()
#open("PG.torrent", 'wb').write(torrent)
exit()
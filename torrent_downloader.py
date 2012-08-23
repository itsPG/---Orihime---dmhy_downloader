# -*- coding: utf-8 -*-
import win32utf8
import codecs
import http.cookiejar, urllib.request
import re, os, sys


print(len(sys.argv))

cj = http.cookiejar.MozillaCookieJar()
cj.load("./tmp_files/cookie.txt")
for ind, cookie in enumerate(cj):
    print("%d - %s" %(ind, cookie))
print("CJ END")



opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

if len(sys.argv) > 1:
	print("Reading " + sys.argv[1])
	main_page = opener.open(sys.argv[1]).read()
else:
	main_page = opener.open("http://share.dmhy.org/").read()

open("./tmp_files/webtmp.txt", "wb").write(main_page)
os.system("node node_html_tag.js")

filter_data = codecs.open("filter.txt", "r", "utf8").readlines()
filter_list = []
for i in filter_data:
	#print(i)
	tmp = i.strip().split(" ")
	#print(tmp)
	filter_list.append(tmp)
#print(filter_list)

main_page = codecs.open("./tmp_files/parsed_web.txt", "r", "utf8").readlines()
torrent_list = []
while len(main_page):
	i = main_page.pop(0)
	j = main_page.pop(0)
	torrent_list.append((i,j))
#print(torrent_list)

download_list = []
skip_count = 0
ignore_count = 0

for title,torrent in torrent_list:
	#print(title, torrent)
	add_flag = False
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
			add_flag = True
			break
	if not add_flag:
		ignore_count += 1

for title,torrent,rule in download_list:
	#print(title, torrent, rule) 
	print(title, rule)
	name = "./torrents/" + re.search("hash_id\/([A-Za-z0-9]+)", torrent).group(1) + ".torrent"
	if os.path.exists(name):
		print("File already exists!")
		skip_count += 1
	else:
		torrent_data = opener.open("http://share.dmhy.org" + torrent).read()
		open(name, "wb").write(torrent_data)
		print("Downloaded 1 torrent file.")

print("Skip " + str(skip_count) + " file(s).")
print("Ignore " + str(ignore_count) + " file(s).")




#torrent = opener.open("http://share.dmhy.org/topics/down/date/1344799839/hash_id/6b9c8696cff2b60f94f0cf635619bacc5da77960").read()
#open("PG.torrent", 'wb').write(torrent)
exit()
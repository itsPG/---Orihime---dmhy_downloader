import time, os, random
while True:
	os.system("python torrent_downloader.py http://share.dmhy.org/topics/list/sort_id/2")
	r = random.randint(900,1800);
	print("Sleep for " + str(r) + " seconds....................")
	time.sleep(r)

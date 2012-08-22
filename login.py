import win32utf8
import http.cookiejar, urllib.request
import re, os, getpass

username = "smartPG@gmail.com"
password = ""
captcha = ""


password = getpass.getpass("Enter the password of " + username + " : ")

cj = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
first_page = opener.open("http://share.dmhy.org/user/login").read().decode("utf-8")
#print(first_page);

m = re.search("common\/generate\-captcha\?code=([0-9]+)", first_page)
print(m.group(1));

captcha_pic = opener.open("http://share.dmhy.org/common/generate-captcha?code=" + m.group(1)).read()
open("PG.jpg", 'wb').write(captcha_pic)
os.system("mspaint PG.jpg");
captcha_code = getpass.getpass("Captcha (won't shown on screen) : ");

#ConsoleFile.wrap_standard_handles()

login_data = urllib.parse.urlencode    \
({                               \
	'email' : username,       \
	'password' : password,      \
	'login_node' : '0',        \
	'cookietime' : '315360000',         \
	'captcha_code' : captcha_code
}).encode("utf-8")
url = urllib.request.Request("http://share.dmhy.org/user/login", login_data)
url.add_header("User-Agent","Chrome/18.1.2.3")

ResponseData = opener.open(url).read().decode("utf8", 'ignore')

print(ResponseData)
for ind, cookie in enumerate(cj):
	print("%d - %s" %(ind, cookie))
cj.save("cookie.txt")

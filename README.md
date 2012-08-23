# dmhy 種子自動下載工具 (dmhy torrent auto downloader)

> ## Written by PG, released under MIT license

> ## this project is a part of project Orihime(TM)

## 系統需求 

* OS: Windows 7 or Mac 10.7 Lion
* node.js
* python 3.2
* pywin (for windows)

## 提醒

本程式建議搭配utorrent的自動載入種子功能，無論是.torrent或者是.torrent.loaded，我都有加入判斷自動略過已有種子的部份，可以降低伺服器的負擔

本程式學術研究成份居多，dmhy短時間內下載大量種子帳號會被ban，請謹慎使用

## 使用方法

如果cookie資訊仍然有效的話，可以跳過步驟1~3

### Step 1. 編輯login.py，把email換成您的email

### Step 2. 執行login.py，打入密碼，此時會顯示驗證碼

### Step 3. 關掉驗證碼視窗，打入驗證碼，如果出現登入cookie資訊就是登入成功

### Step 4. 編輯filter.txt檔案，程式會依照檔案記載的項目觸發下載

### Step 5. 執行`torrent_downloader.py 網址`，即可讀取指定網頁頁面並下載種子


## 技術文件

本程式包含以下技巧，可以當作撰寫程式時的參考

* 基本的python操作
* 解決windows上，python無法顯示utf8 (請參考win32utf8.py)
* 使用peg.js解析最低限度的html語法
* 使用python 操作cookies完成網頁登入
* 儲存並讀取cookies，達成網頁的session








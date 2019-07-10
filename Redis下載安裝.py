# 緩存
# 下載
    # https://github.com/microsoftarchive/redis/releases
    #   Redis-x64-3.0.504.msi


# redis默認端口 6379             mysql默認端口 3306
# r=redis.Redis(host="192.168.43.100",port=6379,db=0,password="gogo610610")

#下載完之後，直接安裝，然後打開安裝的資料夾

# redis-server.exe  這是伺服器端

# redis-cli.exe  這是客戶端

# ************************************
# python 這邊要安裝
# 方法一
# pip3 install redis

# 方法二
    # settings >  project:redis > project interpreter > 按最右邊 的加號 新增  ，然後搜尋  redis 下載安裝


# cmd > ipconfig > 找負責連網際網路的網卡 然後看 ipv4  例如 192.168.43.100

# ping 192.168.43.100  測試IP是否有通

# telnet 192.168.43.100 6379   測試端口是否有通，如果有通，會連到一個黑色畫面

#如果再CMD下 使用 telnet 顯示   'telnet' 不是內部或外部命令、可執行的程式或批次檔。
    # 就在控制台->程式和功能->開啟或關閉Windows功能
    # 找到Telnet 用戶端 打勾後按確定即可使用.

    # linux 遇到防火牆處理方式  82-08  84:00

    # netstat -lntpu  檢查redis對外連接端口是否有打開   linux
    # netstat -an  檢查redis對外連接端口是否有打開   winodws

    # 用netstat看時，6379那邊必須都要是0.0.0.0  這樣才是對外開放

    # 去安裝目錄下 C:\Program Files\Redis  找 redis.windows.conf  和  redis.windows-service.conf  這兩個都要改
    #     然後 在redis.windows.conf 中找到bind 127.0.0.1這行並修改為bind 192.168.43.100。

    #最後先停止redis  然後  重啟 redis   再去測試連線看看


#-------------修改密碼
# 去安裝目錄下 C:\Program Files\Redis  找 redis.windows.conf  和  redis.windows-service.conf  這兩個都要改
#     找到  # requirepass foobared   然後去掉#   foobared→修改為新密碼，例如 requirepass gogo610610
#                                                                 這樣密碼就會是 gogo610610
# 最後先停止redis  然後  重啟 redis   再去測試連線看看

#-----------------------------
# redis 與 python 字典的最大差別
# python 字典 只能存在自己的程式裡面運作，無法去和別的程式做交互

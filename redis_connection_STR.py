#連接  +  str 練習    82-04


import redis

r=redis.Redis(host="192.168.43.100",port=6379,db=0,password="gogo610610")

#創造一個redis 對象，透過這個對象，去控制對資料庫的增刪改查
# r=redis.Redis()   #如果都沒有寫，預設是本地連接

# r.set("peter","999")   #設置方法 set(name, value, ex=None, px=None,    nx=False, xx=False)
                                #    鍵     值   超時(秒)  超時(豪秒)  nx，如果設置為True，則只有name不存在時，會創建，存在則不動做
                                                                    #  xx，如果設置為True，則只有name存在時，會修改，不存在則不動做
print(r.get("peter"))  #取得指定 key 的值
#
# r.set("age","666")
#

#
# r.set("peter","777",xx=True)   #   xx，如果設置為True，則只有name存在時，會修改，不存在則不動做
# print(r.get("peter"))

# r.mset({"p1":222,"p2":888,"qoo":"chhhhh"})    #批量設置，裡面要用字典方式

# print(r.mget("p1","p2"))     # 批量獲取 直接放KEY方式
# print(r.mget(["p1","p2"]))   # 批量獲取 傳列表也可以


# r2=r.getset("p3",8345678908)  # 設置新值並獲取原來的值，所以有返回值
# print(r.get("p3"))
# print(r2)


# print(r.getrange("p3",3,5))  #"p3",8345678908    獲取一個範圍，例如第三到第五個範圍內的內容，
#                             #      0123456789    #所以答案是  b'567'

# r.setrange("p3",5,"====")  #         (要替換的key,key內容的第幾個位置,替換內容)     從第幾個位置，開始替換內容


# r.set("w1","r")
# print(ord("r"))  #轉換為 ASCII = 114
# print(bin(ord("r")))  #轉成 二進制  = 0b1110010
#                       #         位置  012345678
#
# # r.setbit("w1","5",1)   #(name,第幾個位置, value只能是0或1)     # 對name對應值的二進位表示的位元進行操作
#                        # 就是會先把內容，轉換成二進制 如果是 文字(中文佔三位元)，就轉換為 ASCII 然後 在轉成 二進制
#
# print(r.getbit("w1",3))

# r.set("zero","\x00")   # ASCII 的 0    odr(\x00)
# print(r.bitcount("zero"))   # bitcount 計算對應的值的二進位表示中 1 的個數
#
# print(r.strlen("p3"))  #取得字符串的長度
#
# r.incr("nono",1)   #自增方式，參數二必須是整數
# print(r.get("nono"))
#
#
# r.incrbyfloat("nono2",1.5)   #自增方式，參數二可以是浮點數
# print(r.get("nono2"))
#
# r.append("nono2","cccc")  #在後面增加文字  就是字符串拼接
# print(r.get("nono2"))

# print(r.keys())     #  使用  .keys()  取得所有的    key


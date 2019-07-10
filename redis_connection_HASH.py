# hash 哈希 練習    82-06

import redis

r=redis.Redis()   #創造一個redis 對象，透過這個對象，去控制對資料庫的增刪改查

r.hset("info","roro",1)             #一個一個設定
r.hset("info","gogo",3444)
r.hset("info","momo",666)

print(r.hget("info","roro"))  #獲取此name下的key的 value
print(r.hmget("info","roro","momo"))   #批量獲取 此name下的key
print(r.hkeys("info"))   #取得所有此name下的所有key

r.hmset("info",{"o1":55,"o2":2222,"o3":44444})    #批量設定  參數二的 鍵值裡面要是字典
# print(r.hkeys("info"))
#
# print(r.hgetall("info"))  #取得  此name下的key 和 value
#
# print(r.hlen("info"))  #取得 此name下的長度
#
# print(r.hvals("info"))    #取得所有此name下的所有 value
#
# print(r.hexists("info","i2"))  #檢查是否有這個 key
# print(r.hexists("info","o1"))  #檢查是否有這個 key



# r.hdel("info","o1")   #刪除指定key
# print(r.hkeys("info"))   #取得所有此name下的所有key


# r.hincrby("info","8855",1)   #自增   參數三必須是整數
# r.hincrbyfloat("info","333",1.3)   #自增   參數三可以是浮點數
# print(r.hgetall("info"))  #取得  此name下的key 和 value


print(r.hscan("info",0,"3*"))   #模糊匹配   參數三是要模糊匹配用的條件
print(r.hgetall("info"))  #取得  此name下的key 和 value



# print(help(r.hset))
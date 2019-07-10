# set 列表 練習    82-07 18:22
# 集合  是 無序的

import redis

r=redis.Redis()   #創造一個redis 對象，透過這個對象，去控制對資料庫的增刪改查


r.sadd("set_names","roro1","roro2","roro3","roro4","roro5")  #第一個值是key，後面全部都是內容
r.sadd("set_names2","roro11","roro2","roro33","roro4","roro5","roro6")  #第一個值是key，後面全部都是內容


print(r.scard("set_names"))     #獲取 個數

print(r.sdiff("set_names","set_names2"))   #第一個集合有的，但是第二集合沒有的內容   差集

print(r.sdiffstore("set_n3","set_names","set_names2"))    #回傳值是符合條件的個數
# 第一個集合有的 set_names ，但是第二集合沒有的內容 set_names2          放在在一個另外一個集合內  set_n3

print(r.smembers("set_n3"))  # 獲取name對應的集合的所有成員


print(r.sinter("set_names","set_names2"))   #第一個集合有的，第二集合也有的內容   交集

print(r.sinterstore("set_n4","set_names","set_names2"))   #回傳值是符合條件的個數
# 第一個集合有的 set_names ，第二集合也有的內容 set_names2          放在在一個另外一個集合內  set_n4

print(r.smembers("set_n4"))  # 獲取name對應的集合的所有成員


print(r.sismember("set_n4","roro2"))   # 檢查value是否是name對應的集合的成員   {b'roro5', b'roro2', b'roro4'}  True
print(r.sismember("set_n4","roro1"))   # 檢查value是否是name對應的集合的成員   {b'roro5', b'roro2', b'roro4'}  False


print(r.smove("set_n4","set_names","roro4"))  # 把參數一的集合成員 移到 參數二的集合裡面 ，參數三是要移動的值
print(r.smembers("set_n4"))  # 獲取name對應的集合的所有成員
print(r.smembers("set_names"))  # 獲取name對應的集合的所有成員



print(r.spop("set_names"))   ## 集合隨機移除一個成員，並將其返回
print(r.smembers("set_names"))  # 獲取name對應的集合的所有成員


print(r.srandmember("set_names",2))  #隨機獲取  N 個成員，參數二就是要獲取幾個成員

#-------------------以上 是 無序集合
print("---------有序 無序 切割線------")
#-------------------以下是 有序集合


# print(help(r.zadd))

print(r.zadd("sort_n1",{"k1":2,"k2":44,"k3":11,"k4":23,"k5":66}))    # 設置方式，第一個參數是key ，後面是有值，要用字典格式
print(r.zadd("sort_n2",{"k12":2,"k2":44,"k32":11,"k4":23,"k52":66}))    # 設置方式，第一個參數是key ，後面是有值，要用字典格式

print(r.zcard("sort_n1"))   #獲取該有序集合的個數

print(r.zrange("sort_n1",0,-1,withscores=True))    #  zrange  查看內容方式，這時是已經有序  從小到大
                            # withscores=True  也一起查看該元數的值  預設為false

print(r.zrank("sort_n1","k2"))  #獲取該值在裡面的排名，從小到大，從0開始    越小排名越前面


# zremrangebyrank(name, min, max)        #   # 根據排行範圍刪除
r.zremrangebyrank("sort_n1",1,2)
print(r.zrange("sort_n1",0,-1))    #  zrange  查看內容方式，這時是已經有序  從小到大


# zremrangebyscore(name, min, max)       #   # 根據分數範圍刪除
r.zremrangebyscore("sort_n1",40,50)
print(r.zrange("sort_n1",0,-1))    #  zrange  查看內容方式，這時是已經有序  從小到大


#同一組測試---↓
print(r.zadd("sort_n1",{"k1":2,"k2":44,"k3":11,"k4":23,"k5":66}))    # 設置方式，第一個參數是key ，後面是有值，要用字典格式
print(r.zadd("sort_n2",{"k12":2,"k2":41,"k32":11,"k4":23,"k52":66}))    # 設置方式，第一個參數是key ，後面是有值，要用字典格式

r.zinterstore("sort_n3",("sort_n1","sort_n2"),aggregate="MIN")  # 獲取兩個有序集合的交集，如果遇到相同值不同分數，則按照aggregate進行操作
                                                                # # aggregate的值為:  SUM  MIN  MAX

print(r.zrange("sort_n3",0,-1,withscores=True))    #  zrange  查看內容方式，這時是已經有序  從小到大
#同一組測試---↑


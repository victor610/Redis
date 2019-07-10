# Set操作，Set集合就是不允許重複的列表

# sadd(name,values)
# 	# name對應的集合中添加元素

# scard(name)
# 	獲取name對應的集合中元素個數

# sdiff(keys, *args)
# 	在第一個name對應的集合中且不在其他name對應的集合的元素集合

# sdiffstore(dest, keys, *args)
# 	# 獲取第一個name對應的集合中且不在其他name對應的集合，再將其新加入到dest對應的集合中

# sinter(keys, *args)
# 	# 獲取多一個name對應集合的交集

# sinterstore(dest, keys, *args)
# 	# 獲取多一個name對應集合的並集，再講其加入到dest對應的集合中

# sismember(name, value)
# 	# 檢查value是否是name對應的集合的成員

# smembers(name)
# 	# 獲取name對應的集合的所有成員

# smove(src, dst, value)
# 	# 將某個成員從一個集合中移動到另外一個集合

# spop(name)
# 	# 集合隨機移除一個成員，並將其返回

# srandmember(name, numbers)
# 	# 從name對應的集合中隨機獲取 numbers 個元素

# srem(name, values)
# 	# 在name對應的集合中刪除某些值

# sunion(keys, *args)
# 	# 獲取多一個name對應的集合的並集

# sunionstore(dest,keys, *args)
# 	# 獲取多一個name對應的集合的並集，並將結果保存到dest對應的集合中

# sscan(name, cursor=0, match=None, count=None)

# sscan_iter(name, match=None, count=None)
# 	# 同字串的操作，用於增量反覆運算分批獲取元素，避免記憶體消耗太大



#-------------------------------------------------------   有序集合   ---------------------------------------------------

# 有序集合，在集合的基礎上，為每元素排序；元素的排序需要根據另外一個值來進行比較，
# 所以，對於有序集合，每一個元素有兩個值，即：值和分數，分數專門用來做排序。

# zadd(name, *args, **kwargs)
#     # 在name對應的有序集合中添加元素
# print(r.zadd("sort_n1",{"k1":2,"k2":44,"k3":11}))    #第一個參數是key ，後面是有值，要用字典格式

                            #    這種方式有問題↓
                            #     # 如：
                            #     # zadd('zz', 'n1', 1, 'n2', 2)
                            #     # 或
                            #     # zadd('zz', n1=11, n2=22)
                            
                            
# zcard(name)
#   # 獲取name對應的有序集合元素的數量

# zcount(name, min, max)
#   # 獲取name對應的有序集合中分數 在 [min,max] 之間的個數

# zincrby(name, value, amount)
#   # 自增name對應的有序集合的 name 對應的分數

# r.zrange(name, start, end, desc=False, withscores=False, score_cast_func=float)
#   # 按照索引範圍獲取name對應的有序集合的元素
#
    # # 參數：
    # # name，redis的name
    # # start，有序集合索引起始位置（非分數）
    # # end，有序集合索引結束位置（非分數）
    # # desc，排序規則，預設按照分數從小到大排序
    # # withscores，是否獲取元素的分數，預設只獲取元素的值
    # # score_cast_func，對分數進行資料轉換的函數
    #
    # # 更多：
    # # 從大到小排序
    # # zrevrange(name, start, end, withscores=False, score_cast_func=float)
    #
    # # 按照分數範圍獲取name對應的有序集合的元素
    # # zrangebyscore(name, min, max, start=None, num=None, withscores=False, score_cast_func=float)
    
    # # 從大到小排序
    # # zrevrangebyscore(name, max, min, start=None, num=None, withscores=False, score_cast_func=float)
#-------------------

# zrank(name, value)
#  # 獲取某個值在 name對應的有序集合中的排行（從 0 開始）
#
# # 更多：
# # zrevrank(name, value)，從大到小排序
#
# zrem(name, values)
#  # 刪除name對應的有序集合中值是values的成員
# 
# # 如：zrem('zz', ['s1', 's2'])
# zremrangebyrank(name, min, max)
#   # 根據排行範圍刪除

# zremrangebyscore(name, min, max)
#   # 根據分數範圍刪除
#
# zscore(name, value)
#   # 獲取name對應有序集合中 value 對應的分數

# zinterstore(dest, keys, aggregate=None)
#   # 獲取兩個有序集合的交集，如果遇到相同值不同分數，則按照aggregate進行操作
# # aggregate的值為:  SUM  MIN  MAX

# zunionstore(dest, keys, aggregate=None)
#   # 獲取兩個有序集合的並集，如果遇到相同值不同分數，則按照aggregate進行操作
# # aggregate的值為:  SUM  MIN  MAX

# zscan(name, cursor=0, match=None, count=None, score_cast_func=float)

# zscan_iter(name, match=None, count=None, score_cast_func=float)
#   # 同字串相似，相較於字串新增score_cast_func，用來對分數進行操作





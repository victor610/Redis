# hset(name, key, value)      # name對應的hash中設置一個鍵值對（不存在，則創建；否則，修改）
#     # 參數：
#     # name，redis的name
#     # key，name對應的hash中的key
#     # value，name對應的hash中的value
# # 注：
# # hsetnx(name, key, value),當name對應的hash中不存在當前key時則創建（相當於添加）
#
# hmset(name, mapping)        # 在name對應的hash中批量設置鍵值對
#     # 參數：
#     # name，redis的name
#     # mapping，字典，如：{'k1':'v1', 'k2': 'v2'}
#
#     # 如：
#     # r.hmset('xx', {'k1':'v1', 'k2': 'v2'})
#
# hget(name, key)     # 在name對應的hash中獲取根據key獲取value
#
# hmget(name, keys, *args)        # 在name對應的hash中獲取多個key的值
#     # 參數：
#     # name，reids對應的name
#     # keys，要獲取key集合，如：['k1', 'k2', 'k3']
#     # *args，要獲取的key，如：k1,k2,k3
#
#     # 如：
#     # r.mget('xx', ['k1', 'k2'])
#     # 或
#     # print r.hmget('xx', 'k1', 'k2')
#
#
# hgetall(name)        # 獲取name對應hash的所有鍵值
# hlen(name)           # 獲取name對應的hash中鍵值對的個數
# hkeys(name)          # 獲取name對應的hash中所有的key的值
# hvals(name)          # 獲取name對應的hash中所有的value的值
# hexists(name, key)   # 檢查name對應的hash是否存在當前傳入的key
# hdel(name, *keys)    # 將name對應的hash中指定key的鍵值對刪除
#
# hincrby(name, key, amount=1)        # 自增name對應的hash中的指定key的值，不存在則創建key=amount
#     # 參數：
#     # name，redis中的name
#     # key， hash對應的key
#     # amount，自增數（整數）
# hincrbyfloat(name, key, amount=1.0)     # 自增name對應的hash中的指定key的值，不存在則創建key=amount
#     # 參數：
#     # name，redis中的name
#     # key， hash對應的key
#     # amount，自增數（浮點數）
#
#     # 自增name對應的hash中的指定key的值，不存在則創建key=amount

#hscan(name, cursor=0, match=None, count=None)           #模糊匹配
#     Start a full hashs can with:
#         HSCAN  myhash 0
#     Start a hash scan with fields matching a pattern with:
#         HSCAN myhash 0 MATCH order_ *
#     Start a hash scan with fields matching a pattern and forcing the scan command to do more scanning with:
#         HSCAN myhash 0 MATCH order_ * COUNT 1000
#      # 增量式反覆運算獲取，對於資料大的資料非常有用，hscan可以實現分片的獲取資料，並非一次性將資料全部獲取完，從而放置記憶體被撐爆
#
#     # 參數：
#     # name，redis的name
#     # cursor，游標（基於游標分批取獲取資料）
#     # match，匹配指定key，默認None 表示所有的key
#     # count，每次分片最少獲取個數，默認None表示採用Redis的默認分片個數
#
#     # 如：
#     # 第一次：cursor1, data1 = r.hscan('xx', cursor=0, match=None, count=None)
#     # 第二次：cursor2, data1 = r.hscan('xx', cursor=cursor1, match=None, count=None)
#     # ...
#     # 直到返回值cursor的值為0時，表示資料已經通過分片獲取完畢
#
#
# hscan_iter(name, match=None, count=None)        # 利用yield封裝hscan創建生成器，實現分批去redis中獲取資料
#     # 參數：
#     # match，匹配指定key，默認None 表示所有的key
#     # count，每次分片最少獲取個數，默認None表示採用Redis的默認分片個數
#
#     # 如：
#     # for item in r.hscan_iter('xx'):
#     #     print item


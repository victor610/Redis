# set(name, value, ex=None, px=None, nx=False, xx=False)
#     在Redis中設置值，默認，不存在則創建，存在則修改
#     參數：
#     ex，過期時間（秒）
#     px，過期時間（毫秒）
#     nx，如果設置為True，則只有name不存在時，當前set操作才執行
#     xx，如果設置為True，則只有name存在時，崗前set操作才執行
#
# setnx(name, value)
#     設置值，只有name不存在時，執行設置操作（添加）
#
# setex(name, value, time)
#     # 設置值
#     # 參數：
#     # time，過期時間（數位秒 或 timedelta物件）
#
#
# psetex(name, time_ms, value)
#     # 設置值
#     # 參數：
#     # time_ms，過期時間（數位毫秒 或 timedelta物件）
#
# mset(*args, **kwargs)     批量設置值如：
#     mset(k1='v1', k2='v2')
#     或
#     mget({'k1': 'v1', 'k2': 'v2'})
#
#
# get(name)     獲取值
#
# mget(keys, *args)    批量獲取如：
#     mget('ylr', 'wupeiqi')
#     或
#     r.mget(['ylr', 'wupeiqi'])
#
#
# getset(name, value)     設置新值並獲取原來的值，所以有返回值

# getrange(key, start, end)
    # 獲取子序列（根據位元組獲取，非字元）
    # 參數：
    # name，Redis 的 name
    # start，起始位置（位元組）
    # end，結束位置（位元組）
    # 如： "小五子" ，0-3表示 "小"
#
#
# setrange(name, offset, value)
#     # 修改字串內容，從指定字串索引開始向後替換（新值太長時，則向後添加）
#     # 參數：
#     # offset，字串的索引，位元組（一個漢字三個位元組）
#     # value，要設置的值
#
#
# setbit(name, offset, value)     # 對name對應值的二進位表示的位元進行操作
# # 參數：
# # name，redis的name
# # offset，位元的索引（將值變換成二進位後再進行索引）
# # value，值只能是 1 或 0
#
# # 注：如果在Redis中有一個對應： n1 = "foo"，
#     那麼字串foo的二進位表示為：
#     01100110
#     01101111
#     01101111
#     所以，如果執行setbit('n1', 7, 1)，則就會將第7位設置為1，那麼最終二進位則變成
#     01100111
#     01101111
#     01101111，即："goo"
#
#     # 擴展，轉換二進位表示：
#
#     # source = "小五子"
#     source = "foo"
#
#     for i in source:
#         num = ord(i)
#         print
#         bin(num).replace('b', '')
#
#         特別的，如果source是漢字
#         "武沛齊"
#         怎麼辦？
#         答：對於utf - 8，每一個漢字占3個位元組，那麼"小五子"則有9個位元組
#         對於漢字，for迴圈時候會按照位元組反覆運算，那麼在反覆運算時，將每一個位元組轉換十進位數字，然後再將十進位數字轉換成二進位
#         11100110
#         10101101
#         10100110
#         11100110
#         10110010
#         10011011
#         11101001
#         10111101
#         10010000
# -----------------------
# getbit(name, offset)
#     # 獲取name對應的值的二進位表示中的某位元的值 （0或1）

#bitcount(key, start=None, end=None)
#     # 獲取name對應的值的二進位表示中 1 的個數
#     # 參數：
#     # key，Redis的name
#     # start，位起始位置
#     # end，位結束位置
#
# strlen(name)
#     # 返回name對應值的位元組長度（一個漢字3個位元組）

# incr(self, name, amount=1)
#     # 自增 name對應的值，當name不存在時，則創建name＝amount，否則，則自增。
#
#     # 參數：
#     # name,Redis的name
#     # amount,自增數（必須是整數）
#
#     # 注：同incrby
#
# incrbyfloat(self, name, amount=1.0)
#     # 自增 name對應的值，當name不存在時，則創建name＝amount，否則，則自增。
#     # 參數：
#     # name,Redis的name
#     # amount,自增數（浮點型）
#
# decr(self, name, amount=1)
#     # 自減 name對應的值，當name不存在時，則創建name＝amount，否則，則自減。
#     # 參數：
#     # name,Redis的name
#     # amount,自減數（整數）
#
# append(key, value)
#     # 在redis name對應的值後面追加內容
#     # 參數：
#     key, redis的name
#     value, 要追加的字串





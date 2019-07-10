# lpush(name, values)
#     # 在name對應的list中添加元素，每個新的元素都添加到清單的最左邊
#     # 如：
#     # r.lpush('oo', 11,22,33)
#     # 保存順序為: 33,22,11
#
#     # 擴展：
#     # rpush(name, values) 表示從右向左操作
#
#
# lpushx(name, value)
#     # 在name對應的list中添加元素，只有name已經存在時，值添加到列表的最左邊
#
#     # 更多：
#     # rpushx(name, value) 表示從右向左操作
#
#
# llen(name)
# # name對應的list元素的個數
#
# linsert(name, where, refvalue, value))
#     # 在name對應的列表的某一個值前或後插入一個新值
#
#     # 參數：
#     # name，redis的name
#     # where，BEFORE 或 AFTER
#     # refvalue，標杆值，即：在它前後插入資料
#     # value，要插入的資料
#
#
# r.lset(name, index, value)
#     # 對name對應的list中的某一個索引位置重新賦值
#
#     # 參數：
#     # name，redis的name
#     # index，list的索引位置
#     # value，要設置的值
#
#
# r.lrem(name, num, value)
#     # 在name對應的list中刪除指定的值
#
#     # 參數：
#     # name，redis的name
#     # value，要刪除的值
#     # num，  num=0，刪除列表中所有的指定值；
#     # num=2,從前到後，刪除2個；
#     # num=-2,從後向前，刪除2個
#
#
# lpop(name)
#     # 在name對應的列表的左側獲取第一個元素並在清單中移除，返回值則是第一個元素
#
#     # 更多：
#     # rpop(name) 表示從右向左操作
#
#
# lindex(name, index)
#     #在name對應的清單中根據索引獲取清單元素
#
# lrange(name, start, end)
#     # 在name對應的清單分片獲取資料
#     # 參數：
#     # name，redis的name
#     # start，索引的起始位置
#     # end，索引結束位置
#
#
# ltrim(name, start, end)
#     # 在name對應的列表中移除沒有在start-end索引之間的值
#     # 參數：
#     # name，redis的name
#     # start，索引的起始位置
#     # end，索引結束位置
#
#
# rpoplpush(src, dst)
#     # 從一個清單取出最右邊的元素，同時將其添加至另一個列表的最左邊
#     # 參數：
#     # src，要取數據的清單的name
#     # dst，要添加數據的清單的name
#
# blpop(keys, timeout)
#     # 將多個列表排列，按照從左到右去pop對應清單的元素
#
#     # 參數：
#     # keys，redis的name的集合
#     # timeout，超時時間，當元素所有清單的元素獲取完之後，阻塞等待清單內有資料的時間（秒）, 0 表示永遠阻塞
#
#     # 更多：
#     # r.brpop(keys, timeout)，從右向左獲取資料
#
#
# brpoplpush(src, dst, timeout=0)
#     # 從一個清單的右側移除一個元素並將其添加到另一個列表的左側
#
#     # 參數：
#     # src，取出並要移除元素的清單對應的name
#     # dst，要插入元素的清單對應的name
#     # timeout，當src對應的清單中沒有資料時，阻塞等待其有資料的超時時間（秒），0 表示永遠阻塞
#

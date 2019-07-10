# list 列表 練習    82-07 0:00~18:22

import redis

r=redis.Redis()   #創造一個redis 對象，透過這個對象，去控制對資料庫的增刪改查


# r.lpush("names","g1",212,"g2",6666,12131,12313,"peter","g2",6666,12131,12313,"peter")   #第一個參數是要放到哪一個key下,
                                                          # 後面所有內容都是要放進去此key的內容，放進去後是一個列表
#
# print(r.llen("names"))   #取得此列表長度
#
print(r.lrange("names",0,-1))   #取得此列表範圍內的資料


# print(r.lpushx("names",123555544555))   #在name對應的list中添加元素，只有name已經存在時，值添加到列表的最左邊,不存在則不動做
#
# print(r.linsert("names","AFTER","peter","gogog-peter"))      # linsert(name, where, refvalue, value))
#                                                              # 在name對應的列表的某一個值前或後插入一個新值
#                                                              #如果有多個值，從左邊開始遇到的第一個才會執行插入
#
# print(r.lrange("names",0,-1))   #取得此列表範圍內的資料


# r.lset("names","3","test_gogo")       # 對name對應的list中的某一個索引位置重新賦值
#      #        第幾個位置,新內容

# r.lrem("names",2,"1235555")   # 在name對應的list中刪除指定的值
#             # 刪除幾個,刪除什麼值   例如 刪除兩個  值為 1235555 的

# r.lpop("names")   #從names 左邊開始尋找  ，遇到的第一列表內榮的移除

# r.lpush("name2","n1","n2","n3")
# print(r.lpop("name2"))   # 一次移除一個
# print(r.lpop("name2"))
# print(r.lpop("name2"))
# print(r.lrange("names",0,-1))   #取得此列表範圍內的資料
#
# print(r.lindex("names",2))      #在name對應的清單中根據索引獲取清單元素


# print(r.ltrim("names",6,9))    #只會留下 這個範圍索引內的值，其餘的會被移除
#             #     例如只留下 names下  索引6~9 的內容，其他的都被移除

# print(r.lindex("names",2))      #在name對應的清單中根據索引獲取清單元素


# r.rpoplpush("names","names3")  #把參數一列表的  最右邊值，  移到  參數二列表的最左邊
print(r.lrange("names",0,-1))   #取得此列表範圍內的資料，此時names 最右邊會移除少一個
print(r.lrange("names3",0,-1))   #取得此列表範圍內的資料，此時names3  最左邊會增加多一個


r.blpop("names",5)   # 將多個列表排列，按照從左到右去pop對應清單的元素
                    # timeout，超時時間，當元素所有清單的元素獲取完之後，阻塞等待清單內有資料的時間（秒）, 0 表示永遠阻塞
                    # 只要這超時時間內有成功移除這個動作，阻塞就會解除
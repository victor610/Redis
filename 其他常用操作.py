# delete(*names)
#   # 根據刪除redis中的任意資料類型

# exists(name)
#   # 檢測redis的name是否存在

# keys(pattern='*')
#   # 根據模型獲取redis的name
#
# # 更多：
# # KEYS * 匹配資料庫中所有 key 。
# # KEYS h?llo 匹配 hello ， hallo 和 hxllo 等。
# # KEYS h*llo 匹配 hllo 和 heeeeello 等。
# # KEYS h[ae]llo 匹配 hello 和 hallo ，但不匹配 hillo

# expire(name, time)
#   # 為某個redis的某個name設置超時時間

# rename(src, dst)
#   # 對redis的name重命名為

# move(name, db))
#   # 將redis的某個值移動到指定的db下
    # 但是如果另外一個DB已有此元素，則不動做
    
# randomkey()
#   # 隨機獲取一個redis的name（不刪除）

# type(name)
#   # 獲取name對應值的類型

# scan(cursor=0, match=None, count=None)
    # print(r.scan(0,match="*n*"))  #模糊匹配

# scan_iter(match=None, count=None)
#   # 同字串操作，用於增量反覆運算獲取key

# SCAN 命令是一個基於游標的反覆運算器（cursor based iterator）： SCAN 命令每次被調用之後， 都會向使用者返回一個新的游標，
# 使用者在下次反覆運算時需要使用這個新游標作為 SCAN 命令的游標參數， 以此來延續之前的反覆運算過程。
# 當 SCAN 命令的游標參數被設置為 0 時， 伺服器將開始一次新的反覆運算， 而當伺服器向用戶返回值為 0 的游標時，
# 表示反覆運算已結束。



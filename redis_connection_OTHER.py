# 其他常用操作  全局  82-*07  34:50

import redis

r=redis.Redis()   #創造一個redis 對象，透過這個對象，去控制對資料庫的增刪改查

print(r.keys())   #取得此KEY的所有內容

# r.delete("p3")  #單除此單一元素

# print(r.expire("w1",5))   超時時間，時間超過之後，就會刪除

print(r.keys())   #取得此KEY的所有內容



# 默認有16個DB,分別是 0~15  ，預設是使用第0個DB

# r.move("qoo",3)  #移動當前DB下的 某個元素， 到另外一個DB  3
#                  # 但是如果另外一個DB已有此元素，則不動做

print(r.randomkey())   #隨機獲取一個元素

print(r.type("set_names"))          # 獲取name對應值的類型
print(r.type("qoo"))                # 獲取name對應值的類型
print(r.type("sort_n3"))            # 獲取name對應值的類型

print(r.scan(0,match="*n*"))  #模糊匹配

# 82-08 22:00   連接池  & 管道

# 希望一直維持著連接，避免不斷的 段開 連接 的消耗



import redis

pool=redis.ConnectionPool(host="192.168.43.100",port=6379,db=0,password="gogo610610")   #先創造一個連接池，
    # 創造連接池之後，其他地方以後也可以使用此連接池  ，其他地方，不用再進行連接  和  段開




r = redis.Redis(connection_pool=pool)    #然後再創造一個redis 的對象，然後連接著 連接池



           #管道
pipe = r.pipeline(transaction=True)   #類似一個 事務的功能，不是全成功，就是全失敗

#透過這個管道對象，去執行動作時
pipe.set('name', 'peter')
pipe.set('role', '66666')


#使用 pipeline 管道時，必須遇到  execute  才會有結果，
# 如果再遇到 execute之前，報錯誤而沒執行 execute ，那麼之前曾經執行的東西就都不會有結果
pipe.execute()

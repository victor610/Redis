

# redis - py預設在執行每次請求都會創建（連接池申請連接）和斷開（歸還連接池）一次連接操作，
# 如果想要在一次請求中指定多個命令，則可以使用pipline實現一次請求指定多個命令，並且預設情況下一次pipline
# 是原子性操作。


 # !/usr/bin/env python
# -*- coding:utf-8 -*-

import redis

pool = redis.ConnectionPool(host='10.211.55.4', port=6379)

r = redis.Redis(connection_pool=pool)

# pipe = r.pipeline(transaction=False)
pipe = r.pipeline(transaction=True)

pipe.set('name', 'alex')
pipe.set('role', 'sb')

pipe.execute()


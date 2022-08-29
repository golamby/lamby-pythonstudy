from multiprocessing import Queue

# 进程间通信的管道--队列
q = Queue(5)

q.put(3)
q.put(99)
q.put(22)
print(q.full())
q.put(2222)
q.put(111)
print(q.full())

v1 = q.get()
v2 = q.get()
v3 = q.get()
v4 = q.get()
v5 = q.get()
print(q.empty())
# v6 = q.get()  # 没有数据时会阻塞
# v6 = q.get_nowait() # 没有直接报错 queue.Empty
v6 = q.get(timeout=3)

print(v1, v2, v3, v4, v5)
print()


"""
q.full()
q.empty()
q.get_nowait()
在多进程下不准确

"""
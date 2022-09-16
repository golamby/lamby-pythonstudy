import queue

# q = queue.Queue(3)
# q.put(1)
# q.get()
# q.get_nowait()
# q.get(timeout=3)
# q.full()
# q.empty()

q1 = queue.LifoQueue(5)  # 先进后出，栈
q1.put(1)
q1.put(2)
q1.put(3)
print(q1.get())

q2 = queue.PriorityQueue(5)
q2.put((10,'111'))
q2.put((20,'222'))
q2.put((30,'333'))
print(q2.get())



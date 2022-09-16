"""
IO复用模型
多个的进程的IO可以注册到一个复用器(select)上，然后用一个进程调用该select,，select会监听所有注册进来的IO。

如果select监听的IO在内核缓冲区都没有可读数据，select调用进程会被阻塞；而当任一IO在内核缓冲区中有可读数据时，select调用就会返回；而后select调用进程可以自己或通知另外的进程(注册进程)来再次发起读取IO，读取内核中准备好的数据。
Linux中IO复用的实现方式主要有Select，Poll和Epoll：

Select：注册IO、阻塞扫描，监听的IO最大连接数不能多于FD_ SIZE（1024）。
Poll：原理和Select相似，没有数量限制，但IO数量大，扫描线性性能下降。
Epoll ：事件驱动不阻塞，mmap实现内核与用户空间的消息传递，数量很大，Linux2.6后内核支持。


"""
#                               Daemon Thread


A daemon thread is a thread which runs continuously in the background.
It provides support to non-daemon threads. 
When last non-daemon thread terminates, automatically all daemon threads will be terminated. 
We are not required to terminate daemon thread explicitly



#                               Create Daemon Thread


setDaemon(True) Method or daemon = True Property is used to make a thread a Daemon thread.
Ex:- 
t1 = Thread(target=disp)
t1.setDaemon(True)
t1.daemon = True



#                                   Method


setDaemon(True/False) - This method is used to set a thread as daemon thread. 
You can set thread as daemon only before starting that thread which means active thread status cannot be changed as daemon. 
If we pass True non-daemon thread will become daemon and if False daemon thread will become non-daemon.

daemon Property - This property is used to check whether a thread is daemon or not. It returns True if thread is daemon else False.
We can also use daemon property to set a thread as daemon thread or vice versa. 

isDaemon() - This method is used to check whether a thread is daemon or not. It returns True if thread is daemon else False.



#                       Default Nature of Thread


Main Thread is always non-daemon thread. 
Rest of the threads inherits daemon nature from their parents.
If parent thread is non daemon then child thread will become non daemon thread.
If parent thread is daemon then child thread will also become a daemon thread. 
When last non-daemon thread terminates, automatically all daemon threads will be terminated. We are not required to terminate daemon thread explicitly.

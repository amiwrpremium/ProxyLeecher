from leecher import *
from threading import Thread

t1 = Thread(target=free_proxy_list)
t2 = Thread(target=xcoder)
t3 = Thread(target=http_tunnel)
t4 = Thread(target=hide_my_name)
t5 = Thread(target=free_proxy)
t6 = Thread(target=spysme1)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()

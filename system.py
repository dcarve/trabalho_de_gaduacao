# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:02:25 2021

@author: daniel carvalho
"""


from send_cloud.main import thread_main as send_cloud
from read_sensors.main import thread_main as read_sensors


import threading



threads = list()


x = threading.Thread(target=send_cloud)
threads.append(x)
x.start()


x = threading.Thread(target=read_sensors)
threads.append(x)
x.start()



for index, thread in enumerate(threads):

    thread.join()

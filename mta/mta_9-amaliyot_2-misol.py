# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 21:56:54 2023

@author: Lenovo
"""

from queue import Queue

navbat = Queue()

navbat.put(3)
navbat.put(1)
navbat.put(4)
navbat.put(2)
navbat.put(5)

uzunlik = navbat.qsize()

i = -1

while not navbat.empty():
    i += 1
    element = navbat.get()
    if uzunlik % 2 != 0:
        if i != uzunlik//2:
            print(element, end=" ")
    else:
        if i != (uzunlik/2 - 1) or i != uzunlik/2:
            print(element, end=" ")
        else:
            navbat.get()
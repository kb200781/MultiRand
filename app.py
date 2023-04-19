import streamlit as st
import os
import random as r
import sys
import platform
import multiprocessing
import threading
import time

st.write("OS Type: ", os.name)

st.write("OS Name: ", sys.platform)

st.write("OS Platform: ", platform.platform())

numberOfCores = multiprocessing.cpu_count()
st.write("Num of cores are: ", numberOfCores)

activeThread = threading.activeCount()
st.write("Num of threads: ", activeThread)

st.write("Present working directory: ", os.getcwd())

def task (lb, ub, refreshTime, displayLocation):
    while(1):
        num = r.randint(lb, ub)
        # display(num, displayLocation)
        st.write(f'.thread {displayLocation} got {num}')
        time.sleep(refreshTime)
    return

t1 = threading.Thread(target=task, args=(10,20,10,10))
t2 = threading.Thread(target=task, args=(-10,10,20,20))
t3 = threading.Thread(target=task, args=(-100,0,8,30))
t4 = threading.Thread(target=task, args=(0,20,12,40))
t5 = threading.Thread(target=task, args=(-40,40,16,50))
t6 = threading.Thread(target=task, args=(100,200,14,60))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()

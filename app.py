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

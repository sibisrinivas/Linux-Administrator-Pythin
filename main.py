import time, threading
import os

def run_periodically():
    os.system("fab host_type")
    threading.Timer(10, run_periodically).start()

run_periodically()
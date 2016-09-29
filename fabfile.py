from fabric.api import *
from itertools import *

import matplotlib.pyplot as plt
import datetime
import time
import csv
import sys

class MachineStats:
    cpu_load = 0
    num_logged = 0

env.user = 'deepak'
env.password = 'password123'
#list of Hosts
department_qa=['deepak-Vm']
department_engineering=['deepak-Vm']
env.hosts = chain(department_qa,department_engineering)
def host_type():
    try:
        host_name= env.host
        print host_name
        run('uname -s')
        #CPU Usage
        cpu_usage = run("echo $[100-$(vmstat|tail -1|awk '{print $15}')]")
        cpu_usage
        #Number of Logged in Users
        logged_in_users_count = run ("who | cut -d' ' -f1 | uniq| wc -l")
        logged_in_users = run("who | cut -d' ' -f1 | sort | uniq")
        print "Hostname: " + host_name + " -- Cpu_usage is " + cpu_usage + "% -- Logged in users count is: " + logged_in_users_count + " -- Logged in user: "+logged_in_users
        ts=time.time()
        time_stamp= datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        with open('datalog'+time_stamp+'.csv', 'ab') as csvfile:
           spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
           data=[env.host,cpu_usage,logged_in_users_count,logged_in_users]
           spamwriter.writerow(data)
    except:
       error_type=sys.exc_info()[0]
       error=sys.exc_info()[1]
       print "Error Type:"+str(error_type)
       print "Error:"+str(error)
  
def per_host_call(hostnm):
    try:
       env.host = hostnm
       run('uname -s')
       #Disk Space
       disk_space = run ('df')
       #CPU Usage
       cpu_usage = run("echo $[100-$(vmstat|tail -1|awk '{print $15}')]")
       #Number of Logged in Users
       logged_in_users_count = run ("who | cut -d' ' -f1 | uniq| wc -l")
       logged_in_users = run("who | cut -d' ' -f1 | sort | uniq")
       print "Hostname: " + hostnm + " -- Cpu_usage is " + cpu_usage + "% -- Logged in users count is: " + logged_in_users_count + " -- Logged in user: "+logged_in_users
       ts=time.time()
       time_stamp= datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
       with open(hostnm+'.csv', 'ab') as csvfile:
   	 spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
   	 data=[hostnm,cpu_usage,logged_in_users_count,logged_in_users]
     	 spamwriter.writerow(data)
    except:
       error_type=sys.exc_info()[0]
       error=sys.exc_info()[1]
       print "Error Type:"+str(error_type)
       print "Error:"+str(error)
 
def plot_graph(hostnm):
    try:
       cpu_usage=[0]
       with open(hostnm+'.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
         cpu_usage.append(row[1])
        print "CPU Usage:"
        print cpu_usage
        plt.title(hostnm)
        plt.plot(cpu_usage)
        plt.ylabel('Percent')
        plt.xlabel('Hour')
        plt.show()
    except:
       error_type=sys.exc_info()[0]
       error=sys.exc_info()[1]
       print "Error Type:"+str(error_type)
       print "Error:"+str(error)


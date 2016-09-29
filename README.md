# Linux-Administrator-Python:


Modules used:
•	Fabric
•	Itertools 
•	Matplotlib.pyplot
•	DateTime
•	Csv

Description:
ADLI is a software tool which helps linux administrator of a company to find the usage of these machines. The information might include CPU load, memory used, available disk space, number of logged in users etc. The program run hourly and save’s the above information into a csv file.
Contain’s four main features:
1.	Collect the data for all the listed machine
2.	Collect the data for Single machine
3.	Collect Data periodically
4.	Graphical Representation
Python elements used in this project:
1.	List data structure
2.	Class
3.	Function
4.	External Module – Fabric,Matplotlib.pyplot
5.	Itertools
6.	File input and output
7.	Try catch for handling exception
Commands to perform operation:
1.	To run for one host (host supplied by user):
fab per_host_call:hostnm="deepak-Vm"
2.	For Periodic (for every 1 hour) execution"
python main.py 

3.	To run the CPU usage plot graph:
fab plot_graph:hostnm="deepak-Vm"

4.	To run the commands once for all the hosts:
fab host_type


#!/usr/bin/env python

# Author Dr. Ziad Salem
#Add hearin to the lines 
#Search for 'ir_raw' in the file, then save the sensors values only into a new file
#I took the time off (secod line) but in that case we have to be careful to separate the backgroung from the rest of the file.
#either we check the time stamp about when the the real bees recording start
#or we blink the top led (diagnosticled) for 1 sec and we check that from the log file


import time
import argparse
import subprocess
import csv
import sys
from datetime import datetime

if __name__ == '__main__':
	timestamp = time.time() 
 	my_row = []


	with open('/home/assisi/assisi/IR_sensors_validations_2017/logs/2017-10-19-12-33-35-casu-006.csv', 'rt') as f1:
		with open('/home/assisi/assisi/IR_sensors_validations_2017/logs/IR_raw_'+str(datetime.now())+'.csv', 'w') as f2:
			reader = csv.reader(f1)
			w = csv.writer(f2)
			w.writerow(('F','FL','BL','B','BR','FR'))		
			for row in reader:
				if row [0] == "ir_raw":
					print row[2], row[3], row[4], row[5],row[6], row[7] 
					my_row = []							
					my_row.append(row[2])
   					my_row.append(row[3])
    					my_row.append(row[4])
					my_row.append(row[5])
   					my_row.append(row[6])
    					my_row.append(row[7])					
					w.writerow (my_row )
	f1.close()
	f2.close()


print "end"
        

